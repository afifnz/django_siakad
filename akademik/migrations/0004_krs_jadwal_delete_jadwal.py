# Generated by Django 5.1.3 on 2024-12-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0003_matakuliah_matkul_prasyarat_alter_periode_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='krs',
            name='jadwal',
            field=models.ManyToManyField(blank=True, to='akademik.kelas'),
        ),
        migrations.DeleteModel(
            name='Jadwal',
        ),
    ]