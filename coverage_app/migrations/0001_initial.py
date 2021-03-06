# Generated by Django 2.1.7 on 2019-03-19 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=12)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('nurses', models.ManyToManyField(to='coverage_app.Nurse')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='nurse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coverage_app.Nurse'),
        ),
    ]
