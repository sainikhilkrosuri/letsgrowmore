from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import activity, student, SubmitForm
from .forms import MainForm
import requests


# Create your views here.
# Task 1
def index(request):
    if request.method == "POST":
        acc = request.POST.get("activity")
        main = activity(acc=acc)
        main.save()
        messages.success(request, "task added")
        return redirect("/")
    main = activity.objects.all()
    return render(request, "index.html", {"main": main})


def done(request, main):
    gain = activity.objects.get(id=main)
    gain.default = False
    gain.save()
    messages.success(request, "Hurry up the time passed away")
    return redirect('/')


def undone(request, main):
    gain = activity.objects.get(id=main)
    gain.default = True
    gain.save()
    messages.success(request, "Task done in time")
    return redirect('/')


def delete(request, main):
    main = activity.objects.filter(id=main).get()
    main.delete()
    messages.success(request, "Task deleted successfully")
    return redirect("/")


# Task 3
def stude(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        website = request.POST.get("website")
        image = request.FILES.get("image")
        gender = request.POST.get("gender")
        java = request.POST.get("java")
        python = request.POST.get("python")
        other = request.POST.get("other")
        if java is None:
            java = False
        if python is None:
            python = False
        if other is None:
            other = False
        if image is None:
            image = None
        stu = student.objects.create(name=name, email=email, website=website, image=image, gender=gender,
                                     java=java,
                                     python=python, other=other)
        stu.save()
        messages.success(request, "Data added successfully please refresh the page")
        return render(request, "student.html")
    students = student.objects.all()
    return render(request, "student.html", {"students": students})


def remove(request, main):
    main = student.objects.get(id=main)
    main.delete()
    messages.success(request, "Data deleted successfully")
    return redirect("student")


# Task 4
def calculator(request):
    try:
        if request.method == "POST":
            main = request.POST.get("primary")
            if main == "":
                messages.error(request, "Input is not formulated")
                return redirect("calculator")
            else:
                output = eval(main)
                messages.success(request, "Operation performed successfully")
                return render(request, "calculator.html", {"output": output, "record": main})
    except:
        messages.error(request, "Please Check the input")
        return redirect("calculator")

    return render(request, "calculator.html")


def result(request):
    try:
        if request.method == "POST":
            helo = request.POST.get("pin")
            main = SubmitForm.objects.filter(pin=helo).get()
            state = True
            return render(request, "result.html", {"main": main, "state": state})
        state = False
        return render(request, "result.html", {"state": state})
    except:
        messages.error(request, "Data not found")
        state = False
        return render(request, "result.html", {"state": state})


@login_required(login_url="signin")
def submit(request):
    if request.method == "POST":
        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "form submitted successfully")
            return redirect("submit")
    form = MainForm
    return render(request, "submitted.html", {"form": form})


def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "login successfully done add data now")
            return redirect("submit")
    return render(request, "signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("signin")


def person(request):
    if request.method == "POST":
        number = request.POST.get("number")
        if int(number) == 0:
            messages.error(request, "id can't be zero")
            return redirect("person")
        elif 0 < int(number) <= 6:
            ma = requests.get("https://reqres.in/api/users?page=1").json()
            main = ma.get("data")
            i = main[int(number) - 1]
            person_id = i.get("id")
            person_email = i.get("email")
            person_fname = i.get("first_name")
            person_lname = i.get("last_name")
            person_avatar = i.get("avatar")
            messages.success(request, "Data found")
            return render(request, "person.html",
                          {"person_id": person_id, "person_email": person_email, "person_fname": person_fname,
                           "person_lname": person_lname, "person_avatar": person_avatar})
        elif 7 <= int(number) <= 12:
            if number == "7":
                number = 1
            if number == "8":
                number = 2
            if number == "9":
                number = 3
            if number == "10":
                number = 4
            if number == "11":
                number = 5
            if number == "12":
                number = 6
            mad = requests.get("https://reqres.in/api/users?page=2").json()
            main = mad.get("data")
            i = main[int(number) - 1]
            person_id = i.get("id")
            person_email = i.get("email")
            person_fname = i.get("first_name")
            person_lname = i.get("last_name")
            person_avatar = i.get("avatar")
            messages.success(request, "Data found")
            return render(request, "person.html",
                          {"person_id": person_id, "person_email": person_email, "person_fname": person_fname,
                           "person_lname": person_lname, "person_avatar": person_avatar})
        else:
            messages.error(request, "No data found")
            return redirect("person")
    else:
        return render(request, "person.html")
