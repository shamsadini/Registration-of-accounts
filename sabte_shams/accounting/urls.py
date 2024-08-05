# accounting/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('payments/', views.payment_list, name='payment_list'),
    path('payments/new/', views.payment_create, name='payment_create'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/new/', views.expense_create, name='expense_create'),
    path('statements/', views.statement_list, name='statement_list'),
    path('statements/new/', views.statement_create, name='statement_create'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/new/', views.invoice_create, name='invoice_create'),
    path('rents/', views.rent_list, name='rent_list'),
    path('rents/new/', views.rent_create, name='rent_create'),
]



# Api

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, ExpenseViewSet, StatementViewSet, InvoiceViewSet, RentViewSet

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'statements', StatementViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'rents', RentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
