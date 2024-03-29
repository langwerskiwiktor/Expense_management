import pytest
from django.test import Client
from django.contrib.auth.models import User, Group
from mixer.backend.django import mixer
from management.models import UserProfile, Category, Expense, Budget, Income, PaymentMethod, Savings
from account.forms import LoginForm, RegisterForm, GroupPermissionAddForm
from .models import Income, PaymentMethod, Expense



@pytest.fixture
def user():
    user = User.objects.create_user(username='test_user', email='test@example.com', password='test_password')
    return user


@pytest.fixture
def user_profile(user):
    user_profile = UserProfile.objects.create(user=user)
    return user_profile


@pytest.fixture
def category():
    category = Category.objects.create(name='Test Category', total_amount=100)
    return category


@pytest.fixture
def expense(category):
    expense = Expense.objects.create(amount=50, description='Test Expense', category=category)
    return expense


@pytest.fixture
def budget(user_profile, category):
    budget = Budget.objects.create(name='Test Budget', user=user_profile, amount=200)
    budget.categories.add(category)
    return budget


@pytest.fixture
def income(user_profile):
    income = Income.objects.create(amount=500, description='Test Income', date='2024-02-08', user=user_profile)
    return income


@pytest.fixture
def payment_method(category):
    payment_method = PaymentMethod.objects.create(name='Test Payment Method')
    payment_method.categories.add(category)
    return payment_method


@pytest.fixture
def savings(user_profile):
    savings = Savings.objects.create(goal_name='Test Savings Goal', goal_amount=1000, current_amount=500,
                                     user=user_profile)
    return savings


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(username='testuser', password='testpassword')


@pytest.fixture
def logged_in_user(client, user):
    client.force_login(user)
    return user


@pytest.fixture
def group():
    return Group.objects.create(name='testgroup')


@pytest.fixture
def user():
    user = User.objects.create_user(username='testuser', password='testpassword')
    yield user
    user.delete()


@pytest.fixture
def authenticated_user():
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = Client()
    client.login(username='testuser', password='testpassword')
    yield client
    user.delete()


@pytest.fixture
def create_income():
    income = mixer.blend(Income)
    yield income
    income.delete()


@pytest.fixture
def create_payment_method():
    payment_method = mixer.blend(PaymentMethod)
    yield payment_method
    payment_method.delete()
