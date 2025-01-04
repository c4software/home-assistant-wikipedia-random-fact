# Wikipedia Random Fact Of The Day

## 🇫🇷 Français

Cette intégration permet d'afficher un fait historique aléatoire chaque jour, en fonction de la date actuelle, en utilisant l'API Wikipedia. L'intégration supporte plusieurs langues (Français, English, Español, Deutsch) et récupère un événement historique qui s'est produit ce jour-là pour l'afficher dans Home Assistant.

### Fonctionnalités

- Affiche un fait historique aléatoire pour la date actuelle.
- Support multilingue (fr, en, es, de).
- Donne un résumé de l'événement historique dans l'état de l'entité.
- Fournit un lien vers l'article complet sur Wikipédia dans les attributs de l'entité.
- Mise à jour quotidienne, avec une nouvelle valeur à chaque jour.

### Installation

#### Prérequis

Avant de commencer, vous devez avoir Home Assistant installé et fonctionnel.

#### Ajouter l'intégration via HACS

1. Assurez-vous que [HACS](https://hacs.xyz/) est installé sur votre instance Home Assistant.
2. Dans l'interface web de Home Assistant, allez dans **HACS > Intégrations**.
3. Cliquez sur le bouton **...** dans le coin supérieur droit, puis sur **Ajouter un dépôt personnalisé**.
4. Entrez l'URL du dépôt :  
   `https://github.com/c4software/home-assistant-wikipedia-random-fact`
5. Sélectionnez la catégorie **Intégration** et cliquez sur **Ajouter**.
6. Recherchez **Wikipedia Random Fact** dans les intégrations HACS, installez-la, puis redémarrez Home Assistant.

#### Ajouter l'intégration manuellement

1. Téléchargez ou clonez ce repository dans le répertoire `custom_components/wikipedia-rfotd` de votre installation Home Assistant.
2. Redémarrez Home Assistant.
3. Dans l'interface web de Home Assistant, allez dans **Paramètres > Intégrations** et cliquez sur **Ajouter une intégration**.
4. Recherchez **Wikipedia Random Fact** et suivez les instructions à l'écran pour terminer l'ajout.
5. Sélectionnez la langue souhaitée dans le menu déroulant (Français par défaut).

### Configuration

La configuration se fait entièrement via l'interface utilisateur. Lors de l'ajout de l'intégration, vous pourrez choisir :
- La langue de Wikipedia à utiliser parmi :
  - Français (fr)
  - English (en)
  - Español (es)
  - Deutsch (de)

### Entité exposée

L'intégration crée une entité `sensor.wikipedia_fact` avec les caractéristiques suivantes :

#### État
L'état de l'entité contient un résumé court (100 caractères) de l'événement au format :  
```
En {année}: {description}...
```

#### Attributs
L'entité expose les attributs suivants :
- `texte_complet` : Le texte complet de l'événement historique.
- `lien` : L'URL vers l'article Wikipedia correspondant (si disponible).
- `année` : L'année de l'événement historique.

### Dépannage

- Si vous ne voyez pas de fait historique, vérifiez les journaux de Home Assistant pour des erreurs dans la récupération des données depuis Wikipedia.
- Assurez-vous que votre instance Home Assistant est connectée à Internet pour accéder à l'API Wikipedia.

---

## 🇬🇧 English

This integration displays a random historical fact for the current day, using the Wikipedia API. The integration supports multiple languages (French, English, Spanish, German) and retrieves a historical event that happened on this day to display it in Home Assistant.

### Features

- Displays a random historical fact for the current day.
- Multilingual support (fr, en, es, de).
- Provides a summary of the historical event in the entity's state.
- Provides a link to the full article on Wikipedia in the entity's attributes.
- Updates daily, with a new value each day.

### Installation

#### Prerequisites

Before you begin, you need to have Home Assistant installed and running.

#### Add the integration via HACS

1. Ensure [HACS](https://hacs.xyz/) is installed on your Home Assistant instance.
2. In the Home Assistant web interface, go to **HACS > Integrations**.
3. Click the **...** button in the top-right corner and select **Add custom repository**.
4. Enter the repository URL:  
   `https://github.com/c4software/home-assistant-wikipedia-random-fact`
5. Select the **Integration** category and click **Add**.
6. Search for **Wikipedia Random Fact** in the HACS integrations, install it, and restart Home Assistant.

#### Add the integration manually

1. Download or clone this repository into the `custom_components/wikipedia-rfotd` directory of your Home Assistant installation.
2. Restart Home Assistant.
3. In the Home Assistant web interface, go to **Settings > Integrations** and click on **Add Integration**.
4. Search for **Wikipedia Random Fact** and follow the on-screen instructions to complete the setup.
5. Select your desired language from the dropdown menu (French by default).

### Configuration

The configuration is done entirely through the user interface. When adding the integration, you can choose:
- The Wikipedia language to use from:
  - French (fr)
  - English (en)
  - Spanish (es)
  - German (de)

### Exposed Entity

The integration creates a `sensor.wikipedia_fact` entity with the following characteristics:

#### State
The entity's state contains a short summary (100 characters) of the event in the format:  
```
In {year}: {description}...
```

#### Attributes
The entity exposes the following attributes:
- `texte_complet`: The full text of the historical event.
- `lien`: The URL to the corresponding Wikipedia article (if available).
- `année`: The year of the historical event.

### Troubleshooting

- If you do not see a historical fact, check the Home Assistant logs for errors retrieving data from Wikipedia.
- Make sure your Home Assistant instance is connected to the internet to access the Wikipedia API.
