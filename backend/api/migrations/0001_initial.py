# Generated by Django 4.0.8 on 2023-01-02 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battery_capacity', models.TextField(max_length=45)),
                ('charge_port', models.TextField(max_length=45)),
                ('port_location', models.TextField(max_length=45)),
                ('voltage', models.TextField(max_length=45)),
                ('charging_time', models.TextField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_class', models.TextField(max_length=45)),
                ('style', models.TextField(max_length=45)),
                ('layout', models.TextField(max_length=45)),
                ('frame', models.TextField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rim', models.TextField(max_length=45)),
                ('front_tire', models.TextField(max_length=45)),
                ('rear_tire', models.TextField(max_length=45)),
                ('front_suspension', models.TextField(max_length=45)),
                ('rear_suspension', models.TextField(max_length=45)),
                ('front_brake', models.TextField(max_length=45)),
                ('rear_brake', models.TextField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDimension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.DecimalField(decimal_places=2, max_digits=6)),
                ('width', models.DecimalField(decimal_places=2, max_digits=6)),
                ('height', models.DecimalField(decimal_places=2, max_digits=6)),
                ('wheelbase', models.DecimalField(decimal_places=2, max_digits=6)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_speed', models.IntegerField()),
                ('electric_range', models.IntegerField()),
                ('power', models.TextField(max_length=45)),
                ('torque', models.IntegerField()),
                ('drivetrain', models.TextField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=45)),
                ('username', models.TextField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=45)),
                ('production_year', models.DateField(null=True)),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=15)),
                ('battery_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.battery')),
                ('body_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.body')),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.category')),
                ('dimension_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productdimension')),
                ('lastEditedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.user')),
                ('performance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productperformance')),
            ],
        ),
    ]
