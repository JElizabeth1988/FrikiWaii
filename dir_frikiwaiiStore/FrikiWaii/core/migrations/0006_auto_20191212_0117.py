# Generated by Django 2.2.5 on 2019-12-12 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191125_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoContacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('asunto', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=200)),
                ('tipoContacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TipoContacto')),
            ],
        ),
    ]
