# Generated by Django 4.0.6 on 2023-07-23 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0003_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
