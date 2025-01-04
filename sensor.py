import aiohttp
import random
from datetime import date
from homeassistant.helpers.entity import Entity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = "wikipedia_fact"

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities):
    """Configurer le capteur via une entrée de configuration."""
    # Récupère la langue depuis la configuration
    language = config_entry.data.get("language", "fr")
    sensor = WikipediaFactSensor("Wikipedia Fact", language)
    async_add_entities([sensor], update_before_add=True)

class WikipediaFactSensor(Entity):
    """Capteur pour récupérer un fait aléatoire lié au jour courant depuis Wikipedia."""

    def __init__(self, name, language):
        self._name = name
        self._state = None
        self._attributes = {}
        self._last_update = None
        self._language = language

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    @property
    def icon(self):
        return "mdi:book-open-page-variant"

    async def async_update(self):
        today = date.today()

        # Ne mettre à jour que si la date a changé
        if self._last_update == today:
            return

        self._last_update = today
        month = today.strftime("%m")
        day = today.strftime("%d")
        url = f"https://{self._language}.wikipedia.org/api/rest_v1/feed/onthisday/events/{month}/{day}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        self._state = f"Erreur HTTP {response.status}"
                        return

                    data = await response.json()
                    events = data.get("events", [])

                    if not events:
                        self._state = "Aucun événement trouvé."
                        return

                    # Choisir un événement aléatoire
                    event = random.choice(events)
                    year = event.get("year", "Année inconnue")
                    text = event.get("text", "Description indisponible")
                    pages = event.get("pages", [])
                    link = (
                        pages[0].get("content_urls", {}).get("desktop", {}).get("page", "")
                        if pages
                        else None
                    )

                    # Définir un résumé court pour l'état et des détails dans les attributs
                    self._state = f"En {year}: {text[:100]}..."  # Résumé limité à 100 caractères
                    self._attributes = {
                        "texte_complet": f"En {year}: {text}",
                        "lien": link,
                        "année": year,
                    } if link else {"texte_complet": f"En {year}: {text}", "année": year}

        except Exception as e:
            self._state = f"Erreur : {str(e)}"
