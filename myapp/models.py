from django.db import models

class Fish(models.Model):

    species_code = models.CharField(max_length=255, null=True, blank=True, unique=True)
    taxocode = models.TextField(null=True, blank=True)  # Puisque c'est 'Mixed', on utilise TextField
    scientific_name = models.CharField(max_length=100, null=True, blank=True)
    english_name = models.CharField(max_length=100, null=True, blank=True)
    french_name = models.CharField(max_length=100, null=True, blank=True)
    spanish_name = models.CharField(max_length=100, null=True, blank=True)
    arabic_name = models.CharField(max_length=100, null=True, blank=True)
    chinese_name = models.CharField(max_length=100, null=True, blank=True)
    russian_name = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    family = models.CharField(max_length=100, null=True, blank=True)
    order = models.CharField(max_length=100, db_column='order_field', null=True, blank=True)  # 'order' est un mot réservé, on le renomme donc
    stats_data = models.CharField(max_length=100, null=True, blank=True)
    isscaap_code = models.FloatField(null=True, blank=True)  # Puisque c'est un 'Double', on utilise FloatField
    isscaap_group_en = models.CharField(max_length=100, null=True, blank=True)
    isscaap_group_fr = models.CharField(max_length=100, null=True, blank=True)
    isscaap_group_es = models.CharField(max_length=100, null=True, blank=True)
    isscaap_division_code = models.FloatField(null=True, blank=True)  # Puisque c'est un 'Double', on utilise FloatField
    isscaap_division_en = models.CharField(max_length=100, null=True, blank=True)
    isscaap_division_fr = models.CharField(max_length=100, null=True, blank=True)
    isscaap_division_es = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.english_name

    class Meta:
        db_table = 'fish'


class CSVImport(models.Model):
    uploaded_file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    cleaned_file = models.FileField(upload_to='cleaned_csv/', blank=True, null=True)
