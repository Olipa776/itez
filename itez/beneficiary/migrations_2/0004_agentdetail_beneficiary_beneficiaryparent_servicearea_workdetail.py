# Generated by Django 3.1.13 on 2021-11-05 19:47

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0003_auto_20211102_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Second Name')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('agend_ID', models.CharField(default='B314760', max_length=100, verbose_name='Agent Id')),
                ('gender', models.CharField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Transgender'), (4, 'Other')], default=4, max_length=50, verbose_name='Gender')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326, verbose_name='Location')),
            ],
        ),
        migrations.CreateModel(
            name='BeneficiaryParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_first_name', models.CharField(max_length=200, verbose_name='Father First Name')),
                ('father_last_name', models.CharField(max_length=200, verbose_name='Father Last Name')),
                ('mother_first_name', models.CharField(max_length=200, verbose_name='Mother First Name')),
                ('mother_last_name', models.CharField(max_length=200, verbose_name='Mother Last Name')),
                ('address', models.TextField(blank=True, max_length=300, null=True)),
                ('father_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('mother_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('father_date_of_birth', models.DateField(blank=True, null=True, verbose_name="Father's date of birth")),
                ('mother_date_of_birth', models.DateField(blank=True, null=True, verbose_name="Mother's date of birth")),
                ('father_village', models.CharField(blank=True, max_length=200, null=True, verbose_name="Father's Village")),
                ('mother_village', models.CharField(blank=True, max_length=200, null=True, verbose_name="Mother's Village")),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gross_pay', models.DecimalField(decimal_places=2, max_digits=1000, verbose_name='Monthly Salary')),
                ('company', models.CharField(max_length=200, verbose_name='Company Name')),
                ('insured', models.BooleanField(default=False, verbose_name='Company Insured')),
                ('work_address', models.TextField(blank=True, null=True, verbose_name='Work Address')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Service Area')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='beneficiary.district')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('other_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Other Name')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=100, verbose_name='Gender')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photo/', verbose_name='Profile Photo')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('beneficiary_ID', models.UUIDField(default=uuid.UUID('7e4d2dad-4066-4394-bca7-786afbc3b7aa'), editable=False)),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('seperated', 'Seperated'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], max_length=100, verbose_name='Marital Status')),
                ('name_of_spouse', models.CharField(blank=True, max_length=200, null=True, verbose_name='Phone Number')),
                ('number_of_children', models.IntegerField(blank=True, null=True, verbose_name='Number of children')),
                ('number_of_siblings', models.IntegerField(blank=True, null=True, verbose_name='Number of siblings')),
                ('education_level', models.CharField(blank=True, choices=[('none', 'None'), ('primary', 'Primary'), ('basic', 'Basic'), ('secondary', "Secondary O'Level"), ('certificate', 'Certificate'), ('diploma', 'Diploma'), ('degree', 'Degree'), ('masters', 'Masters'), ('doctrate', 'Doctrate'), ('phd', 'PHD')], max_length=300, null=True, verbose_name='Education level')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('agent_ID', models.ForeignKey(default='7395A44', on_delete=django.db.models.deletion.PROTECT, to='beneficiary.agentdetail')),
                ('parent_details', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='beneficiary.beneficiaryparent')),
            ],
            options={
                'verbose_name': 'Beneficiary',
                'verbose_name_plural': 'Beneficiaries',
                'ordering': ['created'],
            },
        ),
    ]