# Generated by Django 4.2.2 on 2023-06-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0006_accessoriesbrid_accessoriescats_accessoriesdogs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessoriesdogs',
            name='price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='accessoriesdogs',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='accessories',
            field=models.CharField(max_length=50),
        ),
    ]
