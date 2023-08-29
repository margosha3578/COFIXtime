# Generated by Django 4.2.2 on 2023-08-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_alter_timeabilities_week_cafeworkinghours'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleForOneDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.DateField(verbose_name='Понедельник на неделе')),
                ('day_of_week', models.CharField(max_length=10)),
                ('hour_00_01', models.ManyToManyField(blank=True, related_name='hour_00_01', to='user_profile.userprofile')),
                ('hour_01_02', models.ManyToManyField(blank=True, related_name='hour_01_02', to='user_profile.userprofile')),
                ('hour_02_03', models.ManyToManyField(blank=True, related_name='hour_02_03', to='user_profile.userprofile')),
                ('hour_03_04', models.ManyToManyField(blank=True, related_name='hour_03_04', to='user_profile.userprofile')),
                ('hour_04_05', models.ManyToManyField(blank=True, related_name='hour_04_05', to='user_profile.userprofile')),
                ('hour_05_06', models.ManyToManyField(blank=True, related_name='hour_05_06', to='user_profile.userprofile')),
                ('hour_06_07', models.ManyToManyField(blank=True, related_name='hour_06_07', to='user_profile.userprofile')),
                ('hour_07_08', models.ManyToManyField(blank=True, related_name='hour_07_08', to='user_profile.userprofile')),
                ('hour_08_09', models.ManyToManyField(blank=True, related_name='hour_08_09', to='user_profile.userprofile')),
                ('hour_09_10', models.ManyToManyField(blank=True, related_name='hour_09_10', to='user_profile.userprofile')),
                ('hour_10_11', models.ManyToManyField(blank=True, related_name='hour_10_11', to='user_profile.userprofile')),
                ('hour_11_12', models.ManyToManyField(blank=True, related_name='hour_11_12', to='user_profile.userprofile')),
                ('hour_12_13', models.ManyToManyField(blank=True, related_name='hour_12_13', to='user_profile.userprofile')),
                ('hour_13_14', models.ManyToManyField(blank=True, related_name='hour_13_14', to='user_profile.userprofile')),
                ('hour_14_15', models.ManyToManyField(blank=True, related_name='hour_14_15', to='user_profile.userprofile')),
                ('hour_15_16', models.ManyToManyField(blank=True, related_name='hour_15_16', to='user_profile.userprofile')),
                ('hour_16_17', models.ManyToManyField(blank=True, related_name='hour_16_17', to='user_profile.userprofile')),
                ('hour_17_18', models.ManyToManyField(blank=True, related_name='hour_17_18', to='user_profile.userprofile')),
                ('hour_18_19', models.ManyToManyField(blank=True, related_name='hour_18_19', to='user_profile.userprofile')),
                ('hour_19_20', models.ManyToManyField(blank=True, related_name='hour_19_20', to='user_profile.userprofile')),
                ('hour_20_21', models.ManyToManyField(blank=True, related_name='hour_20_21', to='user_profile.userprofile')),
                ('hour_21_22', models.ManyToManyField(blank=True, related_name='hour_21_22', to='user_profile.userprofile')),
                ('hour_22_23', models.ManyToManyField(blank=True, related_name='hour_22_23', to='user_profile.userprofile')),
                ('hour_23_24', models.ManyToManyField(blank=True, related_name='hour_23_24', to='user_profile.userprofile')),
            ],
        ),
    ]
