# Generated by Django 2.0.7 on 2020-06-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
                ('age', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
