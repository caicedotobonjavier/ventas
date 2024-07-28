from django.shortcuts import render
#
from .models import User
#
from django.contrib.auth import authenticate, login, logout
#
from rest_framework.authtoken.models import Token
#
from rest_framework.views import APIView
#
from rest_framework.response import Response
#
from .serializers import LoginSerializer, CrearUsuarioSerializador


class CrearUsuarioApiView(APIView):
    serializer_class = CrearUsuarioSerializador
    
    def post(self, request, *args, **kwargs):
        serializador = self.serializer_class(data=request.data)
        serializador.is_valid(raise_exception=True)

        email = serializador.validated_data['email']
        nombre_completo = serializador.validated_data['nombre_completo']
        ocupacion = serializador.validated_data['ocupacion']
        fecha_nacimiento = serializador.validated_data['fecha_nacimiento']
        direccion = serializador.validated_data['direccion']
        password = serializador.validated_data['password']

        usuario = User.objects.create_user(
            email,
            password,
            nombre_completo=nombre_completo,
            ocupacion=ocupacion,
            fecha_nacimiento=fecha_nacimiento,
            direccion=direccion
        )        

        return Response(
            {
                'mensaje' : 'Usuario creado correctamente'
            }
        )


# Esta clase de Python representa una vista de inicio de sesión que autentica a un usuario, genera un token y devuelve
# información del usuario al iniciar sesión correctamente.
class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializador = self.serializer_class(data=request.data)
        serializador.is_valid(raise_exception=True)
        serializador.validated_data
        print(serializador)

        email = serializador.validated_data['email']
        contrasena = serializador.validated_data['password']

        usuario = authenticate(email=email, password=contrasena)
        
        login(self.request, usuario)

        token, created = Token.objects.get_or_create(
            user = usuario
        )
        
                
        usuario_logueado = {
            'user' : usuario.email,
            'nombre' : usuario.nombre_completo,
            'ocupacion' : usuario.ocupacion,
            'token' : token.key,
        }


        return Response(
            {
                'usaurio' : usuario_logueado
            }
        )