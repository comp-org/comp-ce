# Generated by Django 2.2.1 on 2019-06-06 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0005_project_repo_url")]

    operations = [
        migrations.AddField(
            model_name="project", name="listed", field=models.BooleanField(default=True)
        )
    ]
