# Generated by Django 4.2.7 on 2023-11-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(help_text='Insert a valid email', max_length=254)),
                ('subject', models.CharField(choices=[('Inquiry', 'Inquiry'), ('Compliant', 'Complaint')], max_length=10)),
                ('message', models.TextField(max_length=7000)),
            ],
        ),
    ]