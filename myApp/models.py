from django.db import models

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

CATEGORY_CHOICES = (
    ('noun', 'Noun'),  
    ('verb', 'Verb'),  
)
class Word(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField()
    example = models.TextField()
    image_url = models.URLField()
    
    theme = models.CharField(max_length=100, choices=THEME_CHOICES, default='colours')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='noun')

    def __str__(self):
        return f"{self.word} ({self.category}, {self.theme})"




