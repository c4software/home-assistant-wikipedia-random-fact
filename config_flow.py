from homeassistant import config_entries
import voluptuous as vol
from . import DOMAIN

class WikipediaFactConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gère la configuration de l'intégration Wikipedia Random Fact."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            # Valide et enregistre la configuration
            return self.async_create_entry(
                title="Wikipedia Random Fact",
                data={"language": user_input["language"]}
            )

        # Affiche le formulaire de configuration
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("language", default="fr"): vol.In({
                    "fr": "Français",
                    "en": "English",
                    "es": "Español",
                    "de": "Deutsch"
                })
            }),
            errors=errors
        )
