# Generated by Django 3.0.7 on 2022-05-21 20:49

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('listings', '0001_initial'),
	]
	
	operations = [
		migrations.AlterField(
			model_name='listing',
			name='photo_1',
			field=models.FileField(blank=True, upload_to='photos/%Y/%m/%d/'),
		),
		migrations.AlterField(
			model_name='listing',
			name='photo_2',
			field=models.FileField(blank=True, upload_to='photos/%Y/%m/%d/'),
		),
		migrations.AlterField(
			model_name='listing',
			name='photo_3',
			field=models.FileField(blank=True, upload_to='photos/%Y/%m/%d/'),
		),
		migrations.AlterField(
			model_name='listing',
			name='photo_4',
			field=models.FileField(blank=True, upload_to='photos/%Y/%m/%d/'),
		),
		migrations.AlterField(
			model_name='listing',
			name='photo_5',
			field=models.FileField(blank=True, upload_to='photos/%Y/%m/%d/'),
		),
		migrations.AlterField(
			model_name='listing',
			name='photo_6',
			field=models.FileField(blank=True, upload_to='photos/%Y/%m/%d/'),
		),
		migrations.AlterField(
			model_name='listing',
			name='photo_main',
			field=models.FileField(upload_to='photos/%Y/%m/%d/'),
		),
	]