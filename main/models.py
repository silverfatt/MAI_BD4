from django.db import models


class Firm(models.Model):
    firm_name = models.CharField(max_length=50, primary_key=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.firm_name

    class Meta:
        verbose_name = 'Фирма'
        verbose_name_plural = 'Фирмы'


class Form(models.Model):
    form_name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.form_name

    class Meta:
        verbose_name = 'Форма выпуска'
        verbose_name_plural = 'Формы выпуска'



class MedsList(models.Model):
    med_name = models.CharField(max_length=50, unique=True)
    prescription = models.BooleanField()
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.med_name

    class Meta:
        verbose_name = 'Список лекарств'
        verbose_name_plural = 'Списки лекарств'


class Med(models.Model):
    med_firm_name = models.ForeignKey(Firm, on_delete=models.CASCADE)
    med_form_name = models.ForeignKey(Form, on_delete=models.CASCADE)
    med_name = models.ForeignKey(MedsList, to_field='med_name', db_column='med_name', on_delete=models.CASCADE)

    def __str__(self):
        return self.med_name.med_name

    class Meta:
        verbose_name = 'Лекарство'
        verbose_name_plural = 'Лекарства'


class Prescription(models.Model):
    med_id = models.ForeignKey(Med, on_delete=models.CASCADE)
    prescription_number = models.IntegerField()
    patient_full_name = models.CharField(max_length=60)
    med_policy = models.IntegerField()
    release_date = models.DateField()
    amount = models.IntegerField()

    def __str__(self):
        return str(self.prescription_number) + '-' + self.patient_full_name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
