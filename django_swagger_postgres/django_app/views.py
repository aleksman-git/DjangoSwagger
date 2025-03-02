from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializers import LoginSerializer, PasswordSerializer


class GetMethod(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    @swagger_auto_schema(operation_description="login_list",responses={
            200: 'list of logins',
            404: 'list of logins not found'
        })
    def list(self, request, *args, **kwargs):
        login_list = list(Login.objects.all().values())
        return Response(login_list)

    @swagger_auto_schema(operation_description="login_read",responses={
            200: 'your login',
            404: 'your login not found'
        })
    def retrieve(self, request, *args, **kwargs):
        login_list_id = list(Login.objects.filter(id=kwargs['pk']).values())
        return Response(login_list_id)

    @swagger_auto_schema(operation_description="login_create")
    def create(self, request, *args, **kwargs):
        login_add = LoginSerializer(data=request.data)
        if login_add.is_valid():
            login_add.save()
            return Response({"message": "Login CREATED"})
        else:
            return Response({"message": "Can't ADD. Login exists"})

    @swagger_auto_schema(operation_description="login_update")
    def update(self, request, *args, **kwargs):
        login_id = Login.objects.get(id=kwargs['pk'])
        update_login = LoginSerializer(
            login_id, data=request.data, partial=True)
        if update_login.is_valid():
            update_login.save()
            return Response({"message": "Login UPDATED"})
        else:
            return Response({"message": "Can't UPDATE"})

    @swagger_auto_schema(operation_description="login_delete")
    def destroy(self, request, *args, **kwargs):
        login_delete = Login.objects.filter(id=kwargs['pk'])
        if login_delete:
            login_delete.delete()
            return Response({"message": "Login DELETED"})
        else:
            return Response({"message": "Can't DELETE"})


class PasswordView(viewsets.ModelViewSet):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer
    http_method_names = ['get', 'post', 'put']

    @swagger_auto_schema(operation_description="password_list",responses={
            200: 'list of passwords',
            404: 'list of passwords not found'
        })
    def list(self, request, *args, **kwargs):
        password_list = list(Password.objects.all().values())
        return Response(password_list)

    @swagger_auto_schema(operation_description="password_create")
    def create(self, request, *args, **kwargs):
        password_add = PasswordSerializer(data=request.data)
        if password_add.is_valid():
            password_add.save()
            return Response({"message": "Password CREATED"})
        else:
            return Response({"message": "Can't ADD"})

    @swagger_auto_schema(operation_description="password_read",responses={
            200: 'your password',
            404: 'your password not found'
        })
    def retrieve(self, request, *args, **kwargs):
        password_list_id = list(Password.objects.filter(id=kwargs['pk']).values())
        return Response(password_list_id)

    @swagger_auto_schema(operation_description="password_update")
    def update(self, request, *args, **kwargs):
        password_id = Password.objects.get(id=kwargs['pk'])
        update_password = PasswordSerializer(
            password_id, data=request.data, partial=True)
        if update_password.is_valid():
            update_password.save()
            return Response({"message": "Password UPDATED"})
        else:
            return Response({"message": "Can't UPDATE"})