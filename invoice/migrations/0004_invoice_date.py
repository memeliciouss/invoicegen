# Generated by Django 5.1.7 on 2025-03-08 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_items_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='date',
            field=models.DateField(default=datetime.date(2025, 3, 8)),
            preserve_default=False,
        ),
    ]
