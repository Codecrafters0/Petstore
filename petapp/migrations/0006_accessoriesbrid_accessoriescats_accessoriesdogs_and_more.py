# Generated by Django 4.2.2 on 2023-06-12 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0005_sidebar'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessoriesBrid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AccessoriesCats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AccessoriesDogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AccessoriesFish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BedsCats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BedsDogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Brid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessories', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='cats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessories', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessories', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessories', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FleaTicksCats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('cats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flea_ticks_cats', to='petapp.cats')),
            ],
        ),
        migrations.CreateModel(
            name='FleaTicksDogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flea_ticks_dogs', to='petapp.dogs')),
            ],
        ),
        migrations.CreateModel(
            name='FoodBrid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('Brid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_Brid', to='petapp.fish')),
            ],
        ),
        migrations.CreateModel(
            name='FoodCats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('cats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_cats', to='petapp.cats')),
            ],
        ),
        migrations.CreateModel(
            name='FoodDogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_dogs', to='petapp.dogs')),
            ],
        ),
        migrations.CreateModel(
            name='FoodFish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('fish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_fish', to='petapp.fish')),
            ],
        ),
        migrations.CreateModel(
            name='Groomingcats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('cats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grooming_cats', to='petapp.cats')),
            ],
        ),
        migrations.CreateModel(
            name='GroomingDogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grooming_dogs', to='petapp.dogs')),
            ],
        ),
        migrations.CreateModel(
            name='PharmacyVitaminsCats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('cats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy_vitamins_cats', to='petapp.dogs')),
            ],
        ),
        migrations.CreateModel(
            name='PharmacyVitaminsDogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy_vitamins_dogs', to='petapp.dogs')),
            ],
        ),
        migrations.CreateModel(
            name='Toyscats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('cats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toys_cats', to='petapp.cats')),
            ],
        ),
        migrations.CreateModel(
            name='ToysDogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toys_dogs', to='petapp.dogs')),
            ],
        ),
        migrations.CreateModel(
            name='TreatsBiscuitsCats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('cats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treats_biscuits_cats', to='petapp.cats')),
            ],
        ),
        migrations.CreateModel(
            name='TreatsBiscuitsDogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treats_biscuits_dogs', to='petapp.dogs')),
            ],
        ),
        migrations.CreateModel(
            name='WetFoodCats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('cats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wet_food_cats', to='petapp.cats')),
            ],
        ),
        migrations.CreateModel(
            name='WetFoodDogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wet_food_dogs', to='petapp.dogs')),
            ],
        ),
        migrations.DeleteModel(
            name='Sidebar',
        ),
        migrations.RenameField(
            model_name='search',
            old_name='boot',
            new_name='text',
        ),
        migrations.AddField(
            model_name='bedsdogs',
            name='dog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beds_dogs', to='petapp.dogs'),
        ),
        migrations.AddField(
            model_name='bedscats',
            name='cats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beds_cats', to='petapp.cats'),
        ),
        migrations.AddField(
            model_name='accessoriesfish',
            name='fish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessories_fish', to='petapp.fish'),
        ),
        migrations.AddField(
            model_name='accessoriesdogs',
            name='dog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessories_dogs', to='petapp.dogs'),
        ),
        migrations.AddField(
            model_name='accessoriescats',
            name='cats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessories_cats', to='petapp.cats'),
        ),
        migrations.AddField(
            model_name='accessoriesbrid',
            name='Brid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessories_Brid', to='petapp.brid'),
        ),
    ]
