# Generated by Django 3.0.5 on 2020-04-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_intl_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='language',
            field=models.CharField(default='en', max_length=100),
            preserve_default=False,
        ),
    ]
