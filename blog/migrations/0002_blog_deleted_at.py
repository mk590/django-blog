# Generated by Django 4.1.1 on 2022-12-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]