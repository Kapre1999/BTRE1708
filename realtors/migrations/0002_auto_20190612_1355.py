# Generated by Django 2.2.1 on 2019-06-12 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='hire_data',
            new_name='hire_date',
        ),
    ]
