"""Initialisation de l'intégration Wikipedia Fact."""
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

DOMAIN = "wikipedia_fact"

async def async_setup(hass: HomeAssistant, config: dict):
    """Configurer l'intégration Wikipedia Fact via YAML (si nécessaire)."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Configurer une entrée créée depuis l'interface utilisateur."""
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Décharger une entrée."""
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    return True

