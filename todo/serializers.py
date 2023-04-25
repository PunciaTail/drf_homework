from rest_framework import serializers
from todo.models import Todos


class TodoSerialize(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'


class TodoCreateSerialize(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = ['title', ]