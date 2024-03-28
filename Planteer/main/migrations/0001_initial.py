# Generated by Django 5.0.3 on 2024-03-27 10:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def make_profiles(apps, schema_editor):
   User = apps.get_model(settings.AUTH_USER_MODEL)
   Profile = apps.get_model('account', 'Profile')
   profiles = [Profile(user=user)
               for user in User.objects.filter(profile=None)]
   Profile.objects.bulk_create(profiles)


class Migration(migrations.Migration):

   initial = True

   dependencies = [
       migrations.swappable_dependency(settings.AUTH_USER_MODEL),
   ]

   operations = [
       migrations.CreateModel(
           name='Contact',
           fields=[
               ('id', models.BigAutoField(auto_created=True,
                primary_key=True, serialize=False, verbose_name='ID')),
               ('first_name', models.CharField(max_length=20)),
               ('last_name', models.CharField(max_length=20)),
               ('email', models.EmailField(max_length=254)),
               ('message', models.TextField()),
               ('created_at', models.DateTimeField(auto_now_add=True)),
           ],
           options={
               'ordering': ['-created_at'],
           },
       ),
       migrations.CreateModel(
           name='Plant',
           fields=[
               ('id', models.BigAutoField(auto_created=True,
                primary_key=True, serialize=False, verbose_name='ID')),
               ('name', models.CharField(max_length=20)),
               ('about', models.TextField()),
               ('used_for', models.TextField()),
               ('image', models.ImageField(upload_to='images/plant/')),
               ('category', models.CharField(choices=[('Fruit', 'Fruit'), ('Vegetables', 'Vegetables'), (
                  'Flower', 'Flawer'), ('Herb', 'Herb'), ('Mushroom', 'Mushroom')], default='Fruit', max_length=10)),
               ('is_edible', models.BooleanField()),
               ('created_at', models.DateTimeField(auto_now_add=True)),
           ],
           options={
               'ordering': ['name'],
           },
       ),
       migrations.CreateModel(
           name='Comment',
           fields=[
               ('id', models.BigAutoField(auto_created=True,
                primary_key=True, serialize=False, verbose_name='ID')),
               ('content', models.TextField()),
               ('comment_date', models.DateTimeField(auto_now_add=True)),
               ('user', models.ForeignKey(
                  on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
               ('plant', models.ForeignKey(
                  on_delete=django.db.models.deletion.CASCADE, to='main.plant')),
           ],
           options={
               'ordering': ['-comment_date'],
           },
       ),
   ]
