# Generated by Django 3.1 on 2020-08-24 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0020_backupentry_safe_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]