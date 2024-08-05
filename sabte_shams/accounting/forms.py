from django import forms
from persiantools.jdatetime import JalaliDate
from .models import Payment, Expense, Statement, Invoice, Rent

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'register_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'payment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cash_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'cash_receiver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cash_description': forms.Textarea(attrs={'class': 'form-control'}),
            'check_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'check_payer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'check_account': forms.TextInput(attrs={'class': 'form-control'}),
            'check_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'check_number': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'check_description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'invoice_number': 'شماره فاکتور',
            'register_date': 'تاریخ ثبت',
            'image': 'تصویر',
            'project_name': 'نام پروژه',
            'payment_date': 'تاریخ دریافت وجه',
            'payment_type': 'نوع دریافت',
            'payment_method': 'نوع پرداخت',
            'cash_amount': 'مبلغ دریافتی',
            'cash_receiver_name': 'نام دریافت کننده',
            'cash_description': 'توضیحات',
            'check_amount': 'مبلغ دریافتی',
            'check_payer_name': 'نام پرداخت کننده',
            'check_account': 'طرف حساب',
            'check_date': 'تاریخ چک',
            'check_number': 'شماره چک',
            'bank_name': 'نام بانک',
            'check_description': 'توضیحات',
        }
        help_texts = {
            'cash_amount': 'مبلغ دریافتی به‌صورت نقدی.',
            'check_amount': 'مبلغ دریافتی به‌صورت چک.',
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
            'register_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expense_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cash_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'cash_payer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cash_account': forms.TextInput(attrs={'class': 'form-control'}),
            'cash_description': forms.Textarea(attrs={'class': 'form-control'}),
            'check_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'check_payer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'check_account': forms.TextInput(attrs={'class': 'form-control'}),
            'check_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'check_number': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'check_description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'invoice_number': 'شماره فاکتور',
            'register_date': 'تاریخ ثبت',
            'image': 'تصویر',
            'project_name': 'نام پروژه',
            'expense_date': 'تاریخ پرداخت وجه',
            'expense_type': 'نوع پرداخت',
            'expense_method': 'نوع پرداخت',
            'cash_amount': 'مبلغ پرداختی',
            'cash_payer_name': 'نام پرداخت کننده',
            'cash_account': 'طرف حساب',
            'cash_description': 'توضیحات',
            'check_amount': 'مبلغ پرداختی',
            'check_payer_name': 'نام پرداخت کننده',
            'check_account': 'طرف حساب',
            'check_date': 'تاریخ چک',
            'check_number': 'شماره چک',
            'bank_name': 'نام بانک',
            'check_description': 'توضیحات',
        }
        help_texts = {
            'cash_amount': 'مبلغ پرداختی به‌صورت نقدی.',
            'check_amount': 'مبلغ پرداختی به‌صورت چک.',
        }

class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = '__all__'
        widgets = {
            'register_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'statement_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'invoice_number': 'شماره فاکتور',
            'register_date': 'تاریخ ثبت',
            'image': 'تصویر',
            'project_name': 'نام پروژه',
            'statement_date': 'تاریخ صورت وضعیت',
            'contractor_name': 'نام پیمانکار',
            'amount': 'مبلغ',
            'description': 'توضیحات',
        }

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        widgets = {
            'register_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'invoice_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'invoice_number': 'شماره فاکتور',
            'register_date': 'تاریخ ثبت',
            'image': 'تصویر',
            'project_name': 'نام پروژه',
            'invoice_date': 'تاریخ فاکتور',
            'account': 'طرف حساب',
            'amount': 'مبلغ',
            'invoice_reference': 'شماره فاکتور',
            'description': 'توضیحات',
        }

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = '__all__'
        widgets = {
            'register_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'rent_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'invoice_number': 'شماره فاکتور',
            'register_date': 'تاریخ ثبت',
            'image': 'تصویر',
            'rent_date': 'تاریخ پرداخت',
            'payment_source': 'منبع پرداخت',
            'payer_name': 'نام پرداخت کننده',
            'account': 'طرف حساب',
            'origin': 'مبدا',
            'destination': 'مقصد',
            'project_name': 'نام پروژه',
            'amount': 'مبلغ',
            'description': 'توضیحات',
        }
