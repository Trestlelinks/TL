# Generated by Django 3.1.7 on 2021-04-03 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20210403_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyuser',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]
