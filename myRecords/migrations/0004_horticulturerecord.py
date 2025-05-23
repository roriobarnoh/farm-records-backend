# Generated by Django 5.2 on 2025-05-02 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myRecords', '0003_cowrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorticultureRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_name', models.CharField(max_length=100)),
                ('crop_type', models.CharField(choices=[('Fruit', 'Fruit'), ('Vegetable', 'Vegetable'), ('Herb', 'Herb'), ('Flower', 'Flower'), ('Other', 'Other')], max_length=20)),
                ('planting_date', models.DateField()),
                ('harvest_date', models.DateField(blank=True, null=True)),
                ('quantity_harvested', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('unit', models.CharField(default='kg', max_length=20)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
    ]
