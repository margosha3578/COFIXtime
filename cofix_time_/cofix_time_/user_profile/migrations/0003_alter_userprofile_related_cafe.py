# Generated by Django 4.2.2 on 2023-08-04 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_userprofile_related_cafe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='related_cafe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.relatedcafe'),
        ),
    ]
