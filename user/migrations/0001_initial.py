# Generated by Django 5.0.1 on 2024-01-13 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birim_ad', models.CharField(max_length=255)),
                ('user_type', models.CharField(max_length=50)),
                ('ust_birim', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.birim')),
            ],
        ),
        migrations.CreateModel(
            name='Kullanici',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kullanici_ad', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('sifre', models.CharField(max_length=255)),
                ('ilce', models.CharField(max_length=255)),
                ('mahalle', models.CharField(max_length=255)),
                ('user_type', models.CharField(max_length=50)),
                ('birim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.birim')),
            ],
        ),
        migrations.CreateModel(
            name='Personel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personel_ad', models.CharField(max_length=255)),
                ('pozisyon', models.CharField(max_length=255)),
                ('user_type', models.CharField(max_length=50)),
                ('birim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.birim')),
            ],
        ),
    ]
