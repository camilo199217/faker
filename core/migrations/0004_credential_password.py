# Generated by Django 3.2.9 on 2021-11-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211128_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='credential',
            name='password',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
