# Generated by Django 5.1.1 on 2024-09-27 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_collectionimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectionimage',
            old_name='product',
            new_name='collection',
        ),
    ]
