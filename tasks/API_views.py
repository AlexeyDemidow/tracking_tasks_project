from rest_framework import generics, status
from rest_framework.response import Response

from tasks.models import Task
from tasks.serializers import TaskSerializer, TaskStatusSerializer


class TaskCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        telegram_user_id = self.request.query_params.get('telegram_user_id')

        if telegram_user_id:
            return Task.objects.filter(telegram_user_id=telegram_user_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset and 'telegram_user_id' in request.query_params:
            return Response(
                {"detail": "Пользователь не найден или у него нет задач."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TaskStatusUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    status_serializer_class = TaskStatusSerializer
    http_method_names = ['get', 'patch']

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.status_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance.status = serializer.validated_data['status']
        instance.save(update_fields=['status'])

        response_serializer = self.serializer_class(instance)
        return Response(response_serializer.data)
