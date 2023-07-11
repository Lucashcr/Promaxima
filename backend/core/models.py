# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Medicamentos(models.Model):
    principio_ativo = models.CharField()
    cnpj = models.CharField()
    laboratorio = models.CharField()
    ggrem = models.CharField()
    registro = models.CharField(blank=True, null=True)
    ean1 = models.CharField()
    ean2 = models.CharField(blank=True, null=True)
    ean3 = models.CharField(blank=True, null=True)
    produto = models.CharField()
    apresentacao = models.CharField()
    classe_terapeutica = models.CharField()
    tipo_produto = models.CharField(blank=True, null=True)
    regime_preco = models.CharField()
    pf_sem_impostos = models.FloatField()
    pf_0 = models.FloatField(blank=True, null=True)
    pf_12 = models.FloatField(blank=True, null=True)
    pf_17 = models.FloatField(blank=True, null=True)
    pf_17_alc = models.FloatField(blank=True, null=True)
    pf_17_5 = models.FloatField(blank=True, null=True)
    pf_17_5_alc = models.FloatField(blank=True, null=True)
    pf_18 = models.FloatField(blank=True, null=True)
    pf_18_alc = models.FloatField(blank=True, null=True)
    pf_19 = models.FloatField(blank=True, null=True)
    pf_20 = models.FloatField(blank=True, null=True)
    pf_21 = models.FloatField(blank=True, null=True)
    pf_22 = models.FloatField(blank=True, null=True)
    pmvg_sem_impostos = models.FloatField(blank=True, null=True)
    pmvg_0 = models.FloatField(blank=True, null=True)
    pmvg_12 = models.FloatField(blank=True, null=True)
    pmvg_17 = models.FloatField(blank=True, null=True)
    pmvg_17_alc = models.FloatField(blank=True, null=True)
    pmvg_17_5 = models.FloatField(blank=True, null=True)
    pmvg_17_5_alc = models.FloatField(blank=True, null=True)
    pmvg_18 = models.FloatField(blank=True, null=True)
    pmvg_18_alc = models.FloatField(blank=True, null=True)
    pmvg_19 = models.FloatField(blank=True, null=True)
    pmvg_20 = models.FloatField(blank=True, null=True)
    pmvg_21 = models.FloatField(blank=True, null=True)
    pmvg_22 = models.FloatField(blank=True, null=True)
    restricao_hospitalar = models.BooleanField()
    cap = models.BooleanField()
    confaz_87 = models.BooleanField()
    icms_0 = models.BooleanField()
    analise_recursal = models.TextField(blank=True, null=True)  # This field type is a guess.
    lista_ctributario = models.TextField()  # This field type is a guess.
    comercializacao = models.BooleanField()
    tarja = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicamentos'
