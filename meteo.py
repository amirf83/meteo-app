#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script météorologique Python
Demande le nom d'une ville et affiche les détails météorologiques
"""

import requests
import json
import sys
from typing import Dict, Optional


class MeteoApp:
    """Application météorologique pour obtenir les données d'une ville"""
    
    def __init__(self):
        # API Key gratuite OpenWeatherMap (demo key)
        # En production, cette clé devrait être dans une variable d'environnement
        self.api_key = "demo_key"  # À remplacer par une vraie clé API
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def obtenir_meteo(self, ville: str) -> Optional[Dict]:
        """
        Obtient les données météorologiques pour une ville donnée
        
        Args:
            ville (str): Nom de la ville
            
        Returns:
            Dict: Données météorologiques ou None en cas d'erreur
        """
        try:
            # Paramètres de la requête API
            params = {
                'q': ville,
                'appid': self.api_key,
                'units': 'metric',  # Température en Celsius
                'lang': 'fr'  # Descriptions en français
            }
            
            # Simulation des données pour le mode démo
            # En production, utiliser la vraie API
            if self.api_key == "demo_key":
                return self._obtenir_donnees_demo(ville)
            
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête API: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Erreur lors du décodage JSON: {e}")
            return None
    
    def _obtenir_donnees_demo(self, ville: str) -> Dict:
        """
        Fournit des données météorologiques de démonstration
        """
        # Données simulées pour différentes villes
        donnees_demo = {
            'paris': {
                'name': 'Paris',
                'main': {
                    'temp': 18.5,
                    'humidity': 65,
                    'pressure': 1013
                },
                'weather': [
                    {
                        'main': 'Clouds',
                        'description': 'nuageux'
                    }
                ],
                'wind': {
                    'speed': 3.2,
                    'deg': 230
                }
            },
            'lyon': {
                'name': 'Lyon',
                'main': {
                    'temp': 22.1,
                    'humidity': 58,
                    'pressure': 1018
                },
                'weather': [
                    {
                        'main': 'Clear',
                        'description': 'ciel dégagé'
                    }
                ],
                'wind': {
                    'speed': 2.1,
                    'deg': 180
                }
            },
            'marseille': {
                'name': 'Marseille',
                'main': {
                    'temp': 25.3,
                    'humidity': 52,
                    'pressure': 1020
                },
                'weather': [
                    {
                        'main': 'Rain',
                        'description': 'pluie légère'
                    }
                ],
                'wind': {
                    'speed': 4.8,
                    'deg': 150
                }
            }
        }
        
        ville_lower = ville.lower().strip()
        if ville_lower in donnees_demo:
            return donnees_demo[ville_lower]
        else:
            # Données par défaut pour les villes non reconnues
            return {
                'name': ville.title(),
                'main': {
                    'temp': 20.0,
                    'humidity': 60,
                    'pressure': 1015
                },
                'weather': [
                    {
                        'main': 'Clear',
                        'description': 'temps variable'
                    }
                ],
                'wind': {
                    'speed': 3.0,
                    'deg': 200
                }
            }
    
    def interpreter_conditions(self, weather_main: str) -> str:
        """
        Interprète les conditions météorologiques
        
        Args:
            weather_main (str): Condition météo principale
            
        Returns:
            str: Description en français
        """
        conditions = {
            'Clear': '☀️ Il fait beau',
            'Clouds': '☁️ Il y a des nuages',
            'Rain': '🌧️ Il pleut',
            'Drizzle': '🌦️ Il bruine',
            'Thunderstorm': '⛈️ Il y a de l\'orage',
            'Snow': '❄️ Il neige',
            'Mist': '🌫️ Il y a de la brume',
            'Fog': '🌫️ Il y a du brouillard'
        }
        
        return conditions.get(weather_main, f'Conditions: {weather_main}')
    
    def interpreter_vent(self, vitesse: float) -> str:
        """
        Interprète la vitesse du vent
        
        Args:
            vitesse (float): Vitesse du vent en m/s
            
        Returns:
            str: Description du vent
        """
        if vitesse < 1:
            return "💨 Vent très faible"
        elif vitesse < 3:
            return "💨 Vent faible"
        elif vitesse < 7:
            return "💨 Vent modéré"
        elif vitesse < 12:
            return "💨 Vent fort"
        else:
            return "💨 Vent très fort"
    
    def afficher_meteo(self, donnees: Dict) -> None:
        """
        Affiche les données météorologiques de manière formatée
        
        Args:
            donnees (Dict): Données météorologiques de l'API
        """
        print(f"\n🌍 Météo pour {donnees['name']}")
        print("=" * 40)
        
        # Température
        temp = donnees['main']['temp']
        print(f"🌡️  Température: {temp:.1f}°C")
        
        # Humidité
        humidity = donnees['main']['humidity']
        print(f"💧 Humidité: {humidity}%")
        
        # Vent
        wind_speed = donnees['wind']['speed']
        print(f"💨 Vent: {wind_speed:.1f} m/s")
        print(f"   {self.interpreter_vent(wind_speed)}")
        
        # Conditions météorologiques
        weather = donnees['weather'][0]
        print(f"\n{self.interpreter_conditions(weather['main'])}")
        print(f"   Description: {weather['description']}")
        
        # Pression (information bonus)
        if 'pressure' in donnees['main']:
            print(f"📊 Pression: {donnees['main']['pressure']} hPa")
    
    def executer(self) -> None:
        """
        Exécute l'application météorologique
        """
        print("🌤️  Application Météo")
        print("Tapez 'quit' ou 'q' pour quitter\n")
        
        while True:
            try:
                # Demander le nom de la ville
                ville = input("Entrez le nom d'une ville: ").strip()
                
                # Vérifier si l'utilisateur veut quitter
                if ville.lower() in ['quit', 'q', 'quitter']:
                    print("Au revoir! 👋")
                    break
                
                # Vérifier que l'entrée n'est pas vide
                if not ville:
                    print("❌ Veuillez entrer un nom de ville valide.")
                    continue
                
                # Obtenir et afficher les données météo
                donnees = self.obtenir_meteo(ville)
                if donnees:
                    self.afficher_meteo(donnees)
                else:
                    print(f"❌ Impossible d'obtenir les données météo pour '{ville}'")
                
                print("\n" + "-" * 40)
                
            except KeyboardInterrupt:
                print("\n\nAu revoir! 👋")
                break
            except EOFError:
                print("\nAu revoir! 👋")
                break
            except Exception as e:
                print(f"❌ Une erreur s'est produite: {e}")
                break


def main():
    """Fonction principale"""
    app = MeteoApp()
    app.executer()


if __name__ == "__main__":
    main()