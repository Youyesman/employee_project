from django.db import models


# class Position(models.Model):
#     title = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.title

class Employee(models.Model):
    chk_date = models.CharField(max_length=100)
    pic_code = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    dest = models.CharField(max_length=100)
    carrier = models.CharField(max_length=100)
    twenty = models.CharField(max_length=100)
    fourty = models.CharField(max_length=100)
    freq = models.CharField(max_length=100)
    ttime = models.CharField(max_length=100)
    effective = models.CharField(max_length=100)
    scno = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    # position = models.ForeignKey(Position,on_delete=models.CASCADE)
    
class Airfreight(models.Model):
    air_consol = models.CharField(max_length=100)
    air_pic = models.CharField(max_length=100)
    air_chk_date = models.CharField(max_length=100)
    air_origin = models.CharField(max_length=100)
    air_dest = models.CharField(max_length=100)
    air_carrier = models.CharField(max_length=100)
    air_min = models.CharField(max_length=100)
    air_normal = models.CharField(max_length=100)
    air_45kg = models.CharField(max_length=100)
    air_100kg = models.CharField(max_length=100)
    air_300kg = models.CharField(max_length=100)
    air_500kg = models.CharField(max_length=100)
    air_1000kg = models.CharField(max_length=100)
    air_fsc = models.CharField(max_length=100)
    air_iss = models.CharField(max_length=100)
    air_tspoint = models.CharField(max_length=100)
    air_skdl = models.CharField(max_length=100)
    air_remark = models.CharField(max_length=100)

class LCL(models.Model):
    LCL_chk_date = models.CharField(max_length=100)
    LCL_pic_code = models.CharField(max_length=100)
    LCL_origin = models.CharField(max_length=100)
    LCL_dest = models.CharField(max_length=100)
    LCL_ofc = models.CharField(max_length=100)
    LCL_consol = models.CharField(max_length=100)
    LCL_ttime = models.CharField(max_length=100)
    LCL_effective = models.CharField(max_length=100)
    LCL_remark = models.CharField(max_length=100)
    