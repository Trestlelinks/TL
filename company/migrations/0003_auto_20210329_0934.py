# Generated by Django 3.1.7 on 2021-03-29 16:34

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('company', '0002_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='benchresource',
            name='fullname',
        ),
        migrations.AddField(
            model_name='benchresource',
            name='contractedtocompany',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contractedto', to='company.company'),
        ),
        migrations.AddField(
            model_name='benchresource',
            name='currentlocation',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='benchresource',
            name='description',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='benchresource',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='benchresource',
            name='employedtocompany',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employedto', to='company.company'),
        ),
        migrations.AddField(
            model_name='benchresource',
            name='firstname',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='benchresource',
            name='lastname',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='benchresource',
            name='primaryskills',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='benchresource',
            name='ratecard',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='benchresource',
            name='secondaryskills',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='benchresource',
            name='totalexperience',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='companyemail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='companyphonenumber',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='dateofregistration',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='numberofemployees',
            field=models.CharField(choices=[('1', 'less than 10'), ('2', '20-100'), ('3', '100-1000'), ('4', '1000-5000'), ('5', 'more than 5000')], default='1000-5000', max_length=32),
        ),
        migrations.AlterField(
            model_name='benchresource',
            name='mobile',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='companyname',
            field=models.CharField(max_length=256),
        ),
        migrations.CreateModel(
            name='Companyuser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('description', models.CharField(max_length=256)),
                ('mobilenumber', models.CharField(max_length=256)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
