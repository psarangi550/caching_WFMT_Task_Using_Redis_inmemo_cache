# Generated by Django 4.0 on 2022-01-03 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WFMTTaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp_number', models.CharField(max_length=10)),
                ('sne_id', models.IntegerField()),
                ('scheme_number', models.IntegerField()),
                ('trs', models.CharField(max_length=2)),
                ('estimate', models.CharField(max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CachingWFMTTaskIntoRedisApp.category')),
            ],
        ),
    ]
