# Generated by Django 4.2 on 2023-05-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0005_country_alter_title_age_limit_remove_title_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='description',
        ),
        migrations.RemoveField(
            model_name='title',
            name='poster',
        ),
        migrations.AddField(
            model_name='title',
            name='h_poster',
            field=models.ImageField(blank=True, null=True, upload_to='title/h_poster/'),
        ),
        migrations.AddField(
            model_name='title',
            name='v_poster',
            field=models.ImageField(blank=True, null=True, upload_to='title/v_poster/'),
        ),
    ]
