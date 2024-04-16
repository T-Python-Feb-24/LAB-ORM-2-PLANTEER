# Generated by Django 5.0.3 on 2024-03-22 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('used_for', models.TextField()),
                ('image', models.ImageField(default='images/default_img.jpg', upload_to='images/')),
                ('category', models.CharField(choices=[('Tree', 'Tree'), ('Fruit', 'Fruit'), ('Vegetables', 'Vegetables')], max_length=64)),
                ('is_edible', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
