from django import forms
from .models import FuelRecord

class FuelRecordForm(forms.ModelForm):
    class Meta:
        model = FuelRecord
        fields = ['date', 'odometer', 'fuel_liters', 'price_per_liter', 'memo']
        labels = {
            'date': '日付',
            'odometer': '総走行距離',
            'fuel_liters': '給油量（L）',
            'price_per_liter': 'ガソリン価格（円/L）',
            'memo': 'メモ',
        }
        help_texts = {
            'date': '例：2024-01-01',
            'odometer': '例：46000（km）',
            'fuel_liters': '例：0.45（L）',
            'price_per_liter': '例：150（円/L）',
        }

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