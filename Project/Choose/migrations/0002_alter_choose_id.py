# Generated by Django 3.2.5 on 2021-07-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Choose', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choose',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]