#
from rest_framework import serializers
#
from .models import User
#
from django.contrib.auth import authenticate


class CrearUsuarioSerializador(serializers.Serializer):
    email = serializers.EmailField()
    nombre_completo = serializers.CharField()
    ocupacion = serializers.CharField()
    fecha_nacimiento = serializers.DateField()
    direccion = serializers.CharField()
    password = serializers.CharField()
    confirmar_password = serializers.CharField()

    def validate(self, data):
        if data['password'] != data['confirmar_password']:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        
        return data


# La clase `LoginSerializer` en Python valida los datos de correo electrónico y contraseña para la autenticación del usuario.
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError("Email o contraseña incorrectas")
        else:
            return data      