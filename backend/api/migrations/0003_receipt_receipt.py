# Generated by Django 4.0.2 on 2022-02-24 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_total_receipt_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='receipt',
            field=models.FileField(blank=True, null=True, upload_to='receipts'),
        ),
    ]