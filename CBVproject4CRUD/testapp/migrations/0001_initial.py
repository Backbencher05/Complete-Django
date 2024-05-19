# Generated by Django 3.2.5 on 2023-11-18 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=30)),
                ('pages', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
