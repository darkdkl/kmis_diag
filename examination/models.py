from django.db import models


class Device(models.Model):
    device_id = models.IntegerField(verbose_name="Идентификатор оборудования")
    name = models.CharField(max_length=50, verbose_name=" Наименование оборудования")

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"

    def __str__(self):
        return self.name


class Diagnostics(models.Model):

    name = models.CharField(max_length=250, verbose_name="ФИО Пациента")
    date = models.CharField(max_length=50, verbose_name="Дата")
    device = models.ForeignKey(Device, related_name='diagnostics',
                               verbose_name="Данные диагностич оборудования", on_delete=models.CASCADE)
    description = models.CharField(max_length=100, verbose_name="Название процедуры")
    conclusion = models.TextField(max_length=500, verbose_name="Заключение врача")
    file = models.TextField(verbose_name="Файл", blank=True)
    file_md5 = models.CharField(max_length=60, verbose_name="Хеш", blank=True)
    
    class Meta:
        verbose_name = "Диагностика"
        verbose_name_plural = "Диагностика"

    def __str__(self):
        return self.name


class Result (models.Model):
    heart_rate = models.IntegerField(verbose_name="Частота сердцебиения")
    bp_syst = models.IntegerField(verbose_name="Систолическое давление")
    bp_diast = models.IntegerField(verbose_name="Диастолическое давление")
    diagnostics = models.ForeignKey("Diagnostics",related_name='results', on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"

    def __str__(self):
        return f'{self.heart_rate} уд/м,{self.bp_syst}/{self.bp_diast} мм/рт.ст'
