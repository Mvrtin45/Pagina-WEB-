# Generated by Django 5.0.6 on 2024-07-19 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('UserAdmin', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('contrasenaAdmin', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='NumeroAtencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=2)),
                ('ubicacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('nombreTramite', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TramiteCedula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreC', models.CharField(max_length=100)),
                ('apellidoC', models.CharField(max_length=100)),
                ('rutC', models.CharField(max_length=10, unique=True)),
                ('fecha_nacimientoC', models.DateField()),
                ('direccionC', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TramiteVisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreV', models.CharField(max_length=20)),
                ('apellidoV', models.CharField(max_length=30)),
                ('paisV', models.CharField(max_length=30)),
                ('motivodeV', models.CharField(max_length=300)),
            ],
        ),
    ]
