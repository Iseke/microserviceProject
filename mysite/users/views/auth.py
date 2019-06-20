from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token as TokenModel


@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    token, created = TokenModel.objects.get_or_create(user=user)
    return Response({'token': token.key})


@api_view(['POST'])
def logout(request):
    token = TokenModel(request.auth)
    token.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST','GET'])
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.data)
        if form.is_valid():
            form.save()
            return redirect('/api/login/')
        return JsonResponse({'out': 'invalid'})
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'register.html', args)