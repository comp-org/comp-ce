# Generated by Django 2.1.7 on 2019-03-28 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0002_auto_20190319_0944")]

    operations = [
        migrations.AddField(
            model_name="project",
            name="oneliner",
            field=models.CharField(
                default="Oneliner is a new field. Projects should fill it in.",
                max_length=10000,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.CharField(max_length=10000),
        ),
    ]
