# Generated by Django 5.0.3 on 2024-03-27 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_contact_rename_content_comment_context'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='context',
            new_name='content',
        ),
    ]
