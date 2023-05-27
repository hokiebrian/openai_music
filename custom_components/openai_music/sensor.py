""" OpenAI Inquiry Sensor and Services """

import logging
import time
import openai
from openai import error
from aiohttp import ClientSession
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_API_KEY
from .const import (
    DOMAIN,
    DEFAULT_SONG_TITLE,
    DEFAULT_SONG_ARTIST,
    DEFAULT_CHAT_MODEL,
    DEFAULT_MAX_TOKENS,
    DEFAULT_MAX_IMG_TOKENS,
    DEFAULT_TEMPERATURE,
    DEFAULT_IMG_TEMPERATURE,
    DEFAULT_IMAGE_TYPE,
    DEFAULT_IMAGE_RESOLUTION,
    ERROR_IMG,
    MAX_RETRIES,
    PERSONALITIES,
    PROMPTS,
    IMAGE_TYPES,
)


_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, config_entry, async_add_entities):
    """Setup Sensors"""
    sensors = [
        OpenAiTextSensor(config_entry),
        OpenAiImageSensor(config_entry),
    ]

    for sensor in sensors:
        async_add_entities([sensor], True)


class OpenAiTextSensor(Entity):
    """OpenAI Music Text Sensor"""

    _attr_icon = "mdi:information-slab-box"

    def __init__(self, config_entry):
        self.api_key = config_entry.data[CONF_API_KEY]
        self._state = None
        self._attributes = {}
        openai.api_key = self.api_key

    async def async_added_to_hass(self):
        self.hass.services.async_register(DOMAIN, "ask_openai", self.async_ask_openai)

    async def async_will_remove_from_hass(self):
        self.hass.services.async_remove(DOMAIN, "ask_openai")

    @staticmethod
    def _get_from_config(call_data, key, defaults):
        """Gets configuration data with case-insensitive key matching."""
        lc_key = {k.lower(): v for k, v in defaults.items()}
        return lc_key.get(call_data.get(key, "").lower(), defaults.get(key))

    async def async_ask_openai(self, call):
        """Fetch the song info from the AI model."""
        song_title = call.data.get("song_title", DEFAULT_SONG_TITLE)
        song_artist = call.data.get("song_artist", DEFAULT_SONG_ARTIST)
        song_info = f"{song_title} by {song_artist}"
        openai.aiosession.set(ClientSession())

        _LOGGER.debug(song_info)

        ai_prompt = self._get_from_config(call.data, "prompt", PROMPTS)
        ai_personality = self._get_from_config(call.data, "personality", PERSONALITIES)

        if ai_personality is None:
            ai_personality = f"Answer as a {call.data.get('personality')}"

        model = DEFAULT_CHAT_MODEL
        temperature = DEFAULT_TEMPERATURE
        messages = [
            {"role": "system", "content": ai_personality},
            {"role": "user", "content": f"{ai_prompt} {song_info}"},
        ]
        max_tokens = DEFAULT_MAX_TOKENS

        _LOGGER.debug(messages)

        try:
            data = await openai.ChatCompletion.acreate(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
            )

            _LOGGER.debug(data)

            song_data = data["choices"][0]["message"]["content"].strip()
            token_count = data["usage"]["total_tokens"]
            ai_request_time = data["created"]

            self._attributes = {
                "info": song_data,
                "tokens": token_count,
                "fetched": ai_request_time,
                "request": messages,
                "prompt": ai_prompt,
                "personality": ai_personality,
            }

            self._state = song_info

        except error.OpenAIError as err:
            _LOGGER.error(err)
            _LOGGER.debug(ai_prompt)
            self._state = f"Error: {err}"[:254]

        finally:
            await openai.aiosession.get().close()
            self.async_write_ha_state()

    @property
    def name(self):
        return "OpenAI Music Info"

    @property
    def state(self):
        return self._state

    @property
    def unique_id(self):
        return f"AskOpenAI{self.api_key[:7]}"

    @property
    def extra_state_attributes(self):
        return self._attributes


class OpenAiImageSensor(Entity):
    """OpenAI Image Creation"""

    _attr_icon = "mdi:multimedia"

    def __init__(self, config_entry):
        self.api_key = config_entry.data[CONF_API_KEY]
        self._state = None
        self._attributes = {}
        openai.api_key = self.api_key

    async def async_added_to_hass(self):
        self.hass.services.async_register(
            DOMAIN, "get_openai_image", self.async_get_openai_image
        )

    async def async_will_remove_from_hass(self):
        self.hass.services.async_remove(DOMAIN, "get_openai_image")

    @staticmethod
    def _get_from_config(call_data, key, defaults):
        """Gets configuration data with case-insensitive key matching."""
        lc_key = {k.lower(): v for k, v in defaults.items()}
        return lc_key.get(call_data.get(key, "").lower(), defaults.get(key))

    async def async_get_openai_image(self, call):
        """Fetch the song info from the AI model."""
        max_retry_attempts = MAX_RETRIES
        retry_count = 0

        song_title = call.data.get("song_title", DEFAULT_SONG_TITLE)
        song_artist = call.data.get("song_artist", DEFAULT_SONG_ARTIST)
        song_info = f"{song_title} by {song_artist}"
        image_type_name = call.data.get("image_type", DEFAULT_IMAGE_TYPE)
        image_type = self._get_from_config(call.data, "image_type", IMAGE_TYPES)
        openai.aiosession.set(ClientSession())
        _LOGGER.debug(song_info)

        ai_prompt = (
            "You are describing in 400 characters or less, in as much detail as possible, "
            f"a SFW {image_type} image for the Song that would reflect the lyrical themes, "
            "lyrical content and the band's style for an AI image generator."
        )

        model = DEFAULT_CHAT_MODEL
        temperature = DEFAULT_TEMPERATURE
        messages = [
            {"role": "system", "content": ai_prompt},
            {"role": "user", "content": f"Song: {song_info}"},
        ]
        max_tokens = DEFAULT_MAX_IMG_TOKENS
        temperature = DEFAULT_IMG_TEMPERATURE

        _LOGGER.debug(messages)

        while retry_count < max_retry_attempts:
            try:
                data = await openai.ChatCompletion.acreate(
                    model=model,
                    messages=messages,
                    max_tokens=max_tokens,
                    temperature=temperature,
                )

                _LOGGER.debug(data)

                song_data = data["choices"][0]["message"]["content"].strip()
                token_count_img = data["usage"]["total_tokens"]

                prompt = song_data
                size = DEFAULT_IMAGE_RESOLUTION

                data_img = await openai.Image.acreate(prompt=prompt, size=size)

                _LOGGER.debug(data_img)

                image_data = data_img["data"][0]["url"]
                ai_request_time = data_img["created"]

                self._attributes = {
                    "song": song_info,
                    "type": image_type_name,
                    "image": image_data,
                    "fetched": ai_request_time,
                    "desc": song_data,
                    "tokens": token_count_img,
                }

                self._state = f"{song_info} - {ai_request_time} - {image_type_name}"
                break

            except error.OpenAIError as err:
                _LOGGER.error("There was an Error: %s - %s", song_info, str(err))
                _LOGGER.debug(ai_prompt)
                self._attributes = {
                    "song": song_info,
                    "type": image_type_name,
                    "image": ERROR_IMG,
                    "fetched": int(time.time()),
                    "desc": str(err),
                    "tokens": token_count_img,
                }
                retry_count += 1
                self._state = "ERROR"

            finally:
                await openai.aiosession.get().close()
                self.async_write_ha_state()

    @property
    def name(self):
        return "OpenAI Music Image"

    @property
    def state(self):
        return self._state

    @property
    def unique_id(self):
        return f"GetOpenAIImage{self.api_key[:7]}"

    @property
    def extra_state_attributes(self):
        return self._attributes
