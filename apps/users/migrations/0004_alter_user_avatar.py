# Generated by Django 4.2 on 2023-04-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_watched_titles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='default_avatar.png', null=True, upload_to='user_avatar/'),
        ),
    ]