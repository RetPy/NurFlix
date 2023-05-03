# Generated by Django 4.2 on 2023-05-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0004_alter_title_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='title',
            name='age_limit',
            field=models.CharField(max_length=15),
        ),
        migrations.RemoveField(
            model_name='title',
            name='country',
        ),
        migrations.AddField(
            model_name='title',
            name='country',
            field=models.ManyToManyField(related_name='title_country', to='titles.country'),
        ),
    ]
