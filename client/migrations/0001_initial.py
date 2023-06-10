# Generated by Django 4.1.3 on 2022-11-29 23:15

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('document_type', models.CharField(choices=[('CC', 'CEDULA DE CIUDADANIA'), ('CE', 'CEDULA DE EXTRANJERIA'), ('PA', 'PASAPORTE'), ('TI', 'TARJETA DE IDENTIDAD'), ('IT', 'IDENTIFICACION TRIBUTARIA'), ('IP', 'IDENTIFICACION PERSONAL')], max_length=3)),
                ('document_number', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('sex', models.CharField(choices=[('F', 'FEMALE'), ('M', 'MALE'), ('UN', 'UNKNOWN')], default='UNKNOWN', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergies', models.CharField(default='unknown', max_length=50)),
                ('herpes', models.CharField(default='unknown', max_length=50)),
                ('Skin_illness', models.CharField(default='unknown', max_length=50)),
                ('condition', models.CharField(default='unknown', max_length=50)),
                ('cardiac', models.CharField(default='unknown', max_length=50)),
                ('hypertension', models.CharField(default='unknown', max_length=50)),
                ('diabetes', models.CharField(default='unknown', max_length=50)),
                ('thyroid', models.CharField(default='unknown', max_length=50)),
                ('autoimmune_disease', models.CharField(default='unknown', max_length=50)),
                ('surgical_history', models.CharField(default='unknown', max_length=50)),
                ('pregnancy', models.CharField(default='unknown', max_length=50)),
                ('ication', models.CharField(default='unknown', max_length=50)),
                ('pacemaker', models.CharField(default='unknown', max_length=50)),
                ('prosthesis', models.CharField(default='unknown', max_length=50)),
                ('diu', models.CharField(default='unknown', max_length=50)),
                ('implants', models.CharField(default='unknown', max_length=50)),
                ('others', models.CharField(default='unknown', max_length=50)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client.profileclient')),
            ],
        ),
    ]