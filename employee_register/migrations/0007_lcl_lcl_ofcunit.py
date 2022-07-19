# Generated by Django 4.0.5 on 2022-07-11 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0006_airfreight_username_employee_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='lcl',
            name='LCL_ofcunit',
            field=models.CharField(choices=[('CBM', 'CBM'), ('KG', 'KG'), ('BL', 'Antigua')], default=1, max_length=5),
            preserve_default=False,
        ),
    ]