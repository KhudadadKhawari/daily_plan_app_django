# Generated by Django 4.0.1 on 2022-01-24 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_plan_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]