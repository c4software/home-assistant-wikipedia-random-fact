from homeassistant import config_entries
from . import DOMAIN

class WikipediaFactConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gestionnaire de flux de configuration pour Wikipedia Fact."""

    async def async_step_user(self, user_input=None):
        """Premier écran du flux de configuration."""
        if user_input is not None:
            return self.async_create_entry(title="Wikipedia Random Fact", data={})

        return self.async_show_form(step_id="user")

