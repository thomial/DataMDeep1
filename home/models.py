# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from validator import validate_file_extension

# Create your models here.
class table_post_description(models.Model):
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField()
    document = models.FileField(upload_to='documents/', validators=[validate_file_extension])
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

class Import_Nilai(models.Model):
    tahun = models.CharField(max_length=5, null=False)
    bulan = models.CharField(max_length=10, null=False)
    nilai = models.FloatField(null=True)
    berat = models.FloatField(null=True)
    post = models.ForeignKey(table_post_description, on_delete=models.CASCADE, default = 0)

    def __str__(self): return self.bulan

    class meta :
        db_table = "nilai_import"


class regresi_korelasi(models.Model):
    tahun = models.CharField(max_length=5, null = False)
    hasil_regresi_a = models.FloatField(null=True)
    hasil_regresi_b = models.FloatField(null=True)
    hasil_korelasi = models.FloatField()
    post = models.ForeignKey(table_post_description, on_delete=models.CASCADE, default=0)