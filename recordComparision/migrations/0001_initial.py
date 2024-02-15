# Generated by Django 4.1.2 on 2024-02-15 07:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("answerOfQuestions", "0001_initial"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TotalRecordsComparisonModel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("total_points", models.IntegerField(default=0)),
                ("is_match", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_deleted", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "female_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="female_user",
                        to="user.usermodel",
                    ),
                ),
                (
                    "male_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="male_user",
                        to="user.usermodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ComparingRecordsAnswerWiseModel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("total_points", models.IntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                ("is_deleted", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "female_answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="answerOfQuestions.answersoffemalesmodel",
                    ),
                ),
                (
                    "male_answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="answerOfQuestions.answersofmalesmodel",
                    ),
                ),
            ],
        ),
    ]
