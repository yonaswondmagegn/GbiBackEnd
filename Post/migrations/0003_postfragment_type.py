# Generated by Django 4.2.6 on 2023-12-09 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_postfragment_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='postfragment',
            name='type',
            field=models.CharField(choices=[('N', 'NORMAL'), ('C', 'CLOT')], default='N', max_length=1),
        ),
    ]
