from django import forms
from datetime import date

from .models import FuelRecord, MaintenanceRecord, DashboardImage


class FuelRecordForm(forms.ModelForm):
    class Meta:
        model = FuelRecord
        fields = ['date', 'odometer', 'fuel_liters', 'price_per_liter', 'total_price', 'memo']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}
    
        labels = {
            'date': '日付',
            'odometer': '総走行距離',
            'fuel_liters': '給油量（L）',
            'price_per_liter': 'ガソリン単価（円/L）',
            'total_price': '給油金額（円）',
            'memo': 'メモ',
        }
        help_texts = {
            'date': '例：2024-01-01',
            'odometer': '例：46000（km）',
            'fuel_liters': '例：2.5（L）',
            'price_per_liter': '例：150（円/L）',
            'total_price': '例：500（円）',
        }
        
        #入力日を「当日」で表示
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = date.today()
        
class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = ['date', 'odometer', 'interval', 'memo']
        labels = {
            'date': '交換日',
            'odometer': '走行距離',
            'interval': '次回交換距離',
            'memo': 'メモ',
        }
        help_texts = {
            'date': '例：2024-01-01',
            'odometer': '例：46000（km）',
            'interval': '例：3000（km）',
        }
        
        
class DashboardImageForm (forms.ModelForm):
    class Meta:
        model = DashboardImage
        fields =['image'] 
