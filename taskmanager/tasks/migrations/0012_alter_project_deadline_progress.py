# Generated by Django 4.2 on 2023-04-30 10:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0011_alter_project_deadline_alter_task_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="deadline",
            field=models.DateField(
                verbose_name=datetime.datetime(
                    2023, 4, 30, 10, 13, 2, 565899, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.CreateModel(
            name="Progress",
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
                ("percentage", models.PositiveIntegerField(default=0)),
                (
                    "hours_spent",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "date",
                    models.DateField(
                        default=datetime.datetime(
                            2023, 4, 30, 10, 13, 2, 568605, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tasks.task"
                    ),
                ),
            ],
        ),
    ]
