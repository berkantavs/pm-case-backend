from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializer import *
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.shortcuts import get_object_or_404
from .models import *

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = KullaniciSerializer(data=request.data)
        if serializer.is_valid():
            # Kullanıcıyı kaydet
            user = serializer.save()

            return Response({
                'user_id': user.id,
                'username': user.kullanici_ad,
                'email': user.email,
                'user_type':user.user_type,
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('kullanici_ad')
    password = request.data.get('sifre')

    if username is None and password is None:
        user = Kullanici.objects.create(email='guest@example.com')
    else:
        user = Kullanici.objects.filter(kullanici_ad=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        print(user.kullanici_ad)
        print(user.sifre)
        if not (username == user.kullanici_ad and password == user.sifre):
            raise AuthenticationFailed('invalid credentials!')
    if user:
        return Response({
            'user_id': user.id,
            'username': user.kullanici_ad,
            'email': user.email,
            'user_type':user.user_type,
        }, status=status.HTTP_200_OK)   
    else:
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_units(request):
    birimler = Birim.objects.all()
    serializer = BirimSerializer(birimler, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_unit_by_id(request, birim_id):
    try:
        birim = Birim.objects.get(id=birim_id)
        serializer = BirimSerializer(birim)
        return Response(serializer.data)
    except Birim.DoesNotExist:
        return Response({"message": "Birim bulunamadı"}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def create_unit(request):
    serializer = BirimSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)   

@api_view(['GET'])
def delete_unit(request, pk):
    print(pk,'pk')
    try:
        birim = Birim.objects.get(pk=pk)
    except Birim.DoesNotExist:
        return Response({'detail': 'Birim bulunamadı'}, status=status.HTTP_404_NOT_FOUND)

    birim.delete()
    return Response({'detail': 'Birim başarıyla silindi'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_unit(request, birim_id):
    try:
        birim = Birim.objects.get(id=birim_id)
    except Birim.DoesNotExist:
        return Response({"error": "Birim not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = BirimSerializer(birim, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# USERS

@api_view(['GET'])
def get_users(request):
    kullanici_list = Kullanici.objects.all()
    serializer = KullaniciSerializer(kullanici_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_by_id(request, user_id):
    kullanici = get_object_or_404(Kullanici, id=user_id)
    serializer = KullaniciSerializer(kullanici)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = KullaniciSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def delete_user(request, user_id):
    try:
        user = Kullanici.objects.get(pk=user_id)
        user.delete()
        return Response({'detail': 'Kullanıcı başarıyla silindi.'}, status=status.HTTP_204_NO_CONTENT)
    except Kullanici.DoesNotExist:
        return Response({'detail': 'Belirtilen ID ile kullanıcı bulunamadı.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['PUT'])
def update_user(request, user_id):
    user = get_object_or_404(Kullanici, id=user_id)

    data = request.data

    serializer = KullaniciSerializer(user, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)
# EMPLOYEE
@api_view(['GET'])
def get_personels(request):
    personels = Personel.objects.all()
    serializer = PersonelSerializer(personels, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_personel(request):
    serializer = PersonelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def delete_personel(request, personel_id):
    try:
        personel = Personel.objects.get(pk=personel_id)
    except Personel.DoesNotExist:
        return Response({'detail': 'Personel not found'}, status=status.HTTP_404_NOT_FOUND)

    personel.delete()

    return Response({'detail': 'Personel deleted successfully'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_employee_by_id(request, personel_id):
    personel = get_object_or_404(Personel, id=personel_id)
    serializer = PersonelSerializer(personel)
    return Response(serializer.data)

@api_view(['PUT'])
def update_employee(request, personel_id):
    try:
        personel = Personel.objects.get(pk=personel_id)
    except Personel.DoesNotExist:
        return Response({'error': 'Personel not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PersonelSerializer(personel, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)