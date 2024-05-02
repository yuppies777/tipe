import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Données des villes avec leurs coordonnées et leurs températures
donnees = [
    {'ville': 'Paris', 'latitude': 48.8566, 'longitude': 2.3522, 'temperature': 4.7},
    {'ville': 'Marseille', 'latitude': 43.2965, 'longitude': 5.3698, 'temperature': 8.8},
    {'ville': 'Lyon', 'latitude': 45.7640, 'longitude': 4.8357, 'temperature': 4.4},
    {'ville': 'Toulouse', 'latitude': 43.6047, 'longitude': 1.4442, 'temperature': 5.7},
    {'ville': 'Nantes', 'latitude': 47.2184, 'longitude': -1.5536, 'temperature': 4.4},
    {'ville': 'Strasbourg', 'latitude': 48.5734, 'longitude': 7.7521, 'temperature': 2.2},
    {'ville': 'Montpellier', 'latitude': 43.6109, 'longitude': 3.8772, 'temperature': 10.9},
    {'ville': 'Bordeaux', 'latitude': 44.8378, 'longitude': -0.5792, 'temperature': 4.8},
    {'ville': 'Lille', 'latitude': 50.6292, 'longitude': 3.0573, 'temperature': 4.0},
    {'ville': 'Rennes', 'latitude': 48.1173, 'longitude': -1.6778, 'temperature': 3.4},
    {'ville': 'Reims', 'latitude': 49.2583, 'longitude': 4.0317, 'temperature': 3},
    {'ville': 'Le Havre', 'latitude': 49.4944, 'longitude': 0.1070, 'temperature': 4.4},
    {'ville': 'Saint-Étienne', 'latitude': 45.4397, 'longitude': 4.3872, 'temperature': 2.1},
    {'ville': 'Toulon', 'latitude': 43.1242, 'longitude': 5.9280, 'temperature': 11.5},
    {'ville': 'Le Mans', 'latitude': 48.0061, 'longitude': 0.1996, 'temperature': 3.9},
    {'ville': 'Aix-en-Provence', 'latitude': 43.5297, 'longitude': 5.4474, 'temperature': 7.7},
    {'ville': 'Amiens', 'latitude': 49.8942, 'longitude': 2.2957, 'temperature': 4},
    {'ville': 'Limoges', 'latitude': 45.8336, 'longitude': 1.2611, 'temperature': 2.8},
    {'ville': 'Annecy', 'latitude': 45.8992, 'longitude': 6.1294, 'temperature': 5.7},
    {'ville': 'Perpignan', 'latitude': 42.6886, 'longitude': 2.8947, 'temperature': 9.1},
    {'ville': 'Bayonne', 'latitude': 43.4933, 'longitude': -1.4751, 'temperature': 7},
    {'ville': 'Nice', 'latitude': 43.7102, 'longitude': 7.2620, 'temperature': 6.7},
    {'ville': 'Brest', 'latitude': 48.3904, 'longitude': -4.4861, 'temperature': 4.1},
    {'ville': 'Saint-Malo', 'latitude': 48.6493, 'longitude': -2.0257, 'temperature': 2.7},
    {'ville': 'Calais', 'latitude': 50.9513, 'longitude': 1.8587, 'temperature': 4.7}
]


# Récupérer les coordonnées et les températures des villes
latitudes = [ville['latitude'] for ville in donnees]
longitudes = [ville['longitude'] for ville in donnees]
temperatures = [ville['temperature'] for ville in donnees]

# Créer une grille de coordonnées pour la France
latitudes_grille = np.linspace(min(latitudes), max(latitudes), 100)
longitudes_grille = np.linspace(min(longitudes), max(longitudes), 100)
latitude_grille, longitude_grille = np.meshgrid(latitudes_grille, longitudes_grille)

temperature_grille = griddata((latitudes, longitudes), temperatures, (latitude_grille, longitude_grille), method='cubic')

plt.imshow(temperature_grille.T, cmap='coolwarm', extent=(min(longitudes), max(longitudes), min(latitudes), max(latitudes)), origin='lower')
plt.colorbar(label='Température (°C)')
plt.title("Matrice de températures en France le 1er mars 2024")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
