# Generated by Django 3.1.13 on 2021-11-24 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0010_auto_20211122_0730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agentdetail',
            old_name='agend_id',
            new_name='agent_id',
        ),
    ]
