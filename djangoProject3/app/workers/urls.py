from django.urls import path

from app.workers.views import GetListCategoryWorkers, GetListAllWorkers, \
    CreateCategory, CreateWorkers, ItemCategoryViews, ItemWorkersViews, ListWorkersByCategory

# Файл содержит url страниц

urlpatterns = [
    # список всех категорий
    path('list/all/category/workers/', GetListCategoryWorkers.as_view()),
    # список всех рабочих
    path('list/all/workers/', GetListAllWorkers.as_view()),
    # добавить новую категорию
    path('create/category/', CreateCategory.as_view()),
    # добавить нового сотрудника
    path('create/workers/', CreateWorkers.as_view()),
    # поиск категории по id
    path('item/category/<int:pk>/', ItemCategoryViews.as_view()),
    # поиск рабочих по id
    path('item/workers/<int:pk>/', ItemWorkersViews.as_view()),
    # список всех рабочих, принадлежащих конкретной категории
    path('list/workers/category/<int:pk>/', ListWorkersByCategory.as_view()),
]
