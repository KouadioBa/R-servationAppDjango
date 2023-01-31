# Generated by Django 4.1.5 on 2023-01-24 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Classes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("entite", models.CharField(max_length=200)),
                ("classe", models.CharField(max_length=200)),
                ("motif", models.CharField(max_length=200)),
                ("date", models.DateField(max_length=200)),
                ("heure", models.CharField(max_length=200)),
                ("intervenant", models.TextField(max_length=200)),
                ("matiere", models.TextField(max_length=200)),
                ("salle", models.CharField(max_length=200)),
            ],
        ),
    ]