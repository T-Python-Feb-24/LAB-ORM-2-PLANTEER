# Generated by Django 5.0.3 on 2024-03-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.ImageField(default='images/Coffee.jpg', upload_to='images/'),
        ),
    ]
