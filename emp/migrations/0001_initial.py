# Generated by Django 4.1.1 on 2022-11-13 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='depart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('salary', models.IntegerField(default='0')),
                ('bonus', models.IntegerField(default='0')),
                ('phone', models.IntegerField(default='0')),
                ('hiredate', models.DateField()),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.depart')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.role')),
            ],
        ),
    ]
