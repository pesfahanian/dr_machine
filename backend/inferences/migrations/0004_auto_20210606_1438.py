# Generated by Django 3.2.3 on 2021-06-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inferences', '0003_auto_20210606_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chestxrayinference',
            name='patient_birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='covidctinference',
            name='patient_birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]