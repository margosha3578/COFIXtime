# Generated by Django 4.2.2 on 2023-08-04 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedCafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('post', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('telephone_number', models.CharField(max_length=13)),
                ('related_cafe', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.relatedcafe')),
            ],
        ),
        migrations.AddField(
            model_name='relatedcafe',
            name='manager_name',
            field=models.ManyToManyField(blank=True, to='user_profile.userprofile'),
        ),
    ]