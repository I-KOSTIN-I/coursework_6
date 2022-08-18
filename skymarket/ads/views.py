from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer
from ads.models import AdFilter


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_id")
        new_queryset = Comment.objects.filter(ad=ad_id)
        return new_queryset

    def perform_create(self, serializer):
        user = self.request.user
        ad_id = self.kwargs.get("ad_id")
        ad = get_object_or_404(Ad, pk=ad_id)
        serializer.save(author=user, ad=ad)

