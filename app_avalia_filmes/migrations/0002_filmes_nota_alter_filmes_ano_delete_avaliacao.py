# Generated by Django 5.1.6 on 2025-03-01 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_avalia_filmes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmes',
            name='nota',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filmes',
            name='ano',
            field=models.IntegerField(max_length=4),
        ),
        migrations.DeleteModel(
            name='Avaliacao',
        ),
    ]
