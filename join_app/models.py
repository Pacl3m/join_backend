from django.db import models


class Contact(models.Model):
    color = models.CharField(max_length=20)  # Farbe
    email = models.EmailField(max_length=150)  # E-Mail-Adresse
    firstLetters = models.CharField(max_length=3)  # Initialen (z.B. "JH")
    firstName = models.CharField(max_length=50)  # Vorname
    lastName = models.CharField(max_length=50)  # Nachname
    name = models.CharField(max_length=100)  # Vollständiger Name
    password = models.CharField(max_length=100)  # Passwort
    phone = models.CharField(max_length=20)  # Telefonnummer

    def __str__(self):
        return self.name



class Card(models.Model):
    assignedUser = models.JSONField()  # JSONField für die Liste der Benutzernamen (z.B. "JH", "TN")
    assignedUserFullName = models.JSONField()  # JSONField für die vollständigen Namen der Benutzer
    category = models.CharField(max_length=100)  # Kategorie der Aufgabe (z.B. "Generator")
    description = models.TextField()  # Beschreibung der Aufgabe
    dueDate = models.DateField()  # Fälligkeitsdatum (z.B. "2025-03-31")
    listType = models.CharField(max_length=50)  # Typ der Liste (z.B. "ToDo")
    prio = models.CharField(max_length=20)  # Priorität der Aufgabe (z.B. "Urgent")
    progress = models.IntegerField(default=0)  # Fortschritt der Aufgabe (0 bis 100)
    subtasks = models.JSONField(default=list)  # Unteraufgaben als JSON-Array
    title = models.CharField(max_length=200)  # Titel der Aufgabe

    def __str__(self):
        return self.title


class Category(models.Model):
    color = models.CharField(max_length=7)  # Farbe im Hex-Format (z.B. "#FFC701")
    name = models.CharField(max_length=100)  # Name der Kategorie (z.B. "Generator")
    value = models.CharField(max_length=100)  # Wert der Kategorie (z.B. "generator")

    def __str__(self):
        return self.name
