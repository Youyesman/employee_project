# Generated by Django 4.0.5 on 2022-06-27 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0002_airfreight_air_remark'),
    ]

    operations = [
        migrations.CreateModel(
            name='LCL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LCL_chk_date', models.CharField(max_length=100)),
                ('LCL_pic_code', models.CharField(max_length=100)),
                ('LCL_origin', models.CharField(max_length=100)),
                ('LCL_dest', models.CharField(max_length=100)),
                ('LCL_ofc', models.CharField(max_length=100)),
                ('LCL_consol', models.CharField(max_length=100)),
                ('LCL_ttime', models.CharField(max_length=100)),
                ('LCL_effective', models.CharField(max_length=100)),
                ('LCL_remark', models.CharField(max_length=100)),
            ],
        ),
    ]
