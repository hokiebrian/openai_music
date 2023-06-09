"""OpenAI Music Companion"""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import Platform

from homeassistant.helpers import entity_platform

from .const import DOMAIN

PLATFORMS = [Platform.SENSOR, Platform.SELECT]


async def async_setup(hass: HomeAssistant, config: dict):
    """Basic Component Setup"""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Basic platform setup"""
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    )
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload"""
    await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    return True
