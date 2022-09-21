# Generated by Django 4.1.1 on 2022-09-11 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_post_post_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.CharField(default="Blog", max_length=10),
        ),
    ]
