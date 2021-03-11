from django.db import models
from pytz import unicode

# Представление моделей данных главных классов

# Класс категория: название
class Category(models.Model):

    parent_id = models.IntegerField(blank=True, default=0)
    name = models.CharField(max_length=200)

    def __str__(self):
        return unicode(self.name)

# Класс рабочие: поле имя, поле телефон, email
class Workers(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    position = models.CharField(max_length=200)

    def __str__(self):
        return unicode(self.email)


