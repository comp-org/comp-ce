# Generated by Django 3.0.3 on 2020-05-22 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0013_project_latest_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="staging_tag",
            field=models.CharField(max_length=64, null=True),
        ),
    ]
