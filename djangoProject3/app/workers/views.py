from django.http import Http404
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from app.workers.models import Category, Workers


# Файл содержит функции взаимодействия с данными

# получить список всех категорий
from app.workers.sezializers import CategoryWorkersSerializer, WorkersSerializer, WorkersSmallSerializer


class GetListCategoryWorkers(generics.ListAPIView):
    serializer_class = CategoryWorkersSerializer

    def get_queryset(self):
        return Category.objects.all()


# получить список всех работников
class GetListAllWorkers(generics.ListAPIView):
    serializer_class = WorkersSerializer

    def get_queryset(self):
        return Workers.objects.all()


# добавление новой категории
class CreateCategory(APIView):

    def post(self, request, format=None):
        serializer = CategoryWorkersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# добавление нового рабочего
class CreateWorkers(APIView):

    def post(self, request, format=None):
        serializer = WorkersSmallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# поиск и вывод, добавление и редактирование категории по id
class ItemCategoryViews(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CategoryWorkersSerializer(snippet)
        return Response(serializer.data)

    def patch(self, request, pk):

        obj = self.get_object(pk)

        serializer = CategoryWorkersSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CategoryWorkersSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# поиск и вывод, добавление и редактирование рабочих по id
class ItemWorkersViews(APIView):

    def get_object(self, pk):
        try:
            return Workers.objects.get(pk=pk)
        except Workers.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = WorkersSerializer(snippet)
        return Response(serializer.data)

    def patch(self, request, pk):

        obj = self.get_object(pk)

        serializer = WorkersSmallSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = WorkersSmallSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# вывод данных сотрудников по отпределенному каталогу
class ListWorkersByCategory(ListModelMixin, GenericAPIView):
    serializer_class = WorkersSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Workers.objects.filter(category_id=pk)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
