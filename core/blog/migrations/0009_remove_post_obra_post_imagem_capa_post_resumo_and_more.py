# Generated by Django 4.2.7 on 2023-11-20 01:14

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='obra',
        ),
        migrations.AddField(
            model_name='post',
            name='imagem_capa',
            field=models.ImageField(blank=True, null=True, upload_to='static/blog/'),
        ),
        migrations.AddField(
            model_name='post',
            name='resumo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 11, 20, 1, 14, 32, 246934, tzinfo=datetime.timezone.utc)),
        ),
    ]
