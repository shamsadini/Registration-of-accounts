# accounting/models.py

from django.db import models
from django_jalali.db import models as jmodels

# مدل دریافت وجه
class Payment(models.Model):
    invoice_number = models.AutoField(primary_key=True)
    register_date = jmodels.jDateField(auto_now_add=True, verbose_name='تاریخ ثبت')
    image = models.ImageField(upload_to='payments/', verbose_name='تصویر')
    project_name = models.CharField(max_length=200, verbose_name='نام پروژه')
    payment_date = jmodels.jDateField(verbose_name='تاریخ دریافت وجه')
    payment_type = models.CharField(
        max_length=50,
        choices=[('تنخواه', 'تنخواه'), ('حقوق', 'حقوق'), ('سایر', 'سایر')],
        verbose_name='نوع دریافت'
    )
    payment_method = models.CharField(
        max_length=50,
        choices=[('نقد', 'نقد'), ('چک', 'چک')],
        verbose_name='نوع پرداخت'
    )

    # فیلدهای نقد
    cash_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='مبلغ دریافتی')
    cash_receiver_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='نام دریافت کننده')
    cash_description = models.TextField(blank=True, null=True, verbose_name='توضیحات')

    # فیلدهای چک
    check_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='مبلغ دریافتی')
    check_payer_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='نام پرداخت کننده')
    check_account = models.CharField(max_length=200, blank=True, null=True, verbose_name='طرف حساب')
    check_date = jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ چک')
    check_number = models.CharField(max_length=50, blank=True, null=True, verbose_name='شماره چک')
    bank_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='نام بانک')
    check_description = models.TextField(blank=True, null=True, verbose_name='توضیحات')

    class Meta:
        verbose_name = 'دریافت وجه'
        verbose_name_plural = 'دریافت وجه‌ها'

    def __str__(self):
        return f'Payment {self.invoice_number} - {self.project_name}'

# مدل پرداخت وجه
class Expense(models.Model):
    invoice_number = models.AutoField(primary_key=True)
    register_date = jmodels.jDateField(auto_now_add=True, verbose_name='تاریخ ثبت')
    image = models.ImageField(upload_to='expenses/', verbose_name='تصویر')
    project_name = models.CharField(max_length=200, verbose_name='نام پروژه')
    expense_date = jmodels.jDateField(verbose_name='تاریخ پرداخت وجه')
    expense_type = models.CharField(
        max_length=50,
        choices=[('تنخواه', 'تنخواه'), ('چک', 'چک'), ('سایر', 'سایر')],
        verbose_name='نوع پرداخت'
    )
    expense_method = models.CharField(
        max_length=50,
        choices=[('نقد', 'نقد'), ('چک', 'چک')],
        verbose_name='نوع پرداخت'
    )

    # فیلدهای نقد
    cash_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='مبلغ پرداختی')
    cash_payer_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='نام پرداخت کننده')
    cash_account = models.CharField(max_length=200, blank=True, null=True, verbose_name='طرف حساب')
    cash_description = models.TextField(blank=True, null=True, verbose_name='توضیحات')

    # فیلدهای چک
    check_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='مبلغ پرداختی')
    check_payer_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='نام پرداخت کننده')
    check_account = models.CharField(max_length=200, blank=True, null=True, verbose_name='طرف حساب')
    check_date = jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ چک')
    check_number = models.CharField(max_length=50, blank=True, null=True, verbose_name='شماره چک')
    bank_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='نام بانک')
    check_description = models.TextField(blank=True, null=True, verbose_name='توضیحات')

    class Meta:
        verbose_name = 'پرداخت وجه'
        verbose_name_plural = 'پرداخت وجه‌ها'

    def __str__(self):
        return f'Expense {self.invoice_number} - {self.project_name}'

# مدل صورت وضعیت
class Statement(models.Model):
    invoice_number = models.AutoField(primary_key=True)
    register_date = jmodels.jDateField(auto_now_add=True, verbose_name='تاریخ ثبت')
    image = models.ImageField(upload_to='statements/', verbose_name='تصویر')
    project_name = models.CharField(max_length=200, verbose_name='نام پروژه')
    statement_date = jmodels.jDateField(verbose_name='تاریخ صورت وضعیت')
    contractor_name = models.CharField(max_length=200, verbose_name='نام پیمانکار')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='مبلغ')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')

    class Meta:
        verbose_name = 'صورت وضعیت'
        verbose_name_plural = 'صورت وضعیت‌ها'

    def __str__(self):
        return f'Statement {self.invoice_number} - {self.project_name}'

# مدل فاکتور
class Invoice(models.Model):
    invoice_number = models.AutoField(primary_key=True)
    register_date = jmodels.jDateField(auto_now_add=True, verbose_name='تاریخ ثبت')
    image = models.ImageField(upload_to='invoices/', verbose_name='تصویر')
    project_name = models.CharField(max_length=200, verbose_name='نام پروژه')
    invoice_date = jmodels.jDateField(verbose_name='تاریخ فاکتور')
    account = models.CharField(max_length=200, verbose_name='طرف حساب')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='مبلغ')
    invoice_reference = models.CharField(max_length=200, verbose_name='شماره فاکتور')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')

    class Meta:
        verbose_name = 'فاکتور'
        verbose_name_plural = 'فاکتورها'

    def __str__(self):
        return f'Invoice {self.invoice_number} - {self.project_name}'

# مدل کرایه‌ها
class Rent(models.Model):
    invoice_number = models.AutoField(primary_key=True)
    register_date = jmodels.jDateField(auto_now_add=True, verbose_name='تاریخ ثبت')
    image = models.ImageField(upload_to='rents/', verbose_name='تصویر')
    rent_date = jmodels.jDateField(verbose_name='تاریخ پرداخت')
    payment_source = models.CharField(
        max_length=50,
        choices=[('تنخواه نقدی', 'تنخواه نقدی'), ('چک', 'چک'), ('سایر', 'سایر')],
        verbose_name='منبع پرداخت'
    )
    payer_name = models.CharField(max_length=200, verbose_name='نام پرداخت کننده')
    account = models.CharField(max_length=200, verbose_name='طرف حساب')
    origin = models.CharField(max_length=200, verbose_name='مبدا')
    destination = models.CharField(max_length=200, verbose_name='مقصد')
    project_name = models.CharField(max_length=200, verbose_name='نام پروژه')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='مبلغ')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')

    class Meta:
        verbose_name = 'کرایه'
        verbose_name_plural = 'کرایه‌ها'

    def __str__(self):
        return f'Rent {self.invoice_number} - {self.project_name}'
