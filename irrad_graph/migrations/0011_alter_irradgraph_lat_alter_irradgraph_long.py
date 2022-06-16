# Generated by Django 4.0.5 on 2022-06-16 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irrad_graph', '0010_irradgraph_csv_file_alter_irradgraph_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='irradgraph',
            name='lat',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='irradgraph',
            name='long',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]