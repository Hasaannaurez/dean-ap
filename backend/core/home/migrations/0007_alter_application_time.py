# Generated by Django 5.0.6 on 2024-06-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_application_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
