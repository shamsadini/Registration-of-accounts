# accounting/tests.py

from django.test import TestCase
from .models import Payment, Expense, Statement, Invoice, Rent
from django.utils import timezone

class PaymentModelTest(TestCase):
    def setUp(self):
        self.payment = Payment.objects.create(
            project_name="Test Project",
            payment_date=timezone.now(),
            payment_type="تنخواه",
            payment_method="نقد",
            cash_amount=1000,
            cash_receiver_name="Test Receiver",
            cash_description="Test Description"
        )

    def test_payment_creation(self):
        self.assertTrue(isinstance(self.payment, Payment))
        self.assertEqual(self.payment.__str__(), f'Payment {self.payment.invoice_number} - {self.payment.project_name}')

class ExpenseModelTest(TestCase):
    def setUp(self):
        self.expense = Expense.objects.create(
            project_name="Test Project",
            expense_date=timezone.now(),
            expense_type="چک",
            expense_method="نقد",
            cash_amount=2000,
            cash_payer_name="Test Payer",
            cash_account="Test Account",
            cash_description="Test Expense Description"
        )

    def test_expense_creation(self):
        self.assertTrue(isinstance(self.expense, Expense))
        self.assertEqual(self.expense.__str__(), f'Expense {self.expense.invoice_number} - {self.expense.project_name}')

class StatementModelTest(TestCase):
    def setUp(self):
        self.statement = Statement.objects.create(
            project_name="Test Project",
            statement_date=timezone.now(),
            contractor_name="Test Contractor",
            amount=3000,
            description="Test Statement Description"
        )

    def test_statement_creation(self):
        self.assertTrue(isinstance(self.statement, Statement))
        self.assertEqual(self.statement.__str__(), f'Statement {self.statement.invoice_number} - {self.statement.project_name}')

class InvoiceModelTest(TestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create(
            project_name="Test Project",
            invoice_date=timezone.now(),
            account="Test Account",
            amount=4000,
            invoice_reference="INV-001",
            description="Test Invoice Description"
        )

    def test_invoice_creation(self):
        self.assertTrue(isinstance(self.invoice, Invoice))
        self.assertEqual(self.invoice.__str__(), f'Invoice {self.invoice.invoice_number} - {self.invoice.project_name}')

class RentModelTest(TestCase):
    def setUp(self):
        self.rent = Rent.objects.create(
            project_name="Test Project",
            rent_date=timezone.now(),
            payment_source="تنخواه نقدی",
            payer_name="Test Payer",
            account="Test Account",
            origin="Test Origin",
            destination="Test Destination",
            amount=5000,
            description="Test Rent Description"
        )

    def test_rent_creation(self):
        self.assertTrue(isinstance(self.rent, Rent))
        self.assertEqual(self.rent.__str__(), f'Rent {self.rent.invoice_number} - {self.rent.project_name}')
