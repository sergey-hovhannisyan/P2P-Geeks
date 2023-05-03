# Generated by Django 4.2 on 2023-05-03 00:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0012_alter_interview_interview_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="interview",
            name="rating",
            field=models.IntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
    ]
