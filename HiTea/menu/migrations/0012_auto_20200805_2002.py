# Generated by Django 3.0.8 on 2020-08-06 00:02

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_auto_20200805_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freshfruit',
            name='toppings',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Pearl ($0.50)', 'Pearl ($0.50)'), ('Red Beans ($0.50)', 'Red Beans ($0.50)'), ('Coconut Jelly ($0.50)', 'Coconut Jelly ($0.50)'), ('Pudding ($0.50)', 'Pudding ($0.50)'), ('Agar Ball ($0.75)', 'Agar Ball ($0.75)'), ('Aloe ($0.75)', 'Aloe ($0.75)'), ('Popping Boba ($0.75)', 'Popping Boba ($0.75)'), ('Oreo ($1.00)', 'Oreo ($1.00)'), ('Cheese Foam ($1.00)', 'Cheese Foam ($1.00)')], max_length=154, null=True),
        ),
        migrations.AlterField(
            model_name='hotcheesefoam',
            name='toppings',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Pearl ($0.50)', 'Pearl ($0.50)'), ('Red Beans ($0.50)', 'Red Beans ($0.50)'), ('Coconut Jelly ($0.50)', 'Coconut Jelly ($0.50)'), ('Pudding ($0.50)', 'Pudding ($0.50)'), ('Agar Ball ($0.75)', 'Agar Ball ($0.75)'), ('Aloe ($0.75)', 'Aloe ($0.75)'), ('Popping Boba ($0.75)', 'Popping Boba ($0.75)'), ('Oreo ($1.00)', 'Oreo ($1.00)'), ('Cheese Foam ($1.00)', 'Cheese Foam ($1.00)')], max_length=154, null=True),
        ),
        migrations.AlterField(
            model_name='hotlemontea',
            name='toppings',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Pearl ($0.50)', 'Pearl ($0.50)'), ('Red Beans ($0.50)', 'Red Beans ($0.50)'), ('Coconut Jelly ($0.50)', 'Coconut Jelly ($0.50)'), ('Pudding ($0.50)', 'Pudding ($0.50)'), ('Agar Ball ($0.75)', 'Agar Ball ($0.75)'), ('Aloe ($0.75)', 'Aloe ($0.75)'), ('Popping Boba ($0.75)', 'Popping Boba ($0.75)'), ('Oreo ($1.00)', 'Oreo ($1.00)'), ('Cheese Foam ($1.00)', 'Cheese Foam ($1.00)')], max_length=154, null=True),
        ),
        migrations.AlterField(
            model_name='hotmilktea',
            name='toppings',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Pearl ($0.50)', 'Pearl ($0.50)'), ('Red Beans ($0.50)', 'Red Beans ($0.50)'), ('Coconut Jelly ($0.50)', 'Coconut Jelly ($0.50)'), ('Pudding ($0.50)', 'Pudding ($0.50)'), ('Agar Ball ($0.75)', 'Agar Ball ($0.75)'), ('Aloe ($0.75)', 'Aloe ($0.75)'), ('Popping Boba ($0.75)', 'Popping Boba ($0.75)'), ('Oreo ($1.00)', 'Oreo ($1.00)'), ('Cheese Foam ($1.00)', 'Cheese Foam ($1.00)')], max_length=154, null=True),
        ),
        migrations.AlterField(
            model_name='icedcheesefoam',
            name='toppings',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Pearl ($0.50)', 'Pearl ($0.50)'), ('Red Beans ($0.50)', 'Red Beans ($0.50)'), ('Coconut Jelly ($0.50)', 'Coconut Jelly ($0.50)'), ('Pudding ($0.50)', 'Pudding ($0.50)'), ('Agar Ball ($0.75)', 'Agar Ball ($0.75)'), ('Aloe ($0.75)', 'Aloe ($0.75)'), ('Popping Boba ($0.75)', 'Popping Boba ($0.75)'), ('Oreo ($1.00)', 'Oreo ($1.00)'), ('Cheese Foam ($1.00)', 'Cheese Foam ($1.00)')], max_length=154, null=True),
        ),
        migrations.AlterField(
            model_name='icedlemontea',
            name='toppings',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Pearl ($0.50)', 'Pearl ($0.50)'), ('Red Beans ($0.50)', 'Red Beans ($0.50)'), ('Coconut Jelly ($0.50)', 'Coconut Jelly ($0.50)'), ('Pudding ($0.50)', 'Pudding ($0.50)'), ('Agar Ball ($0.75)', 'Agar Ball ($0.75)'), ('Aloe ($0.75)', 'Aloe ($0.75)'), ('Popping Boba ($0.75)', 'Popping Boba ($0.75)'), ('Oreo ($1.00)', 'Oreo ($1.00)'), ('Cheese Foam ($1.00)', 'Cheese Foam ($1.00)')], max_length=154, null=True),
        ),
        migrations.AlterField(
            model_name='icedmilktea',
            name='toppings',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Pearl ($0.50)', 'Pearl ($0.50)'), ('Red Beans ($0.50)', 'Red Beans ($0.50)'), ('Coconut Jelly ($0.50)', 'Coconut Jelly ($0.50)'), ('Pudding ($0.50)', 'Pudding ($0.50)'), ('Agar Ball ($0.75)', 'Agar Ball ($0.75)'), ('Aloe ($0.75)', 'Aloe ($0.75)'), ('Popping Boba ($0.75)', 'Popping Boba ($0.75)'), ('Oreo ($1.00)', 'Oreo ($1.00)'), ('Cheese Foam ($1.00)', 'Cheese Foam ($1.00)')], max_length=154, null=True),
        ),
    ]
