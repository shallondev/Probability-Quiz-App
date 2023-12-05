from django.contrib.auth.models import AbstractUser
from django.db import models

OPTION_CHOICES = [
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
        ('E', 'Option E'),
    ]

class User(AbstractUser):
    pass

class Question(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    context = models.TextField()
    correct_response = models.CharField(max_length=1, choices=OPTION_CHOICES)
    solution = models.TextField(null=True, blank=True)

class Test(models.Model):
    test_size = models.PositiveIntegerField(default=30)
    time = models.PositiveIntegerField(default=180)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Assuming score as a percentage
    show_repeats = models.BooleanField(default=False)
    show_only_wrong_questions = models.BooleanField(default=False)
    questions = models.ManyToManyField(Question, through='MarkedQuestion')

class MarkedQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    marked_date = models.DateTimeField(auto_now_add=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

class UserQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField()