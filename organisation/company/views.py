from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import datetime
from .forms import UserRegistration, ProfileForm, UserLogIn, CreateUnit, CreateEmployee, UpdateDepartment
from .models import Employee, Unit, Profile

# Create your views here.
def register(request):

    if request.method == 'POST':
        user_form = UserRegistration(request.POST or None)
        profile_form = ProfileForm(request.POST or None)

        if user_form.is_valid() and profile_form.is_valid():

            if Profile.objects.filter(full_name=profile_form.cleaned_data['full_name']).exists():
                
                return render(request, 'register.html', {'user_form': user_form,
                                                        'profile_form': profile_form,
                                                        'name': profile_form.cleaned_data['full_name']
                                                        })
            else:
                new_user = user_form.save(commit=False)
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()

                profile = Profile.objects.create(user=new_user,
                                                full_name=profile_form.cleaned_data['full_name'],
                                                position=profile_form.cleaned_data['position'],
                                                department=profile_form.cleaned_data['department'],
                                                start_work=profile_form.cleaned_data['start_work']
                                                )

                return HttpResponse('<h1>Register succes</h1>')
    else:
        user_form = UserRegistration()
        profile_form = ProfileForm()

    return render(request, 'register.html', {
                                            'user_form': user_form,
                                            'profile_form': profile_form
                                            })

def loginUser(request):

    if request.method == 'POST':
        form = UserLogIn(request.POST or None)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = UserLogIn()

    return render(request, 'login.html', {'form': form})


def logoutUser(request):

    if request.user.is_authenticated:
        logout(request)

        return render(request, 'logged_out.html')
    else:
        return HttpResponse('<h1>You didn\'t login</h1>')

@login_required(login_url='login')
def createUnit(request):

    form = CreateUnit(request.POST or None)
    if request.method == 'POST' and request.POST.get('create'):
        unit = request.POST.get('unit')
        if Unit.objects.filter(unit=unit).exists():

            return render(request, 'unit.html', {'form': form,
                                                 'name': unit
                                                })
        else:
            Unit.create(unit)

            return render(request, 'unit.html', {'form': form,
                                                 'department': True
                                                })

    return render(request, 'unit.html', {'form': form})

def collectUnit():

    units = []
    for obj in Unit.objects.all():
        units.append(obj.unit)

    return units  

@login_required(login_url='login')
def showUnit(request):

    units = collectUnit()
    if request.method == 'POST' and request.POST.get('delete'):
        deleteCompany = request.POST.get('company')
        
        try:
            obj = Unit.objects.get(unit=deleteCompany)
            obj.delete()
        except:
            return render(request, 'showUnits.html', {'units': units,
                                                      'flag': True
                                                     })
        units = collectUnit()

        return render(request, 'showUnits.html', {'units': units})
   
    return render(request, 'showUnits.html', {'units': units})

@login_required(login_url='login')
def createEmployee(request):

    form = CreateEmployee(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            if Employee.objects.filter(full_name=form.cleaned_data['full_name']).exists():

                return render(request, 'employee.html', {'form': form,
                                                         'name': form.cleaned_data['full_name']
                                                        })
            else:
                form.save()

                return render(request, 'employee.html', {'form': form,
                                                        'flag': True
                                                        })

    return render(request, 'employee.html', {'form': form})

def collectEmployee():

    employee_name = []
    employee_department = []

    for obj in Employee.objects.all():
        employee_name.append(obj.full_name)
        employee_department.append(obj.department)

    employee = zip(employee_name, employee_department)

    return employee

@login_required(login_url='login')
def editEmployee(request):

    employee = collectEmployee()
    update_department = UpdateDepartment(request.POST)

    if request.method == 'POST' and request.POST.get('delete'):
        deleteEmployee = request.POST.get('employee')
        
        try:
            obj = Employee.objects.get(full_name=deleteEmployee)
            obj.delete()
        except:
            return render(request, 'editEmployee.html', {'employee': employee,
                                                         'form': update_department,
                                                         'flag': True
                                                        })
        
        employee = collectEmployee()

        return render(request, 'editEmployee.html', {'employee': employee,
                                                     'form': update_department
                                                    })

    if request.method == 'POST' and request.POST.get('edit'):
        editPosition = request.POST.get('employee')

        if update_department.is_valid():
            department = update_department.cleaned_data['department']

            obj = Employee.objects.filter(full_name=editPosition)
            obj.update(department=department)

            employee = collectEmployee()

            return render(request, 'editEmployee.html', {'employee': employee,
                                                         'form': update_department
                                                        })

    return render(request, 'editEmployee.html', {'employee': employee,
                                                 'form': update_department
                                                })

@login_required(login_url='login')
def cardEmployee(request):

    data = []
  
    for obj in Employee.objects.all():
        data.append(obj.full_name)

    if request.method == 'POST' and request.POST.get('show'):
        full_name = request.POST.get('card')
        
        try:
            info = Employee.objects.get(full_name=full_name)
        except:
            return render(request, 'cardEmployee.html', {'data': data,
                                                         'flag': True
                                                        })

        return render(request, 'cardEmployee.html', {'data': data,
                                                     'info': info
                                                    })

    return render(request, 'cardEmployee.html', {'data': data})

@login_required(login_url='login')
def showInfo(request):

    info = []
    try:
        for obj in Profile.objects.all():
            info.append(obj)
    except BaseException:
        return render(request, 'showInfo.html', {'flag': True})

    amount = []
    for i in info:
        start_date = i.start_work
        delta = (datetime.date.today() - start_date).days
        delta = delta // 365
        amount.append(f"{delta} years")

    info = zip(info, amount)

    return render(request, 'showInfo.html', {'info': info})