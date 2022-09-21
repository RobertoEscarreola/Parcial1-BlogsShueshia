# Generated by Django 4.1.1 on 2022-09-17 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0015_rename_name_reviewanime_namer_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviewanime",
            name="review",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="animerevs",
                to="main.anime",
            ),
        ),
        migrations.AlterField(
            model_name="reviewmanga",
            name="review",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mangarevs",
                to="main.manga",
            ),
        ),
    ]
