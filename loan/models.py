from django.db import models
# Create your models here.

class Loan(models.Model):
    creditability = models.IntegerField()
    account_balance = models.IntegerField()
    duration = models.IntegerField()
    previous_credit_payment_status = models.IntegerField()
    purpose = models.IntegerField()
    credit_amount = models.IntegerField()
    value_savings = models.IntegerField()
    len_of_cur_employement = models.IntegerField()
    installment_percent = models.IntegerField()
    sex_marital_status = models.IntegerField()
    guarantors = models.IntegerField()
    duration_cur_addr = models.IntegerField()
    most_valuable_asset = models.IntegerField()
    age = models.IntegerField()
    concurrent_credits = models.IntegerField()
    type_of_appt = models.IntegerField()
    credit_this_bank = models.IntegerField()
    occupation = models.IntegerField()
    no_of_dependents = models.IntegerField()
    tel_no = models.IntegerField()
    foreign_worker = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Loan"