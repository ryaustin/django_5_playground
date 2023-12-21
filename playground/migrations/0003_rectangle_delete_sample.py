# Generated by Django 5.0 on 2023-12-20 20:35

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_sample_base'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rectangle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.FloatField()),
                ('height', models.FloatField()),
                ('area', models.GeneratedField(db_persist=True, expression=django.db.models.expressions.CombinedExpression(models.F('base'), '*', models.F('height')), output_field=models.FloatField())),
            ],
        ),
        migrations.DeleteModel(
            name='Sample',
        ),
    ]
