from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

import my_project
from my_project.models import Car, Brand, Characteristic, Bodywork, Transmission, Employee, Department
from my_project.forms import CharForm
from django.contrib.auth.forms import UserCreationForm


def show_info(request, id_car=2):
    user = request.user
    if user.is_authenticated:
        if user.groups.filter(name="Сотрудники").exists():
            employee = Employee.objects.get(id_user_id=user.id)
            department = Department.objects.all()
            return render(request, 'employeeDepartments.html', {'department': department})
        else:
            car = Car.objects.get(id_user_id=user.id)
            name_of_model = Car.objects.filter(id_user=car.id_car)
            return render(request, 'carInfo.html', {'car': car, "name_of_model": name_of_model})
    else:
        return redirect("")

def show_car(request, id_car):
    user = request.user
    if user.is_authenticated and user.groups.filter(name="Сотрудники").exists():
        car = Car.objects.get(id_car=id_car)
        name_of_model = Car.objects.get(id_car=id_car)


        return render(request, 'employeeView.html', {'car': car, "name_of_model": name_of_model})
    else:
        return render(request, 'notAccess.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        print("mmm")
    return redirect('/')

def show_brands_odDepartment(request, name_department):
    department = Department.objects.get(name_department=name_department)
    name_of_brand = department.brands.filter(department=name_department)
    return render(request, 'employeeViewBrand.html', {"name_department": name_department, "brands": name_of_brand})

def show_carsFromBrands(request, name_department, name_of_brand):
    brand = Brand.objects.get(name_of_brand=name_of_brand)
    cars = Car.objects.filter(brand)
    return render(request, 'employeeViewCars.html', {"name_department": name_department, "cars": cars})

def show_index(request):
    if request.method == "GET":
        cur_user = request.user
        if cur_user.is_authenticated:
            return redirect("/info")
        else:
            return render(request, 'index.html')
    else:
        print(request.body)
        if (request.POST.get("email") != None):
            email = request.POST.get("email")
            password = request.POST.get("password")
            username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password)
            try:
                login(request, user)
                return redirect("/info")
            except Exception:
                print("Not correct email or password")
                return redirect("/")

        else:
            username = request.POST.get("create_name")
            email = request.POST.get("create_email")
            password = request.POST.get("create_password")
            user = User.objects.create_user(email=email, username=username, password=password)
            login(request, user)
            return redirect("/info")


def update_character(request, id_car):
    user = request.user
    if request.method == "GET":
        charForm = CharForm()
        return render(request, "templateForm.html", {"form": charForm})
    else:
        charform = CharForm(request.POST)
        if charform.is_valid():

            obj_car = Car.objects.get(id_car=id_car)
            obj_car.price = charform.cleaned_data['price']
            obj_car.save()

            obj_model = Car.objects.get(id_car=id_car)
            obj_model.name_of_model = charform.cleaned_data['model']
            obj_model.save()

            obj_transmission = Transmission()
            obj_transmission.transmission = charform.cleaned_data['transmission']
            obj_transmission.save()

            bodywork = charform.cleaned_data.get('classification')

            return redirect(f"/showcar/{id_car}", {'form': charform})
        else:
            print("ups")
            return redirect("/")

# Create your views here.
