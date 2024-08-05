# accounting/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .forms import PaymentForm, ExpenseForm, StatementForm, InvoiceForm, RentForm
from .models import Payment, Expense, Statement, Invoice, Rent

# ویوی مربوط به فرم دریافت وجه
def payment_create(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'accounting/payment_form.html', {'form': form})

# ویوی مربوط به لیست دریافت وجه
def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'accounting/payment_list.html', {'payments': payments})

# ویوی مربوط به فرم پرداخت وجه
def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'accounting/expense_form.html', {'form': form})

# ویوی مربوط به لیست پرداخت وجه
def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'accounting/expense_list.html', {'expenses': expenses})

# ویوی مربوط به فرم صورت وضعیت
def statement_create(request):
    if request.method == 'POST':
        form = StatementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('statement_list')
    else:
        form = StatementForm()
    return render(request, 'accounting/statement_form.html', {'form': form})

# ویوی مربوط به لیست صورت وضعیت
def statement_list(request):
    statements = Statement.objects.all()
    return render(request, 'accounting/statement_list.html', {'statements': statements})

# ویوی مربوط به فرم فاکتور
def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'accounting/invoice_form.html', {'form': form})

# ویوی مربوط به لیست فاکتور
def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'accounting/invoice_list.html', {'invoices': invoices})

# ویوی مربوط به فرم کرایه
def rent_create(request):
    if request.method == 'POST':
        form = RentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('rent_list')
    else:
        form = RentForm()
    return render(request, 'accounting/rent_form.html', {'form': form})

# ویوی مربوط به لیست کرایه
def rent_list(request):
    rents = Rent.objects.all()
    return render(request, 'accounting/rent_list.html', {'rents': rents})



# accounting/views.py

from rest_framework import viewsets
from .models import Payment, Expense, Statement, Invoice, Rent
from .serializers import PaymentSerializer, ExpenseSerializer, StatementSerializer, InvoiceSerializer, RentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class StatementViewSet(viewsets.ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
