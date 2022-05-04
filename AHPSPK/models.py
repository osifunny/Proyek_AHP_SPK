from django.db import models

# Create your models here.
class TProcessor (models.Model):
    Jenis = models.CharField(max_length=50,null = True)
    Nilai = models.IntegerField(null=True)
    def __str__(self):
        return self.Jenis

class Laptop (models.Model):
    Laptop = models.CharField(max_length=50)
    Harga = models.IntegerField()
    RAM = models.IntegerField()
    Processor = models.ForeignKey(TProcessor,on_delete=models.CASCADE,null=True)
    Storage = models.IntegerField()
    Berat = models.FloatField()
    def __str__(self):
        return self.Laptop

class kriteria_nilai(models.Model):
    kharga = models.IntegerField()
    kram = models.IntegerField()
    kprocessor = models.IntegerField()
    kstorage = models.IntegerField()
    kberat = models.IntegerField()