from django.db import models
import math

class FuelRecord(models.Model):
    date = models.DateField(verbose_name='日付')
    odometer = models.FloatField(verbose_name='総走行距離（km）')
    fuel_liters = models.FloatField(verbose_name='給油量(L)')
    price_per_liter = models.IntegerField(verbose_name='ガソリン単価（円）', blank=True, null=True)
    total_price = models.IntegerField(verbose_name='給油金額（円）', blank=True, null=True)
    memo = models.CharField(verbose_name='メモ', max_length=200, blank=True, null=True)

                            
    @property

    def fuel_efficiency(self):
        previous = FuelRecord.objects.filter(date__lt=self.date).order_by('-date').first()
        if previous:
            distance = self.odometer - previous.odometer
            if self.fuel_liters > 0:
                return round(distance / self.fuel_liters, 2)
        return None

    def __str__(self):
        return f"{self.date} の給油記録"
    
    @property
    #給油金額＝給油量×ガソリン単価切り上げ   
    def calc_total_price(self):
        if self.price_per_liter and self.fuel_liters:
            value=self.price_per_liter * self.fuel_liters
            return math.ceil(value)
        return None 
    
#エンジンオイルの記録モデル
class MaintenanceRecord(models.Model):
    date = models.DateField(verbose_name='交換日')
    odometer = models.IntegerField(verbose_name='走行距離（km）')
    interval = models.IntegerField(verbose_name='交換時期（km）', default=3000)
    memo = models.CharField(verbose_name='メモ', max_length=200, blank=True, null=True)
    
    @property
    def next_change(self):
        return self.odometer + self.interval
    
    def __str__(self):
        return f"{self.date} ({self.odometer} km)"
    
    