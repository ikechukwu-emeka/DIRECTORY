# Generated by Django 4.1 on 2022-10-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=11)),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
    ]
