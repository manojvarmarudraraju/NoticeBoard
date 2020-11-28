# Generated by Django 2.0.5 on 2018-05-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.CharField(max_length=1000)),
                ('teachername', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('year', models.IntegerField()),
                ('section', models.CharField(max_length=6)),
                ('branch', models.CharField(max_length=10)),
            ],
        ),
    ]