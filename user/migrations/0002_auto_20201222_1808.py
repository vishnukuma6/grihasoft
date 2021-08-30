# Generated by Django 3.0.4 on 2020-12-22 18:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerid', models.IntegerField(blank=True, null=True)),
                ('employeeid', models.IntegerField(blank=True, null=True)),
                ('invoiceno', models.CharField(blank=True, max_length=128, null=True)),
                ('invoicedate', models.DateTimeField()),
                ('amount', models.FloatField(blank=True, null=True)),
                ('duedays', models.IntegerField(blank=True, null=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='mobileno',
            field=models.IntegerField(default=-1),
        ),
        migrations.CreateModel(
            name='EntityDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('code', models.CharField(blank=True, max_length=128, null=True)),
                ('gstno', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('entity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('code', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Designation')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gst', models.CharField(blank=True, max_length=128, null=True)),
                ('creditperiod', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('code', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionTran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amountreceived', models.FloatField(blank=True, null=True)),
                ('date', models.DateTimeField()),
                ('status', models.SmallIntegerField(default=1)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('collectionheader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.CollectionHeader')),
            ],
        ),
        migrations.AddField(
            model_name='collectionheader',
            name='entitydetail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.EntityDetail'),
        ),
    ]
