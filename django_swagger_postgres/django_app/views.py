from pickle import FALSE
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
#from drf_spectacular.utils import OpenApiParameter


from .models import Login
from .serializers import LoginSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    http_method_names = ['get', 'post']#, 'put', 'delete']

    @extend_schema(
        responses={200: LoginSerializer(many=True), 400: 'email не найден'},  # Добавить реализацию Serializer400
        summary="Получить адреса почты всех зарегистрированных пользователей",
        description="Получить все email адреса"
    )
    def list(self, request, *args, **kwargs):
        try:
            # получить все email адреса
            email_list = Login.objects.all().values()
            serializer = LoginSerializer(email_list, many=True)
            data = serializer.data
            return Response(data)
        except Exception as ex:
            details = {'message': 'Не удалось получить адреса',
                       'details': str(ex)}
            # детализация кода ошибки
            return Response(details, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses={200: LoginSerializer(many=False), 400: 'email не найден'},  # Добавить реализацию Serializer400
        summary="Получить адрес почты зарегистрированного пользователя",
        description="Получить email по id пользователя"
   )
    def retrieve(self, request, *args, **kwargs):
       try:
           # получить email по ключу (id пользователя)
           email = Login.objects.get(id=kwargs['pk'])
           # передать в сериализатор значение email
           # так как получить надо одно значение many=False
           serializer = LoginSerializer(email, many=False)
           data = serializer.data
           return Response(data)
       except Exception as ex:
           details = {'message': 'Не удалось получить адрес по правилу фильтрации',
                      'details': str(ex)}
           # детализация кода ошибки
           return Response(details, status=status.HTTP_400_BAD_REQUEST)

#   def get(self, *args, **kwargs):
#       try:
#           # определить правило в кластере
#           cluster = kwargs_get(kwargs, model=Cluster, param='id_cluster')
#           # проверит права на кластер
#           cluster_permission(self.request, cluster)
#           # получить правило
#           rule = kwargs_get(kwargs, query=RuleFirewall.objects.filter(cluster=cluster), param='id_rule')
#           # получить все наборы
#           kit = RuleFirewallKit.objects.filter(rule=rule)
#           serializer = RuleKitViewSerializer(kit, many=True)
#           data = serializer.data
#            return Response(data)
#        except Exception as ex:


#        details = {'message': 'Не удалось получить список всех наборов в правиле',
#                   'details': str(ex)}
#        return Response(details, status=status.HTTP_400_BAD_REQUEST)

"""
    @swagger_auto_schema(responce_body=LoginSerializer)
    def list(self, request, *args, **kwargs):
        return super(LoginViewSet, self).list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="login_read",responses={
            200: 'your login',
            404: 'your login not found'
        })
    def retrieve(self, request, *args, **kwargs):
        login_list_id = Login.objects.filter(id=kwargs['pk']).values()
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

"""