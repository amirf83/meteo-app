#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test pour l'application météorologique
"""

from meteo import MeteoApp


def test_meteo_app():
    """Test de l'application météo avec différentes villes"""
    
    app = MeteoApp()
    
    # Villes à tester
    villes_test = ['Paris', 'Lyon', 'Marseille', 'Toulouse', 'Nice']
    
    print("🧪 Test de l'application météorologique")
    print("=" * 50)
    
    for ville in villes_test:
        print(f"\n🔍 Test pour la ville: {ville}")
        print("-" * 30)
        
        # Obtenir les données météo
        donnees = app.obtenir_meteo(ville)
        
        if donnees:
            app.afficher_meteo(donnees)
            print("✅ Test réussi")
        else:
            print("❌ Test échoué - pas de données")
        
        print("\n" + "=" * 50)


def test_fonctions_individuelles():
    """Test des fonctions individuelles"""
    
    print("\n🔧 Test des fonctions individuelles")
    print("=" * 50)
    
    app = MeteoApp()
    
    # Test de l'interprétation des conditions
    print("\n🌤️ Test des conditions météorologiques:")
    conditions = ['Clear', 'Clouds', 'Rain', 'Snow', 'Thunderstorm']
    for condition in conditions:
        result = app.interpreter_conditions(condition)
        print(f"  {condition} -> {result}")
    
    # Test de l'interprétation du vent
    print("\n💨 Test de l'interprétation du vent:")
    vitesses = [0.5, 2.0, 5.0, 10.0, 15.0]
    for vitesse in vitesses:
        result = app.interpreter_vent(vitesse)
        print(f"  {vitesse} m/s -> {result}")


if __name__ == "__main__":
    test_meteo_app()
    test_fonctions_individuelles()
    print("\n🎉 Tests terminés!")