""" Config Flow for OpenAI Music Companion """
import aiohttp
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers import config_validation as cv
from .const import DOMAIN


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
            except vol.Invalid as e:
                errors[e.path[0]] = str(e)

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
                    data={"api_key": user_input["api_key"]},
                )

        return self.async_show_form(
            step_id="user",
            data_schema=self.schema,
            errors=errors,
        )

    async def test_openai_api_key(self, api_key):
        """Test the connection to the OpenAI API using the provided API key."""

        headers = {"Authorization": f"Bearer {api_key}"}

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    "https://api.openai.com/v1/engines", headers=headers
                ) as response:
                    response.raise_for_status()
                    return True
        except aiohttp.ClientError as error:
            return False

    @property
    def schema(self):
        """Schema Definition"""
        return vol.Schema({vol.Required("api_key"): cv.string})
