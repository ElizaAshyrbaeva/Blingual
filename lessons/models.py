from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Word(models.Model):
    english = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    example = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="words", null=True, blank=True)

    def __str__(self):
        return f"{self.english} - {self.translation}"


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    words = models.ManyToManyField(Word, related_name="lessons")

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)
    favorite_words = models.ManyToManyField(Word, blank=True)

    def __str__(self):
        return self.user.username


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
