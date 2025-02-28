from django.db import models


class Contact(models.Model):
    color = models.CharField(max_length=20)  # Farbe
    email = models.EmailField(max_length=150)  # E-Mail-Adresse
    firstLetters = models.CharField(max_length=3)  # Initialen (z.B. "JH")
    firstName = models.CharField(max_length=50)  # Vorname
    lastName = models.CharField(max_length=50)  # Nachname
    name = models.CharField(max_length=100)  # Vollständiger Name
    phone = models.CharField(max_length=100)  # Telefonnummer

    def __str__(self):
        return self.name


class Card(models.Model):
    assignedUser = models.JSONField()
    assignedUserFullName = models.JSONField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    dueDate = models.DateField()
    listType = models.CharField(max_length=50)
    prio = models.CharField(max_length=20)
    progress = models.IntegerField(default=0)
    subtasks = models.JSONField(default=list)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Category(models.Model):
    color = models.CharField(max_length=7)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name
