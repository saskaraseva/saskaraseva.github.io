# Generated by Django 2.0 on 2018-08-20 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_phone', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'client',
            },
        ),
    ]
