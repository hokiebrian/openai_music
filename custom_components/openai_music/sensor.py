""" OpenAI Inquiry Sensor and Services """

import logging
import time
import asyncio
import openai
import aiohttp
from openai import error
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_API_KEY
from .const import (
    DOMAIN,
    DEFAULT_SONG_TITLE,
    DEFAULT_SONG_ARTIST,
    DEFAULT_CHAT_MODEL,
    DEFAULT_USER_TAG,
    DEFAULT_MAX_TOKENS,
    DEFAULT_TEMPERATURE,
    DEFAULT_IMG_COUNT,
    DEFAULT_IMAGE_TYPE,
    DEFAULT_IMAGE_RESOLUTION,
    DEFAULT_IMAGE_QUALITY,
    DEFAULT_IMAGE_STYLE,
    DEFAULT_IMAGE_MODEL,
    ERROR_IMG,
    MAX_RETRIES,
    PERSONALITIES,
    PROMPTS,
    IMAGE_TYPES,
    IMAGE_PROMPT,
)


_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, config_entry, async_add_entities):
    """Setup Sensors"""
    sensors = [
        OpenAiTextSensor(config_entry),
        OpenAiImageSensor(config_entry),
        OpenAiTextSensorSecondary(config_entry),
    ]

    for sensor in sensors:
        async_add_entities([sensor], True)


class OpenAiTextSensor(Entity):
    """OpenAI Music Text Sensor"""

    _attr_icon = "mdi:information-slab-box"

    def __init__(self, config_entry):
        self.api_key = config_entry.data[CONF_API_KEY]
        self.config = config_entry
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
        start_time = time.time()
        call_data = call.data
        song_title = call_data.get("song_title", DEFAULT_SONG_TITLE)
        song_artist = call_data.get("song_artist", DEFAULT_SONG_ARTIST)
        ai_personality_name = call_data["personality"]
        song_info = f"{song_title} by {song_artist}"
        ai_request_time = 0

        text_session = aiohttp.ClientSession()

        config_options = self.config.options
        temperature = config_options.get("temperature", DEFAULT_TEMPERATURE)
        max_tokens = config_options.get("max_tokens", DEFAULT_MAX_TOKENS)
        model = config_options.get("chat_model", DEFAULT_CHAT_MODEL)
        user_tag = config_options.get("user_tag", DEFAULT_USER_TAG).strip()
        max_retry_attempts = MAX_RETRIES
        retry_count = 0

        _LOGGER.debug(song_info)

        ai_prompt = (
            self._get_from_config(call_data, "prompt", PROMPTS) or call_data["prompt"]
        )
        ai_personality = self._get_from_config(call_data, "personality", PERSONALITIES)

        if ai_personality is None:
            ai_personality = f"Answer as a {call_data.get('personality')}"

        messages = [
            {
                "role": "system",
                "content": ai_personality,
            },
            {"role": "user", "content": f"{ai_prompt} Song: {song_info}"},
        ]

        _LOGGER.debug(messages)

        openai.aiosession.set(text_session)

        while retry_count < max_retry_attempts:
            try:
                data = await openai.ChatCompletion.acreate(
                    model=model,
                    messages=messages,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    user=user_tag,
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
                    "personality": ai_personality_name,
                }

                self._state = song_info
                break

            except error.OpenAIError as err:
                _LOGGER.error("There was an Error: %s - %s", song_info, str(err))
                retry_count += 1
                self._attributes = {
                    "info": str(err),
                    "tokens": 0,
                    "fetched": int(time.time()),
                    "request": messages,
                    "prompt": ai_prompt,
                    "personality": ai_personality_name,
                }
                self._state = f"Error: {str(err)}"[:254]

        await openai.aiosession.get(text_session).close()
        elapsed_time = time.time() - start_time
        self._attributes["elapsed_time"] = round(elapsed_time, 2)
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


class OpenAiTextSensorSecondary(Entity):
    """OpenAI Music Text Sensor #2"""

    _attr_icon = "mdi:information-slab-box"

    def __init__(self, config_entry):
        self.api_key = config_entry.data[CONF_API_KEY]
        self.config = config_entry
        self._state = None
        self._attributes = {}
        openai.api_key = self.api_key

    async def async_added_to_hass(self):
        self.hass.services.async_register(
            DOMAIN, "ask_openai_secondary", self.async_ask_openai
        )

    async def async_will_remove_from_hass(self):
        self.hass.services.async_remove(DOMAIN, "ask_openai_secondary")

    @staticmethod
    def _get_from_config(call_data, key, defaults):
        """Gets configuration data with case-insensitive key matching."""
        lc_key = {k.lower(): v for k, v in defaults.items()}
        return lc_key.get(call_data.get(key, "").lower(), defaults.get(key))

    async def async_ask_openai(self, call):
        """Fetch the song info from the AI model."""
        start_time = time.time()
        call_data = call.data
        song_title = call_data.get("song_title", DEFAULT_SONG_TITLE)
        song_artist = call_data.get("song_artist", DEFAULT_SONG_ARTIST)
        ai_personality_name = call_data["personality"]
        song_info = f"{song_title} by {song_artist}"

        text_session_secondary = aiohttp.ClientSession()

        config_options = self.config.options
        temperature = config_options.get("temperature", DEFAULT_TEMPERATURE)
        max_tokens = config_options.get("max_tokens", DEFAULT_MAX_TOKENS)
        model = config_options.get("chat_model", DEFAULT_CHAT_MODEL)
        user_tag = config_options.get("user_tag", DEFAULT_USER_TAG).strip()
        max_retry_attempts = MAX_RETRIES
        retry_count = 0

        _LOGGER.debug(song_info)

        ai_prompt = (
            self._get_from_config(call_data, "prompt", PROMPTS) or call_data["prompt"]
        )
        ai_personality = self._get_from_config(call_data, "personality", PERSONALITIES)

        if ai_personality is None:
            ai_personality = f"Answer as a {call_data.get('personality')}"

        messages = [
            {
                "role": "system",
                "content": ai_personality,
            },
            {"role": "user", "content": f"{ai_prompt} Song: {song_info}"},
        ]

        _LOGGER.debug(messages)

        openai.aiosession.set(text_session_secondary)

        while retry_count < max_retry_attempts:
            try:
                data = await openai.ChatCompletion.acreate(
                    model=model,
                    messages=messages,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    user=user_tag,
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
                    "personality": ai_personality_name,
                }

                self._state = song_info
                break

            except error.OpenAIError as err:
                _LOGGER.error("There was an Error: %s - %s", song_info, str(err))
                retry_count += 1
                self._attributes = {
                    "info": str(err),
                    "tokens": 0,
                    "fetched": int(time.time()),
                    "request": messages,
                    "prompt": ai_prompt,
                    "personality": ai_personality_name,
                }
                self._state = f"Error: {str(err)}"[:254]

        await openai.aiosession.get(text_session_secondary).close()
        elapsed_time = time.time() - start_time
        self._attributes["elapsed_time"] = round(elapsed_time, 2)
        self.async_write_ha_state()

    @property
    def name(self):
        return "OpenAI Music Info Secondary"

    @property
    def state(self):
        return self._state

    @property
    def unique_id(self):
        return f"AskOpenAI_2{self.api_key[:7]}"

    @property
    def extra_state_attributes(self):
        return self._attributes


class OpenAiImageSensor(Entity):
    """OpenAI Image Creation"""

    _attr_icon = "mdi:multimedia"

    def __init__(self, config_entry):
        self.api_key = config_entry.data[CONF_API_KEY]
        self.config = config_entry
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
        start_time = time.time()
        max_retry_attempts = MAX_RETRIES
        retry_count = 0
        token_count_img = 0
        ai_prompt = IMAGE_PROMPT

        img_session = aiohttp.ClientSession()

        # Get Service Call Data
        call_data = call.data
        song_title = call_data.get("song_title", DEFAULT_SONG_TITLE)
        song_artist = call_data.get("song_artist", DEFAULT_SONG_ARTIST)
        song_info = f"{song_title} by {song_artist}"

        # Get Integration Options or use defaults
        config_options = self.config.options
        img_count = config_options.get("img_count", DEFAULT_IMG_COUNT)
        user_tag = config_options.get("user_tag", DEFAULT_USER_TAG)
        size = config_options.get("img_resolution", DEFAULT_IMAGE_RESOLUTION)
        img_quality = config_options.get("img_quality", DEFAULT_IMAGE_QUALITY)
        img_style = config_options.get("img_style", DEFAULT_IMAGE_STYLE)
        img_model = config_options.get("img_model", DEFAULT_IMAGE_MODEL)

        image_type = (
            self._get_from_config(call_data, "image_type", IMAGE_TYPES)
            or call_data["image_type"]
        )
        image_type_name = call_data.get("image_type", DEFAULT_IMAGE_TYPE)

        _LOGGER.debug(song_info)

        messages = f"{ai_prompt} SONG: {song_info}, STYLE: {image_type}"

        _LOGGER.debug(messages)

        openai.aiosession.set(img_session)

        while retry_count < max_retry_attempts:
            try:
                song_data = f"SONG: {song_info}, STYLE: {image_type}"
                token_count_img = 0

                prompt = messages
                image_data_list = []

                openai.aiosession.set(img_session)

                tasks = [
                    openai.Image.acreate(
                        prompt=prompt,
                        model=img_model,
                        n=1,
                        quality=img_quality,
                        size=size,
                        style=img_style,
                        user=user_tag,
                    )
                    for _ in range(img_count)
                ]

                responses = await asyncio.gather(*tasks)

                for data_img in responses:
                    for image_info in data_img["data"]:
                        image_with_time = {
                            "revised_prompt": image_info["revised_prompt"],
                            "url": image_info["url"],
                            "ai_request_time": data_img["created"],
                        }
                        image_data_list.append(image_with_time)
                    _LOGGER.debug(data_img)

                ai_request_time = responses[-1]["created"] if responses else None

                self._attributes = {
                    "song": song_info,
                    "type": image_type_name,
                    "image": image_data_list,
                    "image_count": img_count,
                    "fetched": ai_request_time,
                    "desc": song_data,
                    "tokens": token_count_img,
                    "messages": messages,
                }

                self._state = f"{song_info} - {ai_request_time} - {image_type_name}"
                break

            except error.OpenAIError as err:
                _LOGGER.error("There was an Error: %s - %s", song_info, str(err))
                _LOGGER.debug(ai_prompt)
                retry_count += 1
                self._attributes = {
                    "song": song_info,
                    "type": image_type_name,
                    "image": [
                        {"url": ERROR_IMG},
                        {"revised_prompt": err},
                        {"ai_request_time": ai_request_time},
                    ],
                    "image_count": 1,
                    "fetched": int(time.time()),
                    "desc": str(err),
                    "tokens": token_count_img,
                    "messages": messages,
                }
                self._state = "ERROR"

        await openai.aiosession.get(img_session).close()
        elapsed_time = time.time() - start_time
        self._attributes["elapsed_time"] = round(elapsed_time, 2)
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
