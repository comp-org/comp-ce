# Generated by Django 3.0.3 on 2020-06-16 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0014_project_staging_tag"),
    ]

    operations = [
        migrations.RemoveField(model_name="project", name="server_cost",),
    ]