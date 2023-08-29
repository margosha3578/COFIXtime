# Generated by Django 4.2.2 on 2023-08-25 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_remove_scheduleforoneday_hour_00_01_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scheduleforoneday',
            old_name='hour_00_01',
            new_name='hour_0_1',
        ),
        migrations.RenameField(
            model_name='scheduleforoneday',
            old_name='hour_01_02',
            new_name='hour_1_2',
        ),
        migrations.RenameField(
            model_name='scheduleforoneday',
            old_name='hour_02_03',
            new_name='hour_2_3',
        ),
        migrations.RenameField(
            model_name='scheduleforoneday',
            old_name='hour_04_05',
            new_name='hour_3_4',
        ),
        migrations.RenameField(
            model_name='scheduleforoneday',
            old_name='hour_09_10',
            new_name='hour_5_6',
        ),
        migrations.RenameField(
            model_name='scheduleforoneday',
            old_name='hour_03_04',
            new_name='hour_6_7',
        ),
        migrations.RenameField(
            model_name='scheduleforoneday',
            old_name='hour_05_06',
            new_name='hour_7_8',
        ),
        migrations.RenameField(
            model_name='scheduleforoneday',
            old_name='hour_06_07',
            new_name='hour_8_9',
        ),
        migrations.RenameField(
            model_name='scheduleforoneday',
            old_name='hour_07_08',
            new_name='hour_9_10',
        ),
        migrations.RemoveField(
            model_name='scheduleforoneday',
            name='hour_08_09',
        ),
        migrations.AddField(
            model_name='scheduleforoneday',
            name='hour_4_5',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
