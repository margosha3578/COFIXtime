# Generated by Django 4.2.2 on 2023-08-26 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0010_scheduleforoneday_cafe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafeworkinghours',
            name='hour_0_1',
        ),
        migrations.RemoveField(
            model_name='cafeworkinghours',
            name='hour_1_2',
        ),
        migrations.RemoveField(
            model_name='cafeworkinghours',
            name='hour_2_3',
        ),
        migrations.RemoveField(
            model_name='cafeworkinghours',
            name='hour_3_4',
        ),
        migrations.RemoveField(
            model_name='cafeworkinghours',
            name='hour_4_5',
        ),
        migrations.RemoveField(
            model_name='cafeworkinghours',
            name='hour_5_6',
        ),
        migrations.RemoveField(
            model_name='scheduleforoneday',
            name='hour_0_1',
        ),
        migrations.RemoveField(
            model_name='scheduleforoneday',
            name='hour_1_2',
        ),
        migrations.RemoveField(
            model_name='scheduleforoneday',
            name='hour_2_3',
        ),
        migrations.RemoveField(
            model_name='scheduleforoneday',
            name='hour_3_4',
        ),
        migrations.RemoveField(
            model_name='scheduleforoneday',
            name='hour_4_5',
        ),
        migrations.RemoveField(
            model_name='scheduleforoneday',
            name='hour_5_6',
        ),
    ]