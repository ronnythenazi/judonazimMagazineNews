# Generated by Django 3.2.8 on 2021-12-23 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0016_alter_blogpost_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumb',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
