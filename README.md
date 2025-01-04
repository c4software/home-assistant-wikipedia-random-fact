# Wikipedia Random Fact

Cette intégration permet d'afficher un fait historique aléatoire chaque jour, en fonction de la date actuelle, en utilisant l'API [Wikipedia en français](https://fr.wikipedia.org/).

L'intégration récupère un événement historique qui s'est produit ce jour-là et l'affiche dans Home Assistant. Elle fournit également un lien vers l'article Wikipédia correspondant.

## Fonctionnalités

- Affiche un fait historique aléatoire pour la date actuelle.
- Donne un résumé de l'événement historique dans l'état de l'entité.
- Fournit un lien vers l'article complet sur Wikipédia dans les attributs de l'entité.
- Mise à jour quotidienne, avec une nouvelle valeur à chaque jour.

## Installation

### Prérequis

Avant de commencer, vous devez avoir Home Assistant installé et fonctionnel.

### Ajouter l'intégration

1. Téléchargez ou clonez ce repository dans le répertoire `custom_components` de votre installation Home Assistant.
2. Redémarrez Home Assistant.
3. Dans l'interface web de Home Assistant, allez dans **Paramètres > Intégrations** et cliquez sur **Ajouter une intégration**.
4. Recherchez **Wikipedia Random Fact** et suivez les instructions à l'écran pour terminer l'ajout.

## Configuration

Aucune configuration manuelle n'est nécessaire. Une fois l'intégration ajoutée, un nouveau capteur sera disponible pour afficher le fait historique aléatoire du jour.

### Exemple de configuration dans Home Assistant

Une fois l'intégration installée, un capteur `sensor.wikipedia_fact` sera créé. Vous pouvez l'utiliser dans vos automatisations ou afficher le fait du jour dans votre tableau de bord.


## Dépannage

- Si vous ne voyez pas de fait historique, vérifiez les journaux de Home Assistant pour des erreurs dans la récupération des données depuis Wikipedia.
- Assurez-vous que votre instance Home Assistant est connectée à Internet pour accéder à l'API Wikipedia.
