# Generated by Django 4.2 on 2023-05-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0003_alter_person_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='title_image/'),
        ),
    ]