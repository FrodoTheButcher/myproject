# Generated by Django 4.1.5 on 2023-03-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gradinita_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kids",
            name="age",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="kids",
            name="group",
            field=models.CharField(default="none", max_length=10),
        ),
        migrations.AlterField(
            model_name="kids",
            name="last_name",
            field=models.CharField(default="None", max_length=100),
        ),
        migrations.AlterField(
            model_name="kids",
            name="name",
            field=models.CharField(default="none", max_length=100),
        ),
    ]
