# Generated by Django 2.2.4 on 2019-09-03 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('address', models.CharField(max_length=45)),
            ],
        ),
    ]
