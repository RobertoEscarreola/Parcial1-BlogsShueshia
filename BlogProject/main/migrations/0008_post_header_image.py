# Generated by Django 4.1.1 on 2022-09-11 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_post_snippet"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="header_image",
            field=models.ImageField(blank=True, null=True, upload_to="blog_images"),
        ),
    ]
