# Generated by Django 5.0.6 on 2024-06-28 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TramiFast', '0002_tramitevisa_alter_numeroatencion_ubicacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='TramiteCedula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreC', models.CharField(max_length=100)),
                ('apellidoC', models.CharField(max_length=100)),
                ('rutC', models.CharField(max_length=10, unique=True)),
                ('fecha_nacimientoC', models.DateField()),
                ('direccionC', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='tramitevisa',
            name='motivodeV',
            field=models.CharField(max_length=300),
        ),
    ]