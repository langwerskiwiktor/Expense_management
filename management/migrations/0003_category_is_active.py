# Generated by Django 5.0.6 on 2024-09-10 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_remove_expense_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
