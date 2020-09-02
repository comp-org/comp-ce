# Generated by Django 3.0.9 on 2020-08-27 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0025_auto_20200826_1400"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cluster",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField(max_length=64)),
                ("access_token", models.CharField(max_length=128, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("deleted_at", models.DateTimeField(null=True)),
                (
                    "service_account",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="users.Profile",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="cluster",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="projects",
                to="users.Cluster",
            ),
        ),
    ]
