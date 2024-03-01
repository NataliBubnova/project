# Generated by Django 4.2.5 on 2023-12-22 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import my_project.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('type_of_actuator', models.CharField(help_text='Введите вид привода', max_length=50, primary_key=True, serialize=False, verbose_name='Привод')),
                ('plus', models.TextField(help_text='Опишите плюсы', null=True, verbose_name='Плюсы')),
                ('minus', models.TextField(help_text='Опишите минусы', null=True, verbose_name='Минусы')),
            ],
            options={
                'db_table': 'Actuator',
            },
        ),
        migrations.CreateModel(
            name='Bodywork',
            fields=[
                ('classification', models.CharField(help_text='Введите тип кузова', max_length=50, primary_key=True, serialize=False, verbose_name='Кузов')),
                ('number_of_doors', my_project.models.IntegerRangeField(help_text='Введите количество дверей', null=True, verbose_name='Количество дверей')),
                ('number_of_seats', my_project.models.IntegerRangeField(help_text='Введите количесто мест', null=True, verbose_name='Количество мест')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'db_table': 'Bodywork',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название бренда', max_length=50, verbose_name='Компания')),
                ('country', models.CharField(help_text='Введите страну', max_length=50, null=True, verbose_name='Страна')),
                ('foundation_date', models.DateField(help_text='Введите дату основания', null=True, verbose_name='Дата основания')),
                ('information', models.TextField(help_text='Опишите компанию', null=True, verbose_name='Информация')),
            ],
            options={
                'db_table': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('type_of_transmission', models.CharField(help_text='Введите тип коробки передач', max_length=50, primary_key=True, serialize=False, verbose_name='Коробка передач')),
                ('number_of_gears', my_project.models.IntegerRangeField(null=True, verbose_name='Количество передач')),
            ],
            options={
                'db_table': 'Transmission',
            },
        ),
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('type_motor', models.CharField(help_text='Введите тип двигателя', max_length=50, primary_key=True, serialize=False, verbose_name='Двигатель')),
                ('location', models.CharField(help_text='Введите расположение', max_length=50, null=True, verbose_name='Расположение')),
                ('engine_cylinder', my_project.models.IntegerRangeField(help_text='Введите количество цилиндров', null=True, verbose_name='Цилиндры двигателя')),
                ('transmission', models.ForeignKey(help_text='Выберите тип коробки передач', null=True, on_delete=django.db.models.deletion.CASCADE, to='my_project.transmission', verbose_name='Коробка передач')),
            ],
            options={
                'db_table': 'Motor',
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id_characteristic', my_project.models.IntegerRangeField(help_text='Введите id характеристики', primary_key=True, serialize=False, verbose_name='ID характеристики]')),
                ('actuator', models.ForeignKey(help_text='Выберите привод', null=True, on_delete=django.db.models.deletion.CASCADE, to='my_project.actuator', verbose_name='Привод')),
                ('bodywork', models.ForeignKey(help_text='Выберите кузов', null=True, on_delete=django.db.models.deletion.CASCADE, to='my_project.bodywork', verbose_name='Кузов')),
            ],
            options={
                'db_table': 'Characteristic',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id_car', my_project.models.IntegerRangeField(help_text='Введите id машины', primary_key=True, serialize=False, verbose_name='ID машины')),
                ('name_of_model', models.CharField(help_text='Введите название модели', max_length=50, verbose_name='Модель')),
                ('year_of_production', models.DateField(help_text='Укажите дату создания', null=True, verbose_name='Дата создания')),
                ('price', models.IntegerField(help_text='Введите цену', null=True, verbose_name='Цена')),
                ('characteristic', models.ForeignKey(help_text='Выберите характеристики', null=True, on_delete=django.db.models.deletion.CASCADE, to='my_project.characteristic', verbose_name='Характеристики')),
                ('id_user', models.ForeignKey(blank=True, help_text='выберите id пользователя', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id User')),
                ('name_of_brand', models.ForeignKey(help_text='Выберите марку', null=True, on_delete=django.db.models.deletion.CASCADE, to='my_project.brand', verbose_name='Марка')),
            ],
            options={
                'db_table': 'Car',
            },
        ),
        migrations.AddField(
            model_name='actuator',
            name='motor',
            field=models.ForeignKey(help_text='Выберите вид привода', null=True, on_delete=django.db.models.deletion.CASCADE, to='my_project.motor', verbose_name='Двигатель'),
        ),
    ]
