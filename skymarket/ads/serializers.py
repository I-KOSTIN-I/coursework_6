from phonenumber_field import serializerfields
from rest_framework import serializers
from ads.models import Ad, Comment

# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою


# TODO сериалайзер для модели
class CommentSerializer(serializers.ModelSerializer):

    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    author_id = serializers.ReadOnlyField(source="author.id")
    ad_id = serializers.ReadOnlyField(source="ad.id")

    class Meta:
        model = Comment
        fields = '__all__'


# TODO сериалайзер для модели
class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "description")


# TODO сериалайзер для модели
class AdDetailSerializer(serializers.ModelSerializer):

    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    author_id = serializers.ReadOnlyField(source="author.id")
    phone = serializerfields.PhoneNumberField(source="ad.phone", read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'
