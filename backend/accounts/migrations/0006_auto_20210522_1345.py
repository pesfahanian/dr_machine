# Generated by Django 3.2.3 on 2021-05-22 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='medical_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='national_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
