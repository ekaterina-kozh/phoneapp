import this

from rest_framework import serializers

from app.workers.models import Category, Workers

# Сериализация данных для понятного вывода



# Сериализация категории
class CategoryWorkersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'



# Сериализация рабочего (без ин-ции о категории)
class WorkersSmallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workers
        fields = '__all__'


# Сериализация категории (полностью)
class WorkersSerializer(serializers.ModelSerializer):

    category = CategoryWorkersSerializer(read_only=True, many=False)

    class Meta:
        model = Workers
        fields = '__all__'
