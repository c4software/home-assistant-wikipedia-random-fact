# Wikipedia Random Fact Of The Day

## 🇫🇷 Français

Cette intégration permet d'afficher un fait historique aléatoire chaque jour, en fonction de la date actuelle, en utilisant l'API [Wikipedia en français](https://fr.wikipedia.org/).

L'intégration récupère un événement historique qui s'est produit ce jour-là et l'affiche dans Home Assistant. Elle fournit également un lien vers l'article Wikipédia correspondant.

### Fonctionnalités

- Affiche un fait historique aléatoire pour la date actuelle.
- Donne un résumé de l'événement historique dans l'état de l'entité.
- Fournit un lien vers l'article complet sur Wikipédia dans les attributs de l'entité.
- Mise à jour quotidienne, avec une nouvelle valeur à chaque jour.

### Installation

#### Prérequis

Avant de commencer, vous devez avoir Home Assistant installé et fonctionnel.

#### Ajouter l'intégration

1. Téléchargez ou clonez ce repository dans le répertoire `custom_components/wikipedia-rfotd` de votre installation Home Assistant.
2. Redémarrez Home Assistant.
3. Dans l'interface web de Home Assistant, allez dans **Paramètres > Intégrations** et cliquez sur **Ajouter une intégration**.
4. Recherchez **Wikipedia Random Fact** et suivez les instructions à l'écran pour terminer l'ajout.

### Configuration

Aucune configuration manuelle n'est nécessaire. Une fois l'intégration ajoutée, un nouveau capteur sera disponible pour afficher le fait historique aléatoire du jour.

#### Exemple de configuration dans Home Assistant

Une fois l'intégration installée, un capteur `sensor.wikipedia_fact` sera créé. Vous pouvez l'utiliser dans vos automatisations ou afficher le fait du jour dans votre tableau de bord.

### Dépannage

- Si vous ne voyez pas de fait historique, vérifiez les journaux de Home Assistant pour des erreurs dans la récupération des données depuis Wikipedia.
- Assurez-vous que votre instance Home Assistant est connectée à Internet pour accéder à l'API Wikipedia.

---

## 🇬🇧 English

This integration displays a random historical fact for the current day, using the [Wikipedia API in French](https://fr.wikipedia.org/).

It retrieves a historical event that happened on this day and shows it in Home Assistant, along with a link to the corresponding Wikipedia article.

### Features

- Displays a random historical fact for the current day.
- Provides a summary of the historical event in the entity's state.
- Provides a link to the full article on Wikipedia in the entity's attributes.
- Updates daily, with a new value each day.

### Installation

#### Prerequisites

Before you begin, you need to have Home Assistant installed and running.

#### Add the integration

1. Download or clone this repository into the `custom_components/wikipedia-rfotd` directory of your Home Assistant installation.
2. Restart Home Assistant.
3. In the Home Assistant web interface, go to **Settings > Integrations** and click on **Add Integration**.
4. Search for **Wikipedia Random Fact** and follow the on-screen instructions to complete the setup.

### Configuration

No manual configuration is needed. Once the integration is added, a new sensor will be available to display the random historical fact of the day.

#### Example in Home Assistant

Once the integration is installed, a `sensor.wikipedia_fact` will be created. You can use it in your automations or display the fact of the day on your dashboard.

### Troubleshooting

- If you do not see a historical fact, check the Home Assistant logs for errors retrieving the data from Wikipedia.
- Make sure your Home Assistant instance is connected to the internet to access the Wikipedia API.
