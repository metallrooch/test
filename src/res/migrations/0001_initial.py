# Generated by Django 2.1.5 on 2019-01-14 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_reserved', models.BooleanField(default=False)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Table №<django.db.models.fields.IntegerField>', max_length=20)),
                ('places', models.IntegerField(default=True)),
                ('shape', models.CharField(choices=[('OVAL', 'oval'), ('SQUERE', 'squere')], default=True, max_length=20)),
                ('width', models.IntegerField(default=10)),
                ('length', models.IntegerField(default=20)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='reserved',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='res.Table'),
        ),
        migrations.AddField(
            model_name='reserved',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='res.User'),
        ),
    ]
