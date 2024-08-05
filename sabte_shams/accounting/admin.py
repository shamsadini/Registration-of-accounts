# accounting/admin.py

from django.contrib import admin
from .models import Payment, Expense, Statement, Invoice, Rent

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'register_date', 'project_name', 'payment_date', 'payment_type', 'payment_method')
    list_filter = ('payment_type', 'payment_method')
    search_fields = ('invoice_number', 'project_name')
    readonly_fields = ('register_date',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'register_date', 'project_name', 'expense_date', 'expense_type', 'expense_method')
    list_filter = ('expense_type', 'expense_method')
    search_fields = ('invoice_number', 'project_name')
    readonly_fields = ('register_date',)

@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'register_date', 'project_name', 'statement_date', 'contractor_name', 'amount')
    list_filter = ('statement_date',)
    search_fields = ('invoice_number', 'project_name', 'contractor_name')
    readonly_fields = ('register_date',)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'register_date', 'project_name', 'invoice_date', 'account', 'amount', 'invoice_reference')
    list_filter = ('invoice_date',)
    search_fields = ('invoice_number', 'project_name', 'invoice_reference')
    readonly_fields = ('register_date',)

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'register_date', 'project_name', 'rent_date', 'payment_source', 'payer_name', 'amount')
    list_filter = ('payment_source',)
    search_fields = ('invoice_number', 'project_name', 'payer_name')
    readonly_fields = ('register_date',)
