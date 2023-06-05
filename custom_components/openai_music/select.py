"""
    Select Entities for OpenAI Music Companion
    Retrieves items from const.py to build
    dropdown select entities
"""
from homeassistant.components.select import SelectEntity
from .const import IMAGE_TYPES, PROMPTS, PERSONALITIES


async def async_setup_entry(hass, config, async_add_entities):
    """Create and add the select entities"""
    async_add_entities(
        [
            InfoSelectEntity(),
            InfoSelectEntitySecondary(),
            PersonalitySelectEntity(),
            PersonalitySelectEntitySecondary(),
            ImageSelectEntity(),
        ]
    )


class InfoSelectEntity(SelectEntity):
    """Select Info type to request."""

    _attr_icon = "mdi:chat-question"
    _attr_unique_id = "OAIInfoSelect"

    def __init__(self):
        self._state = "General Song Info"
        self._attr_options = sorted([key for key, value in PROMPTS.items()])

    @property
    def name(self):
        return "OpenAI Music Info Profile"

    @property
    def state(self):
        return self._state

    @property
    def current_option(self):
        return None

    async def async_select_option(self, option):
        if option in self._attr_options:
            self._state = option
            self.async_write_ha_state()


class InfoSelectEntitySecondary(SelectEntity):
    """Select Info type to request."""

    _attr_icon = "mdi:chat-question"
    _attr_unique_id = "OAIInfoSelectSecondary"

    def __init__(self):
        self._state = "General Song Info"
        self._attr_options = sorted([key for key, value in PROMPTS.items()])

    @property
    def name(self):
        return "OpenAI Music Info Profile (Secondary)"

    @property
    def state(self):
        return self._state

    @property
    def current_option(self):
        return None

    async def async_select_option(self, option):
        if option in self._attr_options:
            self._state = option
            self.async_write_ha_state()


class PersonalitySelectEntity(SelectEntity):
    """Select OpenAI Personality."""

    _attr_icon = "mdi:tooltip-account"
    _attr_unique_id = "OAIPersonality"

    def __init__(self):
        self._state = "Normal"
        self._attr_options = sorted([key for key, value in PERSONALITIES.items()])

    @property
    def name(self):
        return "OpenAI Music Personality Profile"

    @property
    def state(self):
        return self._state

    @property
    def current_option(self):
        return None

    async def async_select_option(self, option):
        if option in self._attr_options:
            self._state = option
            self.async_write_ha_state()

class PersonalitySelectEntitySecondary(SelectEntity):
    """Select OpenAI Personality."""

    _attr_icon = "mdi:tooltip-account"
    _attr_unique_id = "OAIPersonalitySecondary"

    def __init__(self):
        self._state = "Normal"
        self._attr_options = sorted([key for key, value in PERSONALITIES.items()])

    @property
    def name(self):
        return "OpenAI Music Personality Profile (Secondary)"

    @property
    def state(self):
        return self._state

    @property
    def current_option(self):
        return None

    async def async_select_option(self, option):
        if option in self._attr_options:
            self._state = option
            self.async_write_ha_state()

class ImageSelectEntity(SelectEntity):
    """Select Image Creation Profile."""

    _attr_icon = "mdi:palette"
    _attr_unique_id = "OAIImageSelect"

    def __init__(self):
        self._state = "Normal"
        self._attr_options = sorted([key for key, value in IMAGE_TYPES.items()])

    @property
    def name(self):
        return "OpenAI Music Image Profile"

    @property
    def state(self):
        return self._state

    @property
    def current_option(self):
        return None

    async def async_select_option(self, option):
        if option in self._attr_options:
            self._state = option
            self.async_write_ha_state()
