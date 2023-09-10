from django.db import models

class Fish(models.Model):
    species_code = models.CharField(max_length=10, unique=True)
    taxocode = models.PositiveIntegerField(unique=True)
    scientific_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    order = models.CharField(max_length=100, db_column='order_field')  # 'order' est un mot réservé en Python, donc nous utilisons db_column pour le renommer dans la base de données.

    def __str__(self):
        return self.english_name
