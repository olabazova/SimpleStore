# Generated by Django 2.2.2 on 2019-06-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imageUrl',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]