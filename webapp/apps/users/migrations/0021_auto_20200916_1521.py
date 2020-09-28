# Generated by Django 3.0.10 on 2020-09-16 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0020_auto_20200911_1433"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={
                "permissions": (
                    (
                        "read_project",
                        "Users with this permission may view and run this project, even if it's private.",
                    ),
                    (
                        "write_project",
                        "Users with this permission may edit the project and view its usage statistics.",
                    ),
                    (
                        "admin_project",
                        "Users with this permission control the visibility of this project and who has read, write, and admin access to it.",
                    ),
                )
            },
        ),
    ]
