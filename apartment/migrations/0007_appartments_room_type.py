# Generated by Django 2.1 on 2019-03-09 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0006_auto_20190309_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='appartments',
            name='room_type',
            field=models.CharField(choices=[('Furnished', 'Furnished'), ('Unfurnished', 'Unfurnished')], default='Furnished', max_length=50),
        ),
    ]
