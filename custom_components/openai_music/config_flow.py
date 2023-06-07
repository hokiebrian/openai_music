""" Config Flow for OpenAI Music Companion """
import openai
import voluptuous as vol
from openai import error
from homeassistant import config_entries
from homeassistant.helpers import config_validation as cv
from .const import (
    DOMAIN,
    DEFAULT_TEMPERATURE,
    DEFAULT_CHAT_MODEL,
    DEFAULT_MAX_TOKENS,
    DEFAULT_IMAGE_RESOLUTION,
    DEFAULT_IMG_TEMPERATURE,
    DEFAULT_IMG_COUNT,
    DEFAULT_USER_TAG,
)


class OpenAIMusicFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Flow Handler"""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """Get API Key"""
        errors = {}

        if user_input is not None:
            # Validate the user input against the expected schema
            try:
                self.schema(user_input)
            except vol.Invalid as err:
                errors[err.path[0]] = str(err)

            # Test the OpenAI API with the user's API key
            api_key = user_input.get("api_key")
            success = await self.test_openai_api_key(api_key)

            if not success:
                errors["base"] = (
                    "Failed to connect to OpenAI API with the provided API key. "
                    "Do you have a pay-as-you-go account?"
                )
            if not errors:
                # The user input is valid and the API test passed, create a new config entry
                await self.async_set_unique_id(user_input["api_key"][:6])
                self._abort_if_unique_id_configured()
                return self.async_create_entry(
                    title="OpenAI Music Companion",
                    data={
                        "api_key": user_input["api_key"],
                    },
                )

        return self.async_show_form(
            step_id="user",
            data_schema=self.schema,
            errors=errors,
        )

    async def test_openai_api_key(self, api_key):
        """Test the connection to the OpenAI API using the provided API key."""
        openai.api_key = api_key

        try:
            await openai.Engine.alist()
            return True
        except error.OpenAIError:
            return False

    @property
    def schema(self):
        """Schema Definition"""
        return vol.Schema(
            {
                vol.Required("api_key"): cv.string,
            }
        )

    @staticmethod
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return OpenAIMusicOptionsFlow(config_entry)


class OpenAIMusicOptionsFlow(config_entries.OptionsFlow):
    """Spotify Sensor config flow."""

    def __init__(self, config_entry: config_entries.ConfigEntry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Handle a flow initialized by the user."""

        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        temperature = self.config_entry.options.get("temperature", DEFAULT_TEMPERATURE)
        img_temperature = self.config_entry.options.get(
            "img_temperature", DEFAULT_IMG_TEMPERATURE
        )
        max_tokens = self.config_entry.options.get("max_tokens", DEFAULT_MAX_TOKENS)
        chat_model = self.config_entry.options.get("chat_model", DEFAULT_CHAT_MODEL)
        img_resolution = self.config_entry.options.get(
            "img_resolution", DEFAULT_IMAGE_RESOLUTION
        )
        user_tag = self.config_entry.options.get("user_tag", DEFAULT_USER_TAG)
        img_count = self.config_entry.options.get("img_count", DEFAULT_IMG_COUNT)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Optional("temperature", default=temperature): vol.All(
                        vol.Coerce(float), vol.Range(min=0.0, max=2.0)
                    ),
                    vol.Optional("img_temperature", default=img_temperature): vol.All(
                        vol.Coerce(float), vol.Range(min=0.0, max=2.0)
                    ),
                    vol.Optional("max_tokens", default=max_tokens): vol.All(
                        vol.Coerce(int), vol.Range(min=100, max=1000)
                    ),
                    vol.Optional("chat_model", default=chat_model): vol.In(
                        ["gpt-3.5-turbo", "gpt-4"]
                    ),
                    vol.Optional("img_resolution", default=img_resolution): vol.In(
                        ["1024x1024", "512x512", "256x256"]
                    ),
                    vol.Optional("user_tag", default=user_tag): str,
                    vol.Optional("img_count", default=img_count): vol.All(
                        vol.Coerce(int), vol.Range(min=1, max=10)
                    ),
                }
            ),
        )
