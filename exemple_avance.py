#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemple d'utilisation avancée de l'application météo
Démontre comment utiliser la classe MeteoApp dans d'autres scripts
"""

from meteo import MeteoApp


def exemple_utilisation_programmatique():
    """Exemple d'utilisation de l'API de façon programmatique"""
    
    app = MeteoApp()
    
    # Liste de villes à vérifier
    villes = ['Paris', 'Lyon', 'Marseille', 'Bordeaux', 'Lille']
    
    print("📊 Rapport météorologique pour plusieurs villes")
    print("=" * 60)
    
    for ville in villes:
        donnees = app.obtenir_meteo(ville)
        if donnees:
            temp = donnees['main']['temp']
            humidity = donnees['main']['humidity']
            weather = donnees['weather'][0]['description']
            
            print(f"🏙️  {ville:12} | {temp:5.1f}°C | {humidity:2d}% | {weather}")
        else:
            print(f"❌ {ville:12} | Données non disponibles")
    
    print("=" * 60)


def exemple_filtrage_conditions():
    """Exemple de filtrage par conditions météorologiques"""
    
    app = MeteoApp()
    villes = ['Paris', 'Lyon', 'Marseille', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg']
    
    print("\n🌧️  Villes où il pleut:")
    print("-" * 30)
    
    for ville in villes:
        donnees = app.obtenir_meteo(ville)
        if donnees and 'Rain' in donnees['weather'][0]['main']:
            print(f"   💧 {ville}")
    
    print("\n☀️  Villes avec beau temps:")
    print("-" * 30)
    
    for ville in villes:
        donnees = app.obtenir_meteo(ville)
        if donnees and 'Clear' in donnees['weather'][0]['main']:
            print(f"   🌞 {ville}")


if __name__ == "__main__":
    exemple_utilisation_programmatique()
    exemple_filtrage_conditions()