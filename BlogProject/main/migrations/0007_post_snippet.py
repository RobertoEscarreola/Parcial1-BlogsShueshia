# Generated by Django 4.1.1 on 2022-09-11 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_alter_post_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="snippet",
            field=models.CharField(
                default="Presiona el link para leer el post!", max_length=30
            ),
        ),
    ]