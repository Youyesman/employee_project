# Generated by Django 4.0.5 on 2022-06-15 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='airfreight',
            name='air_remark',
            field=models.CharField(default=1123, max_length=100),
            preserve_default=False,
        ),
    ]