from django import forms
from .models import Employee
from .models import Airfreight



class EmployeeForm(forms.ModelForm) :
    
    class Meta:
        model = Employee
        fields = ('chk_date','pic_code','origin','dest','carrier','twenty','fourty','freq','ttime','effective','scno','remark','position')
        labels = {
            'chk_date' : 'Check date',
            'pic_code' : 'PIC',
            'origin' : 'Origin',
            'dest' : 'Destination',
            'carrier' : 'Carrier',
            'twenty' : '20FT',
            'fourty' : '40FT',
            'freq' : 'Frequency',
            'ttime' : 'T/T',
            'effective' : '운임유효기간',
            'scno' : 'SC No.',
            'remark' : 'Remark',
            'position' : '담당자'
        }
        widgets = {
        'chk_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
        
        
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        # self.fields['position'].empty_label = "Select"
        self.fields['chk_date'].required = False  #필수 입력값 아님
        self.fields['pic_code'].required = False
        self.fields['origin'].required = False
        self.fields['dest'].required = False
        self.fields['carrier'].required = False
        self.fields['twenty'].required = False
        self.fields['fourty'].required = False
        self.fields['freq'].required = False
        self.fields['ttime'].required = False
        self.fields['effective'].required = False
        self.fields['scno'].required = False
        self.fields['remark'].required = False
        self.fields['position'].required = False
        
class AirfreightForm(forms.ModelForm) :
    
    class Meta:
        model = Airfreight
        fields = '__all__'
        # labels = {
        # }
        widgets = {
        'air_chk_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
        
        
        
    def __init__(self, *args, **kwargs):
        super(AirfreightForm,self).__init__(*args, **kwargs)
        # self.fields['position'].empty_label = "Select"
        self.fields['air_consol'].required = False  #필수 입력값 아님
        self.fields['air_pic'].required = False
        self.fields['air_chk_date'].required = False
        self.fields['air_origin'].required = False
        self.fields['air_dest'].required = False
        self.fields['air_carrier'].required = False
        self.fields['air_min'].required = False
        self.fields['air_normal'].required = False
        self.fields['air_45kg'].required = False
        self.fields['air_100kg'].required = False
        self.fields['air_300kg'].required = False
        self.fields['air_500kg'].required = False
        self.fields['air_1000kg'].required = False
        self.fields['air_fsc'].required = False
        self.fields['air_iss'].required = False
        self.fields['air_tspoint'].required = False
        self.fields['air_skdl'].required = False
        self.fields['air_remark'].required = False
        
        
        