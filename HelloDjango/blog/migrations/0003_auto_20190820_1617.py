# Generated by Django 2.2.4 on 2019-08-20 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190819_0919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='abstract',
            new_name='brief_content',
        ),
    ]