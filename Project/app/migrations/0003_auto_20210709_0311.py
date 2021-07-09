# Generated by Django 3.1.7 on 2021-07-08 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_category_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='skill',
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
            preserve_default=False,
        ),
    ]