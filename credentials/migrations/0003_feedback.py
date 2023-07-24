# Generated by Django 4.0.6 on 2023-07-23 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('review', models.TextField()),
                ('rating', models.PositiveIntegerField()),
            ],
        ),
    ]
