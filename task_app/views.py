from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer


class BaseAPIViewMixin:
    queryset = None
    serializer_class = None
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TaskAPIViewMixin(BaseAPIViewMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CategoryAPIViewMixin(BaseAPIViewMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListCreateAPIView(generics.ListCreateAPIView):
    pass


class RetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)


class DestroyAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)


class TaskCreateAPI(TaskAPIViewMixin, ListCreateAPIView):
    pass


class TaskUpdateAPI(TaskAPIViewMixin, RetrieveUpdateAPIView):
    pass


class TaskDeleteAPI(TaskAPIViewMixin, DestroyAPIView):
    pass


class CategoryCreateAPI(CategoryAPIViewMixin, ListCreateAPIView):
    pass


class CategoryUpdateAPI(CategoryAPIViewMixin, RetrieveUpdateAPIView):
    pass


class CategoryDeleteAPI(CategoryAPIViewMixin, DestroyAPIView):
    pass
