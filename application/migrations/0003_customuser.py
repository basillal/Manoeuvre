# Generated by Django 4.2.4 on 2023-09-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_coding_details_gaming_details_hackathon_details_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, null=True)),
                ('team_name', models.CharField(max_length=100, null=True)),
                ('team_leader1', models.CharField(max_length=50, null=True)),
                ('team_leader2', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50)),
                ('is_team', models.BooleanField(default=False)),
                ('is_oncontrol', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
