""" OpenAI Inquiry Sensor and Services """

import logging
import time
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
            {"role": "system", "content": ai_personality},
            {"role": "user", "content": f"{ai_prompt} {song_info}"},
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
            {"role": "system", "content": ai_personality},
            {"role": "user", "content": f"{ai_prompt} {song_info}"},
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

        img_session = aiohttp.ClientSession()

        # Get Service Call Data
        call_data = call.data
        song_title = call_data.get("song_title", DEFAULT_SONG_TITLE)
        song_artist = call_data.get("song_artist", DEFAULT_SONG_ARTIST)
        song_info = f"{song_title} by {song_artist}"

        # Get Integration Options or use defaults
        config_options = self.config.options
        temperature = config_options.get("img_temperature", DEFAULT_IMG_TEMPERATURE)
        max_tokens = config_options.get("max_tokens", DEFAULT_MAX_IMG_TOKENS)
        model = config_options.get("chat_model", DEFAULT_CHAT_MODEL)
        user_tag = config_options.get("user_tag", DEFAULT_USER_TAG)
        size = config_options.get("img_resolution", DEFAULT_IMAGE_RESOLUTION)

        image_type = (
            self._get_from_config(call_data, "image_type", IMAGE_TYPES)
            or call_data["image_type"]
        )
        image_type_name = call_data.get("image_type", DEFAULT_IMAGE_TYPE)

        _LOGGER.debug(song_info)

        ai_prompt = (
            "Create a prompt in 3 sentences or less for "
            "a detailed Style image for the Song that would provide an "
            "intepretation of the lyrics. "
            "Provide only descriptive text emphasizing detail, style and lyrical themes. "
            "Don't use the word create. Speak in the present tense."
        )

        messages = [
            {"role": "system", "content": ai_prompt},
            {"role": "user", "content": f"Song: {song_info}, Style: {image_type}"},
        ]

        _LOGGER.debug(messages)

        openai.aiosession.set(img_session)

        # Retry if error. It's possible the safety system will flag it multiple times
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
                token_count_img = data["usage"]["total_tokens"]

                prompt = song_data

                openai.aiosession.set(img_session)
                data_img = await openai.Image.acreate(
                    prompt=prompt, size=size, user=user_tag
                )

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
                retry_count += 1
                self._attributes = {
                    "song": song_info,
                    "type": image_type_name,
                    "image": ERROR_IMG,
                    "fetched": int(time.time()),
                    "desc": str(err),
                    "tokens": token_count_img,
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
