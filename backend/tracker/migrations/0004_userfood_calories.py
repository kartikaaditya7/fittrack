# Generated by Django 5.0.6 on 2024-06-22 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_user_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfood',
            name='calories',
            field=models.IntegerField(default=0),
        ),
    ]