# Generated by Django 4.1.4 on 2023-01-21 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Cname', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('Cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm.course')),
            ],
        ),
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now=True)),
                ('Sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm.website')),
            ],
        ),
    ]