# Generated by Django 3.1.8 on 2021-04-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('url', 'URL')], max_length=16, verbose_name='Field Type'),
        ),
    ]
