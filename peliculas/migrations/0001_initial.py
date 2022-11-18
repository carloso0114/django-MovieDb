# Generated by Django 4.1.3 on 2022-11-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Pon el nombre del director', max_length=64)),
                ('fechaNacimiento', models.CharField(help_text='edad', max_length=32)),
            ],
        ),
    ]
