""" OpenAI Inquiry Sensor and Services """

import logging
import time
import openai
from openai import error
from aiohttp import ClientSession
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_API_KEY
from .const import *

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

    _LOGGER = logging.getLogger(__name__)
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

    async def async_ask_openai(self, call):
        """Fetch the song info from the AI model."""
        song_title = call.data.get("song_title", DEFAULT_SONG_TITLE)
        song_artist = call.data.get("song_artist", DEFAULT_SONG_ARTIST)
        song_info = f"{song_title} by {song_artist}"

        self._LOGGER.debug(song_info)

        prompt = call.data.get("prompt", DEFAULT_PROMPT)
        personality = call.data.get("personality", DEFAULT_PERSONALITY)

        lc_prompt = {key.lower(): value for key, value in PROMPTS.items()}
        match_prompt = lc_prompt.get(prompt.lower())

        if match_prompt is not None:
            ai_prompt = match_prompt
        else:
            ai_prompt = DEFAULT_PROMPT

        lc_personality = {key.lower(): value for key, value in PERSONALITIES.items()}
        match_personality = lc_personality.get(personality.lower())

        if match_personality is not None:
            ai_personality = match_personality
        else:
            ai_personality = f"Answer as a {personality}"

        model = DEFAULT_CHAT_MODEL
        temperature = DEFAULT_TEMPERATURE
        messages = [
            {"role": "system", "content": ai_personality},
            {"role": "user", "content": f"{ai_prompt} {song_info}"},
        ]
        max_tokens = DEFAULT_MAX_TOKENS
        temperature = DEFAULT_TEMPERATURE

        self._LOGGER.debug(messages)

        openai.aiosession.set(ClientSession())

        try:
            data = await openai.ChatCompletion.acreate(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
            )

            self._LOGGER.debug(data)

            song_data = data["choices"][0]["message"]["content"].strip()
            token_count = data["usage"]["total_tokens"]
            ai_request_time = data["created"]

            self._attributes = {
                "info": song_data,
                "tokens": token_count,
                "fetched": ai_request_time,
                "request": messages,
                "prompt": prompt,
                "personality": personality,
            }

            self._state = song_info

        except error.OpenAIError as err:
            self._LOGGER.error(err)
            self._LOGGER.debug(prompt)
            self._state = f"Error: {err}"[:254]

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

    _LOGGER = logging.getLogger(__name__)
    _attr_icon = "mdi:multimedia"

    def __init__(self, config_entry):
        self.api_key = config_entry.data[CONF_API_KEY]
        self._state = None
        self._attributes = {}

    async def async_added_to_hass(self):
        self.hass.services.async_register(
            DOMAIN, "get_openai_image", self.async_get_openai_image
        )

    async def async_will_remove_from_hass(self):
        self.hass.services.async_remove(DOMAIN, "get_openai_image")

    async def async_get_openai_image(self, call):
        """Fetch the song info from the AI model."""
        max_retry_attempts = 2
        retry_count = 0

        song_title = call.data.get("song_title", DEFAULT_SONG_TITLE)
        song_artist = call.data.get("song_artist", DEFAULT_SONG_ARTIST)
        song_info = f"{song_title} by {song_artist}"
        image_type = call.data.get("image_type", DEFAULT_IMAGE_TYPE)

        self._LOGGER.debug(song_info)

        img_prompt = {key.lower(): value for key, value in IMAGE_TYPES.items()}
        img_match_prompt = img_prompt.get(image_type.lower())

        if img_match_prompt is not None:
            image_prompt = img_match_prompt
        else:
            image_prompt = image_type

        ai_prompt = (
            "You are describing in 400 characters or less, in as much detail as possible, "
            f"a SFW {image_prompt} image for the Song that would reflect the lyrical themes, "
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

        self._LOGGER.debug(messages)

        openai.aiosession.set(ClientSession())

        try:
            data = await openai.ChatCompletion.acreate(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
            )

            self._LOGGER.debug(data)

            song_data = data["choices"][0]["message"]["content"].strip()
            token_count_img = data["usage"]["total_tokens"]

            prompt = song_data
            size = DEFAULT_IMAGE_RESOLUTION

        except error.OpenAIError as err:
            self._LOGGER.error(err)
            self._state = f"Error: {err}"[:254]

        while retry_count < max_retry_attempts:
            try:
                data_img = await openai.Image.acreate(prompt=prompt, size=size)

                self._LOGGER.debug(data_img)

                image_data = data_img["data"][0]["url"]
                ai_request_time = data_img["created"]

                self._attributes = {
                    "song": song_info,
                    "type": image_type,
                    "image": image_data,
                    "fetched": ai_request_time,
                    "desc": song_data,
                    "tokens": token_count_img,
                }

                self._state = f"{song_info} - {ai_request_time} - {image_type}"
                break

            except error.OpenAIError as err:
                self._LOGGER.error(f"There was an Error: {song_info} - {str(err)}")
                self._LOGGER.debug(prompt)
                self._attributes = {
                    "song": song_info,
                    "type": image_type,
                    "image": ERROR_IMG,
                    "fetched": int(time.time()),
                    "desc": str(err),
                    "tokens": token_count_img,
                }
                retry_count += 1
                self._state = "ERROR"

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
