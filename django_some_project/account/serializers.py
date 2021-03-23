from rest_framework import  serializers
from account.models import Account


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'password')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = Account.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
