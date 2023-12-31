# Generated by Django 4.2.6 on 2023-11-08 20:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0005_alter_profile_authority_alter_profile_major'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnouncementPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=225, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='anouncement_images')),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('target_group', models.ManyToManyField(to='Profile.group')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Profile.profile')),
            ],
        ),
    ]
