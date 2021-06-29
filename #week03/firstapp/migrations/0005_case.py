# Generated by Django 3.1.7 on 2021-06-29 00:32

from django.db import migrations, models
import django.db.models.deletion
import font_icons.models


class Migration(migrations.Migration):

    dependencies = [
        ('font_icons', '0003_auto_20190304_1154'),
        ('firstapp', '0004_choose'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('short_info', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(upload_to='Case_image', verbose_name='Sekil')),
                ('short_description', models.CharField(blank=True, max_length=127, null=True)),
                ('icon', font_icons.models.IconForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='font_icons.fonticonmodel')),
            ],
        ),
    ]
