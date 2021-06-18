# Generated by Django 3.2.4 on 2021-06-17 16:31

import CT_LIS.models
import CT_LIS.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CTLungInfectionSegmentation',
            fields=[
                ('patient_id', models.CharField(blank=True, max_length=64, null=True)),
                ('patient_sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], default='U', max_length=1)),
                ('patient_age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=CT_LIS.models.get_file_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['zip']), CT_LIS.validators.validate_file_size])),
                ('upper_left', models.FloatField(blank=True, null=True, validators=[CT_LIS.validators.validate_involvement])),
                ('upper_right', models.FloatField(blank=True, null=True, validators=[CT_LIS.validators.validate_involvement])),
                ('lower_left', models.FloatField(blank=True, null=True, validators=[CT_LIS.validators.validate_involvement])),
                ('lower_middle', models.FloatField(blank=True, null=True, validators=[CT_LIS.validators.validate_involvement])),
                ('lower_right', models.FloatField(blank=True, null=True, validators=[CT_LIS.validators.validate_involvement])),
                ('report', models.TextField(blank=True, max_length=10000, null=True)),
                ('prescriber', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]