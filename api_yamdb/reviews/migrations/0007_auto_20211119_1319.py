# Generated by Django 2.2.16 on 2021-11-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20211119_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('moderator', 'moderator'), ('user', 'user')], default='user', max_length=9, verbose_name='Роль'),
        ),
    ]
