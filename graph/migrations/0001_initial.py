# Generated by Django 4.0.5 on 2022-08-07 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IrradGraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('long', models.DecimalField(decimal_places=2, max_digits=5)),
                ('year', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/graph_imgs')),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('csv_file', models.FileField(blank=True, null=True, upload_to='media/csv')),
            ],
            options={
                'verbose_name_plural': 'IrradGraphs',
            },
        ),
    ]
