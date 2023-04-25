from rest_framework import serializers
from user.models import Users


class UserSerialize (serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    # 이메일을 아이디 값으로 취급
    # 비번은 해싱
    def update(self, instance, validated_data):
        password = validated_data.get('password', instance.password)
        instance.set_password(password)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance
