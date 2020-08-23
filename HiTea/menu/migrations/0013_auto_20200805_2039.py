# Generated by Django 3.0.8 on 2020-08-06 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_auto_20200805_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='HotCheeseFoam',
            new_name='CheeseFoam',
        ),
        migrations.RenameModel(
            old_name='HotLemonTea',
            new_name='LemonTea',
        ),
        migrations.RenameModel(
            old_name='IcedMilkTea',
            new_name='MilkTea',
        ),
        migrations.RemoveField(
            model_name='icedcheesefoam',
            name='product',
        ),
        migrations.RemoveField(
            model_name='icedlemontea',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='isHot',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='HotMilkTea',
        ),
        migrations.DeleteModel(
            name='IcedCheeseFoam',
        ),
        migrations.DeleteModel(
            name='IcedLemonTea',
        ),
        migrations.AddField(
            model_name='food',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Product'),
        ),
    ]