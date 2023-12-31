# Generated by Django 4.2.6 on 2023-11-08 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_alter_group_sub_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='authority',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='major',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Profile.studentmajor'),
        ),
    ]
