from django.db import models
import math

class FuelRecord(models.Model):
    date = models.DateField(verbose_name='日付')
    odometer = models.FloatField(verbose_name='総走行距離（km）')
    fuel_liters = models.FloatField(verbose_name='給油量(L)')
    price_per_liter = models.IntegerField(verbose_name='ガソリン単価（円）', blank=True, null=True)
    total_price = models.IntegerField(verbose_name='給油金額（円）', blank=True, null=True)
    memo = models.CharField(verbose_name='メモ', max_length=200, blank=True, null=True)

    odometer_diff = models.FloatField(verbose_name='走行距離差（km）', blank=True, null=True)
    fuel_efficiency_value = models.FloatField(verbose_name='燃費（km/L）', blank=True, null=True)

    def save(self, *args, **kwargs):
        # 前回のレコードを取得
        previous = FuelRecord.objects.filter(date__lt=self.date).order_by('-date').first()

        if previous:
            self.odometer_diff = self.odometer - previous.odometer
        else:
            self.odometer_diff = None

        # 燃費計算
        if self.odometer_diff and self.fuel_liters:
            self.fuel_efficiency_value = round(self.odometer_diff / self.fuel_liters, 2)
        else:
            self.fuel_efficiency_value = None
            
    #給油金額
        if self.price_per_liter and self.fuel_liters:
            self.total_price = math.ceil(self.price_per_liter * self.fuel_liters)
        else:
            self.total_price = None

        super().save(*args, **kwargs)

    @property
    def fuel_efficiency(self):
        return self.fuel_efficiency_value

    def __str__(self):
        return f"{self.date} の給油記録"

    @property
    def calc_total_price(self):
        if self.price_per_liter and self.fuel_liters:
            value = self.price_per_liter * self.fuel_liters
            return math.ceil(value)
        return None


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

#画像保存
class DashboardImage(models.Model):
    image = models.ImageField(upload_to='dashboard/')

    

    
    
    