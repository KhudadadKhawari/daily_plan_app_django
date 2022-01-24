# Generated by Django 4.0.1 on 2022-01-24 21:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_plan_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
