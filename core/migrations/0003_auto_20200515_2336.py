# Generated by Django 3.0.6 on 2020-05-16 02:36

import core.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200515_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem'),
        ),
    ]
