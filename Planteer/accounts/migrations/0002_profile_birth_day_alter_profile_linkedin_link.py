# Generated by Django 5.0.2 on 2024-03-27 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_day',
            field=models.DateField(default=0.0005),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin_link',
            field=models.URLField(blank=True),
        ),
    ]
