# Application Météo 🌤️

Script Python qui demande en entrée le nom d'une ville et qui ressort les détails météorologiques tels que la température, l'humidité, le vent, et les conditions météorologiques (s'il fait beau, s'il pleut, s'il vente).

## Fonctionnalités ✨

- **Entrée interactive** : Demande le nom d'une ville à l'utilisateur
- **Données météorologiques complètes** :
  - 🌡️ Température en degrés Celsius
  - 💧 Humidité en pourcentage
  - 💨 Vitesse du vent en m/s avec interprétation
  - 🌤️ Conditions météorologiques (beau temps, pluie, nuages, etc.)
  - 📊 Pression atmosphérique
- **Interface en français** avec emojis pour une meilleure lisibilité
- **Mode démo** avec données simulées pour plusieurs villes françaises
- **Gestion d'erreurs** robuste

## Installation 🔧

1. Clonez le repository :
```bash
git clone <repository-url>
cd meteo-app
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation 🚀

### Mode interactif
Lancez l'application et suivez les instructions :
```bash
python3 meteo.py
```

Exemple d'utilisation :
```
🌤️  Application Météo
Tapez 'quit' ou 'q' pour quitter

Entrez le nom d'une ville: Paris

🌍 Météo pour Paris
========================================
🌡️  Température: 18.5°C
💧 Humidité: 65%
💨 Vent: 3.2 m/s
   💨 Vent modéré

☁️ Il y a des nuages
   Description: nuageux
📊 Pression: 1013 hPa
```

### Tests
Pour tester l'application avec plusieurs villes :
```bash
python3 test_meteo.py
```

## Villes de démonstration 🏙️

Le mode démo inclut des données météorologiques simulées pour :
- **Paris** - Temps nuageux
- **Lyon** - Ciel dégagé
- **Marseille** - Pluie légère
- **Autres villes** - Données par défaut

## Configuration API 🔑

Actuellement, l'application fonctionne en mode démo avec des données simulées. 

Pour utiliser de vraies données météorologiques :
1. Créez un compte gratuit sur [OpenWeatherMap](https://openweathermap.org/api)
2. Obtenez votre clé API
3. Remplacez `demo_key` dans `meteo.py` par votre vraie clé
4. Ou mieux, utilisez une variable d'environnement :
```bash
export OPENWEATHER_API_KEY="votre_cle_ici"
```

## Structure du projet 📁

```
meteo-app/
├── meteo.py           # Script principal
├── test_meteo.py      # Tests automatisés
├── requirements.txt   # Dépendances Python
├── config.txt         # Instructions de configuration
└── README.md          # Documentation
```

## Fonctionnalités techniques 🔧

- **Gestion d'erreurs** : EOF, KeyboardInterrupt, erreurs réseau
- **Interface utilisateur** : Emojis et couleurs pour une meilleure UX
- **Architecture modulaire** : Classe MeteoApp avec méthodes spécialisées
- **Interprétation intelligente** : Conversion des données brutes en descriptions françaises
- **Mode démo** : Fonctionne sans API key pour les tests

## Commandes disponibles 💬

- Tapez le nom d'une ville pour obtenir la météo
- `quit`, `q`, ou `quitter` pour sortir de l'application
- `Ctrl+C` pour sortir à tout moment

## Auteur 👨‍💻

Script Python basique utilisant une API afin d'obtenir les détails météorologiques d'une ville.
