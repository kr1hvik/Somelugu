# Generated by Django 4.2.1 on 2023-05-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tekst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dokument', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
