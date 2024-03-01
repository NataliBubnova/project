from django.db import models
from django.contrib.auth.models import User


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(**kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Transmission(models.Model):
    type_of_transmission = models.CharField(max_length=50,  primary_key=True, verbose_name="Коробка передач",
                                            help_text="Введите тип коробки передач", null=False, blank=False)
    number_of_gears = IntegerRangeField(min_value=1, max_value=9, verbose_name="Количество передач", null=True)

    def __str__(self):
        return 'Transmission: ' + self.type_of_transmission

    class Meta:
        db_table = 'Transmission'


class Motor(models.Model):
    type_motor = models.CharField(max_length=50, primary_key=True, verbose_name="Двигатель",
                                  help_text="Введите тип двигателя", null=False, blank=False)
    location = models.CharField(max_length=50, verbose_name="Расположение",
                                help_text="Введите расположение", null=True, blank=False)
    engine_cylinder = IntegerRangeField(min_value=1, max_value=12, verbose_name="Цилиндры двигателя",
                                        help_text="Введите количество цилиндров", null=True)
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE, verbose_name="Коробка передач",
                                     help_text="Выберите тип коробки передач", null=True)

    def __str__(self):
        return 'Motor: ' + self.type_motor

    class Meta:
        db_table = 'Motor'


class Actuator(models.Model):
    type_of_actuator = models.CharField(max_length=50, primary_key=True, verbose_name="Привод",
                                        help_text="Введите вид привода", null=False, blank=False)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE, verbose_name="Двигатель",
                              help_text="Выберите вид привода", null=True, blank=False)
    plus = models.TextField(verbose_name="Плюсы", help_text="Опишите плюсы", null=True)
    minus = models.TextField(verbose_name="Минусы", help_text="Опишите минусы", null=True)

    def __str__(self):
        return 'Actuator: ' + self.type_of_actuator

    class Meta:
        db_table = 'Actuator'


class Bodywork(models.Model):
    classification = models.CharField(max_length=50, primary_key=True, verbose_name="Кузов",
                                      help_text="Введите тип кузова", null=False, blank=False)
    number_of_doors = IntegerRangeField(min_value=1, max_value=10, verbose_name="Количество дверей",
                                        help_text="Введите количество дверей", null=True)
    number_of_seats = IntegerRangeField(min_value=1, verbose_name="Количество мест",
                                        help_text="Введите количесто мест", null=True)
    description = models.TextField(verbose_name="Описание", null=True)

    def __str__(self):
        return 'Bodywork: ' + self.classification

    class Meta:
        db_table = 'Bodywork'


class Characteristic(models.Model):
    id_characteristic = IntegerRangeField(min_value=1, primary_key=True, verbose_name="ID характеристики]",
                      help_text="Введите id характеристики", null=False, blank=False)
    actuator = models.ForeignKey(Actuator, on_delete=models.CASCADE, verbose_name="Привод", help_text="Выберите привод", null=True)
    bodywork = models.ForeignKey(Bodywork, on_delete=models.CASCADE, verbose_name="Кузов", help_text="Выберите кузов", null=True)


    class Meta:
        db_table = 'Characteristic'


class Brand(models.Model):
    name_of_brand = models.CharField(max_length=50, verbose_name="Компания",
                            help_text="Введите название бренда", null=False, blank=False)
    country = models.CharField(max_length=50, verbose_name="Страна", help_text="Введите страну", null=True)
    foundation_date = models.DateField(verbose_name="Дата основания", help_text="Введите дату основания", null=True)
    information = models.TextField(verbose_name="Информация", help_text="Опишите компанию", null=True)

    def __str__(self):
        return 'Brand: ' + self.name_of_brand

    class Meta:
        db_table = 'Brand'


class Car(models.Model):
    id_car = IntegerRangeField(min_value=1, primary_key=True, verbose_name="ID машины",
                               help_text="Введите id машины", null=False, blank=False)
    name_of_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Марка",
                                      help_text="Выберите марку", null=True, blank=False)
    name_of_model = models.CharField(max_length=50, verbose_name="Модель",
                                     help_text="Введите название модели", null=False, blank=False)
    year_of_production = models.DateField(verbose_name="Дата создания", help_text="Укажите дату создания", null=True)
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену", null=True)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE, verbose_name="Характеристики",
                                       help_text="Выберите характеристики", null=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id User', help_text='выберите id пользователя',
                                null=True, blank=True)

    class Meta:
        db_table = 'Car'

class Employee(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Name", help_text="Введите имя",
                                  null=False, blank=False)
    last_name = models.CharField(max_length=100, verbose_name="Surname", help_text="Введите фамилию",
                                 null=False, blank=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id User', help_text='выберите id пользователя',
                                null=True, blank=True)

    def __str__(self):
        return 'Employee: ' + self.first_name

    class Meta:
        db_table = "Employee"


class Department(models.Model):
    name_department = models.CharField(max_length=100, verbose_name="Название отдела",
                                       help_text="Введите название отдела", null=False, blank=False,
                                       primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Employee', help_text='выберите id сотрудника',
                                 null=False, blank=False)
    brands = models.ManyToManyField(Brand)

    def __str__(self):
        return 'Department: ' + self.name_department

    class Meta:
        db_table = "Department"
