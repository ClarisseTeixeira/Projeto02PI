# Generated by Django 4.2.3 on 2023-07-18 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="imagem",
            field=models.ImageField(upload_to="image"),
        ),
    ]