# Generated by Django 2.0.3 on 2018-04-16 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_table_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='icon',
            field=models.CharField(default='', max_length=31),
            preserve_default=False,
        ),
    ]
