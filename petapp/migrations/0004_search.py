# Generated by Django 4.2.2 on 2023-06-12 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0003_doctorvent_alter_order_customer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boot', models.CharField(max_length=200)),
            ],
        ),
    ]
