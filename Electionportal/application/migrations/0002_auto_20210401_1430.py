# Generated by Django 3.1.7 on 2021-04-01 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='date_of_application',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
