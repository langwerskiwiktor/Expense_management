# Generated by Django 5.0.1 on 2024-02-04 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_paymentmethod_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='last_added_expense',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.expense'),
        ),
    ]
