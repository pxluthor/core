# Generated by Django 4.2.7 on 2023-11-04 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 11, 50, 15, 44285, tzinfo=datetime.timezone.utc)),
        ),
    ]
