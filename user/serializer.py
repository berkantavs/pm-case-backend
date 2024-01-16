from rest_framework import serializers
from .models import Birim, Kullanici, Personel

class BirimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Birim
        fields = ['id', 'birim_ad', 'ust_birim', 'user_type']

class KullaniciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kullanici
        fields = ['id', 'kullanici_ad', 'email', 'sifre', 'birim', 'ilce', 'mahalle', 'user_type']

class PersonelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personel
        fields = ['id', 'personel_ad', 'pozisyon', 'birim', 'user_type']
