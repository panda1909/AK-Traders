# Generated by Django 3.1 on 2021-03-16 12:19

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210316_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=128)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Product', models.CharField(max_length=128)),
                ('Quantity', models.PositiveIntegerField()),
                ('Description', models.TextField(max_length=5000)),
            ],
        ),
    ]