# Generated by Django 4.2.7 on 2023-11-22 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_userinfo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='title',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]