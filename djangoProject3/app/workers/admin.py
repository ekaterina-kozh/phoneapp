from django.contrib import admin
from app.workers.models import Category, Workers

# Сторона админимтратора (Просмотр, добавлени, удаление, редактирвание данных)

admin.site.register(Category)
admin.site.register(Workers)
