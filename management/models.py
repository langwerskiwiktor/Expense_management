from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description} - {self.amount} USD"


class Budget(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.amount} USD"


class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description} - {self.amount} USD"


class PaymentMethod(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Savings(models.Model):
    goal_name = models.CharField(max_length=255)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.goal_name} - {self.current_amount}/{self.goal_amount} USD"
