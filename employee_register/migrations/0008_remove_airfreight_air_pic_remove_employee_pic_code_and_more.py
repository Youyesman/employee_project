# Generated by Django 4.0.5 on 2022-07-15 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0007_lcl_lcl_ofcunit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airfreight',
            name='air_pic',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='pic_code',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
        migrations.AlterField(
            model_name='lcl',
            name='LCL_dest',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='lcl',
            name='LCL_ofcunit',
            field=models.CharField(choices=[('CBM', 'CBM'), ('KG', 'KG'), ('BL', 'BL')], default='CBM', max_length=5),
        ),
        migrations.AlterField(
            model_name='lcl',
            name='LCL_origin',
            field=models.CharField(max_length=4),
        ),
    ]