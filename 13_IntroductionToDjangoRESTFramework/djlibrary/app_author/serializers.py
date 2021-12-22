from logic_library.models import AuthorModel
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ['id', 'name', 'surname', 'date_of_birth']
