# Importation des modules nécessaires
from django.db import models

# Choix disponibles pour le champ 'theme'
THEME_CHOICES = (
    ('colours', 'Colours'),
    ('town', 'Town'),
    ('kitchen', 'Kitchen'),
    ('pencase', 'Pencase'),
    ('fruits', 'Fruits'),
    ('objects', 'Objects'),
    ('pets', 'Pets'),
    ('school', 'School'),
    ('summer', 'Summer'),
)

# Choix disponibles pour le champ 'category'
CATEGORY_CHOICES = (
    ('noun', 'Noun'),  
    ('verb', 'Verb'),  
)

# Définition du modèle Word
class Word(models.Model):
    word = models.CharField(max_length=100)  # Champ pour le mot
    definition = models.TextField()  # Champ pour la définition
    example = models.TextField()  # Champ pour l'exemple
    image_url = models.URLField()  # Champ pour l'URL de l'image
    
    theme = models.CharField(max_length=100, choices=THEME_CHOICES, default='colours')  # Champ pour le thème avec des choix prédéfinis
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='noun')  # Champ pour la catégorie avec des choix prédéfinis

    def __str__(self):
        return f"{self.word} ({self.category}, {self.theme})"
