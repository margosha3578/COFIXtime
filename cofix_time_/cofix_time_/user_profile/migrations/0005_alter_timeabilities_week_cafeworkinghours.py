# Generated by Django 4.2.2 on 2023-08-18 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_timeabilities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeabilities',
            name='week',
            field=models.DateField(verbose_name='Понедельник на неделе'),
        ),
        migrations.CreateModel(
            name='CafeWorkingHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour_00_01', models.IntegerField()),
                ('hour_01_02', models.IntegerField()),
                ('hour_02_03', models.IntegerField()),
                ('hour_03_04', models.IntegerField()),
                ('hour_04_05', models.IntegerField()),
                ('hour_05_06', models.IntegerField()),
                ('hour_06_07', models.IntegerField()),
                ('hour_07_08', models.IntegerField()),
                ('hour_08_09', models.IntegerField()),
                ('hour_09_10', models.IntegerField()),
                ('hour_10_11', models.IntegerField()),
                ('hour_11_12', models.IntegerField()),
                ('hour_12_13', models.IntegerField()),
                ('hour_13_14', models.IntegerField()),
                ('hour_14_15', models.IntegerField()),
                ('hour_15_16', models.IntegerField()),
                ('hour_16_17', models.IntegerField()),
                ('hour_17_18', models.IntegerField()),
                ('hour_18_19', models.IntegerField()),
                ('hour_19_20', models.IntegerField()),
                ('hour_20_21', models.IntegerField()),
                ('hour_21_22', models.IntegerField()),
                ('hour_22_23', models.IntegerField()),
                ('hour_23_24', models.IntegerField()),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.relatedcafe')),
            ],
        ),
    ]
