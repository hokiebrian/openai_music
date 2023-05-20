""" OpenAI Inquiry Sensor """

import logging
import aiohttp
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_API_KEY
from .const import *

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, config_entry, async_add_entities):
    sensors = [
        OpenAiTextSensor(config_entry),
        OpenAiImageSensor(config_entry),
    ]

    for sensor in sensors:
        async_add_entities([sensor], True)


class OpenAiTextSensor(Entity):
    _LOGGER = logging.getLogger(__name__)

    def __init__(self, config_entry):
        self.api_key = config_entry.data[CONF_API_KEY]
        self._state = None
        self._attributes = {}

    async def async_added_to_hass(self):
        self.hass.services.async_register(DOMAIN, "ask_openai", self.async_ask_openai)

    async def async_will_remove_from_hass(self):
        self.hass.services.async_remove(DOMAIN, "ask_openai")

    async def async_ask_openai(self, call):
        """Fetch the song info from the AI model."""
        # Connect to the OpenAI API and send the song info and personality
        song_title = call.data.get("song_title", DEFAULT_SONG_TITLE)
        song_artist = call.data.get("song_artist", DEFAULT_SONG_ARTIST)
        song_info = f"{song_title} by {song_artist}"

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

        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "max_tokens": DEFAULT_MAX_TOKENS,
            "model": DEFAULT_CHAT_MODEL,
            "temperature": DEFAULT_TEMPERATURE,
            "messages": [
                {"role": "system", "content": ai_personality},
                {"role": "user", "content": f"{ai_prompt} {song_info}"},
            ],
        }

        async with aiohttp.ClientSession() as session:
            response = await session.post(
                API_URL,
                headers=headers,
                json=payload,
            )
            data = await response.json()
            self._LOGGER.debug(data)

        song_data = data["choices"][0]["message"]["content"].strip()
        token_count = data["usage"]
        ai_request_time = data["created"]
        self._state = song_info

        self._attributes = {
            "info": song_data,
            "tokens": token_count,
            "fetched": ai_request_time,
            "request": payload,
        }
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
    _LOGGER = logging.getLogger(__name__)

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
        # Connect to the OpenAI API and get song desc and request image

        song_title = call.data.get("song_title", DEFAULT_SONG_TITLE)
        song_artist = call.data.get("song_artist", DEFAULT_SONG_ARTIST)
        song_info = f"{song_title} by {song_artist}"
        image_type = call.data.get("image_type", DEFAULT_IMAGE_TYPE)

        img_prompt = {key.lower(): value for key, value in IMAGE_TYPES.items()}
        img_match_prompt = img_prompt.get(image_type.lower())

        if img_match_prompt is not None:
            image_prompt = img_match_prompt
        else:
            image_prompt = DEFAULT_IMAGE_TYPE

        ai_prompt = f"describe in a concise way a {image_prompt} image that describes the themes and lyrics of the song"

        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "max_tokens": 100,
            "model": DEFAULT_CHAT_MODEL,
            "temperature": DEFAULT_TEMPERATURE,
            "messages": [
                {"role": "user", "content": f"{ai_prompt} {song_info}"},
            ],
        }

        async with aiohttp.ClientSession() as session:
            response = await session.post(
                API_URL,
                headers=headers,
                json=payload,
            )
            data = await response.json()
            song_data = data["choices"][0]["message"]["content"].strip()

            payload_img = {"prompt": song_data, "size": DEFAULT_IMAGE_RESOLUTION}

            response2 = await session.post(
                IMAGE_API_URL,
                headers=headers,
                json=payload_img,
            )
            data_img = await response2.json()

            self._LOGGER.debug(data)

        image_data = data_img["data"][0]["url"]
        ai_request_time = data_img["created"]
        self._state = f"{song_info} - {ai_request_time} - {image_type}"

        self._attributes = {
            "song": song_info,
            "type": image_type,
            "image": image_data,
            "fetched": ai_request_time,
            "desc": song_data,
        }
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
