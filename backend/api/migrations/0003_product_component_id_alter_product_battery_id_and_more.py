# Generated by Django 4.0.8 on 2023-01-04 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_battery_productbattery_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='component_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.productcomponent'),
        ),
        migrations.AlterField(
            model_name='product',
            name='battery_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.productbattery'),
        ),
        migrations.AlterField(
            model_name='product',
            name='body_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.productbody'),
        ),
        migrations.AlterField(
            model_name='product',
            name='dimension_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.productdimension'),
        ),
        migrations.AlterField(
            model_name='product',
            name='performance_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.productperformance'),
        ),
    ]
