# Generated by Django 4.0 on 2022-07-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_archive_date_created_delete_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='archive',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
