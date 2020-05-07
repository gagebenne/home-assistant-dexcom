"""Config flow for Dexcom integration."""
import logging

from pydexcom import AccountError, Dexcom, SessionError
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME

from .const import DOMAIN  # pylint:disable=unused-import

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema(
    {vol.Required(CONF_USERNAME): str, vol.Required(CONF_PASSWORD): str}
)


class DexcomConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Dexcom."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            try:
                await self.hass.async_add_executor_job(
                    Dexcom, user_input[CONF_USERNAME], user_input[CONF_PASSWORD]
                )

                await self.async_set_unique_id(user_input[CONF_USERNAME])
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=user_input[CONF_USERNAME], data=user_input
                )
            except SessionError:
                errors["base"] = "session_error"
            except AccountError:
                errors["base"] = "account_error"
            except Exception:  # pylint: disable=broad-except
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )

    async def async_step_import(self, user_input):
        """Handle import."""
        await self.async_set_unique_id(user_input[CONF_USERNAME])
        self._abort_if_unique_id_configured()

        return await self.async_step_user(user_input)
