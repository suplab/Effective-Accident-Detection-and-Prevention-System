# Generated by Django 2.1.7 on 2019-03-16 15:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20190316_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccidentLocation',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('orgs', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='organisation',
            name='id',
            field=models.CharField(default=django.utils.timezone.now, max_length=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organisation',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
