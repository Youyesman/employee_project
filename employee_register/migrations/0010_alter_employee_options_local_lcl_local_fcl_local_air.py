# Generated by Django 4.0.5 on 2022-07-19 03:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee_register', '0009_airfreight_air_effective'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={},
        ),
        migrations.CreateModel(
            name='Local_Lcl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loc_Lcl_Cfs', models.CharField(max_length=10)),
                ('Loc_Lcl_Doc', models.CharField(max_length=10)),
                ('Loc_Lcl_Hdc', models.CharField(max_length=10)),
                ('Loc_Lcl_Clc', models.CharField(max_length=10)),
                ('Loc_Lcl_Blf', models.CharField(max_length=10)),
                ('Loc_Lcl_Otc', models.CharField(max_length=100)),
                ('Loc_Lcl_Remark', models.CharField(max_length=100)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
        migrations.CreateModel(
            name='Local_Fcl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loc_Fcl_Thc', models.CharField(max_length=10)),
                ('Loc_Fcl_Doc', models.CharField(max_length=10)),
                ('Loc_Fcl_Vgm', models.CharField(max_length=10)),
                ('Loc_Fcl_Seal', models.CharField(max_length=10)),
                ('Loc_Fcl_Clc', models.CharField(max_length=10)),
                ('Loc_Fcl_Hdc', models.CharField(max_length=10)),
                ('Loc_Fcl_Otc', models.CharField(max_length=100)),
                ('Loc_Fcl_Remark', models.CharField(max_length=100)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
        migrations.CreateModel(
            name='Local_Air',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loc_branch', models.CharField(max_length=10)),
                ('Loc_Air_Hdc', models.CharField(max_length=10)),
                ('Loc_Air_Hdcunit', models.CharField(choices=[('CBM', 'CBM'), ('KG', 'KG'), ('BL', 'BL')], default='CBM', max_length=5)),
                ('Loc_Air_Clc', models.CharField(max_length=10)),
                ('Loc_Air_Clcunit', models.CharField(choices=[('CBM', 'CBM'), ('KG', 'KG'), ('BL', 'BL')], default='CBM', max_length=5)),
                ('Loc_Air_Doc', models.CharField(max_length=10)),
                ('Loc_Air_Docunit', models.CharField(choices=[('CBM', 'CBM'), ('KG', 'KG'), ('BL', 'BL')], default='CBM', max_length=5)),
                ('Loc_Air_Thc', models.CharField(max_length=10)),
                ('Loc_Air_Thcunit', models.CharField(choices=[('CBM', 'CBM'), ('KG', 'KG'), ('BL', 'BL')], default='CBM', max_length=5)),
                ('Loc_Air_Otc', models.CharField(max_length=100)),
                ('Loc_Air_Remark', models.CharField(max_length=100)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
    ]
