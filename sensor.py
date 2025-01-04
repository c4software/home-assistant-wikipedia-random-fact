import aiohttp
import random
from datetime import date
from homeassistant.helpers.entity import Entity

DOMAIN = "wikipedia_fact"

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Configurer le capteur via une entrée de configuration."""
    sensor = WikipediaFactSensor("Wikipedia Fact")
    async_add_entities([sensor], update_before_add=True)  # Force la mise à jour avant l'ajout


class WikipediaFactSensor(Entity):
    """Capteur pour récupérer un fait aléatoire lié au jour courant depuis Wikipedia."""

    def __init__(self, name):
        """Initialise le capteur."""
        self._name = name
        self._state = None
        self._attributes = {}
        self._last_update = None  # Stocke la date de la dernière mise à jour

    @property
    def name(self):
        """Nom de l'entité."""
        return self._name

    @property
    def state(self):
        """État actuel de l'entité."""
        # Limite l'état à 255 caractères maximum
        return self._state[:255] if self._state else None

    @property
    def extra_state_attributes(self):
        """Attributs supplémentaires."""
        return self._attributes

    async def async_update(self):
        """Met à jour l'état avec un fait aléatoire si nécessaire."""
        today = date.today()

        # Ne mettre à jour que si la date a changé
        if self._last_update == today:
            return

        self._last_update = today
        month = today.strftime("%m")
        day = today.strftime("%d")
        url = f"https://fr.wikipedia.org/api/rest_v1/feed/onthisday/events/{month}/{day}"

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
            self._state = f"Erreur : {str(e)[:100]}"  # Limite les messages d'erreur

