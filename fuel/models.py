from django.db import models

class FuelRecord(models.Model):
    date = models.DateField(verbose_name='日付')
    odometer = models.FloatField(verbose_name='総走行距離（km）')
    fuel_liters = models.FloatField(verbose_name='給油量(L)')
    price_per_liter = models.IntegerField(verbose_name='ガソリン単価（円）', blank=True, null=True)
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
