# Generated by Django 4.0.5 on 2022-07-19 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0010_alter_employee_options_local_lcl_local_fcl_local_air'),
    ]

    operations = [
        migrations.AddField(
            model_name='local_lcl',
            name='Loc_Lcl_Blfunit',
            field=models.CharField(choices=[('CBM', 'CBM'), ('KG', 'KG'), ('BL', 'BL')], default='CBM', max_length=5),
        ),
        migrations.AddField(
            model_name='local_lcl',
            name='Loc_Lcl_Cfsunit',
            field=models.CharField(choices=[('CBM', 'CBM'), ('KG', 'KG'), ('BL', 'BL')], default='CBM', max_length=5),
        ),
        migrations.AddField(
            model_name='local_lcl',
            name='Loc_Lcl_Clcunit',
            field=models.CharField(choices=[('CBM', 'CBM'), ('KG', 'KG'), ('BL', 'BL')], default='CBM', max_length=5),
        ),
        migrations.AddField(
            model_name='local_lcl',
            name='Loc_Lcl_Docunit',
            field=models.CharField(choices=[('CBM', 'CBM'), ('KG', 'KG'), ('BL', 'BL')], default='CBM', max_length=5),
        ),
        migrations.AddField(
            model_name='local_lcl',
            name='Loc_Lcl_Hdcunit',
            field=models.CharField(choices=[('CBM', 'CBM'), ('KG', 'KG'), ('BL', 'BL')], default='CBM', max_length=5),
        ),
        migrations.AddField(
            model_name='local_lcl',
            name='Loc_branch',
            field=models.CharField(default=123, max_length=10),
            preserve_default=False,
        ),
    ]