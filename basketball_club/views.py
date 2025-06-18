from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from basketball_club.models import Students, Lecturers, Meetups, Tournament
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from datetime import datetime
# Create your views here.


def index(request):
    return render(request, 'index.html')


def joinus(request):
    if request.method == 'POST':
        studid = request.POST.get('studentid', '')
        noj = request.POST.get('nomonjersey', '')
        stuname = request.POST.get('studentname', '')
        sem = request.POST.get('semester', 0)
        phonenumber = request.POST.get('phonenumber', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        data = Students(studentid=studid,
                        nomonjersey=noj,
                        studentname=stuname,
                        semester=sem,
                        phonenumber=phonenumber,
                        email=email,
                        password=password)
        data.save()
    return render(request, 'joinus.html')


def login(request):
    if request.method == 'POST':
        studentid = request.POST['studentid']
        studentpassword = request.POST['studentpassword']

        find = Students.objects.filter(studentid=studentid).values()
        if find.exists():
            if (find[0]['password'] == studentpassword):
                request.session['logged_in'] = True
                request.session['studentid'] = studentid
                return redirect("profile", studentid=studentid)
            else:
                return render(request, 'login.html', {"message": "wrong password"})
        else:
            return render(request, 'login.html', {"message": "wrong username"})

    return render(request, 'login.html', {'message': 'Please log in'})


def meetups(request):
    all_tournaments = Tournament.objects.all()
    all_meetups = Meetups.objects.all().order_by(
        '-M_date')
    return render(request, 'meetups.html', {'meetups': all_meetups, 'tournaments': all_tournaments})


def members(request):
    students = Students.objects.all()
    lecturers = Lecturers.objects.all()
    context = {
        'students': students,
        'lecturers': lecturers,
        'message': 'NEW MENTOR HAS BEEN SAVED'
    }
    return render(request, "members.html", context)


def createmeetup(request):
    if request.method == 'POST':
        title = request.POST.get('M_tittle', '')
        description = request.POST.get('M_description', '')
        date_str = request.POST.get('M_date', '')
        time = request.POST.get('M_time', '')
        location = request.POST.get('M_location', '')

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'createmeetup.html', {'error': 'Invalid date format. Use YYYY-MM-DD.'})

        data = Meetups(M_title=title, M_description=description,
                       M_date=date, M_time=time, M_location=location)
        data.save()

        return redirect('meetups')

    return render(request, 'createmeetup.html')


def lecturerregister(request):
    if request.method == 'POST':
        lecturerid = request.POST.get('lecturerid', '')
        lecturername = request.POST.get('lecturername', '')
        lecturernumber = request.POST.get('lecturernumber', '')
        lectureremail = request.POST.get('lectureremail', '')
        lecturerpasword = request.POST.get('lecturerpasword', '')

        data = Lecturers(lecturerid=lecturerid,
                         lecturername=lecturername,
                         lecturernumber=lecturernumber,
                         lectureremail=lectureremail,
                         lecturerpasword=lecturerpasword)
        data.save()

    return render(request, 'lecturerregister.html')


def tournaments(request):
    if request.method == 'POST':
        tittle = request.POST.get('tittle', '')
        date1 = request.POST.get('date', '')
        time = request.POST.get('time', 0)
        location = request.POST.get('location', '')

        try:
            date = datetime.strptime(date1, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'createmeetup.html', {'error': 'Invalid date format. Use YYYY-MM-DD.'})

        data = Tournament(tittle=tittle,
                          date=date,
                          time=time,
                          location=location)
        data.save()

    return render(request, 'tournaments.html')


def profile(request, studentid=None):
    if not request.session.get('logged_in'):
        return redirect('login')

    if studentid is None:
        studentid = request.session.get('studentid')

    try:
        student = Students.objects.get(studentid=studentid)
        return render(request, 'profile.html', {'student': student})
    except Students.DoesNotExist:
        return render(request, 'login.html')


def logout(request):
    request.session.flush()
    return redirect('login')


def update(request, studentid):
    updateid = Students.objects.get(studentid=studentid)
    dict = {
        'updateid': updateid,
        'message': 'PAGE RENDERED, DATA IS NOT UPDATED YET'
    }
    return render(request, "update.html", dict)


def updatedata(request, studentid):
    if request.method == "POST":
        data = Students.objects.get(studentid=studentid)
        data.studentname = request.POST['studentname']
        data.nomonjersey = request.POST['nomonjersey']
        data.semester = request.POST['semester']
        data.phonenumber = request.POST['phonenumber']
        data.email = request.POST['email']
        data.password = request.POST['password']
        data.save()
        return redirect('profile', studentid=studentid)
    return HttpResponseRedirect(reverse("profile"))


def delete(request, studentid):
    if request.method == 'POST':
        student = Students.objects.get(studentid=studentid)
        student.delete()
        return redirect('login')
    return redirect('profile', studentid=studentid)


def viewdelete(request, studentid):
    student = Students.objects.get(studentid=studentid)
    return render(request, "delete.html", {'student': student})


def updatemeetup(request, meetupid):
    meetup = Meetups.objects.get(id=meetupid)
    if request.method == 'POST':
        meetup.M_title = request.POST.get('M_title')
        meetup.M_description = request.POST.get('M_description')
        meetup.M_date = request.POST.get('M_date')
        meetup.M_time = request.POST.get('M_time')
        meetup.M_location = request.POST.get('M_location')
        meetup.save()
        return redirect('meetups')
    return render(request, "updatemeetup.html", {'meetup': meetup})


def deletemeetup(request, meetupid):
    if request.method == 'POST':
        meetupdelete = Meetups.objects.get(id=meetupid)
        meetupdelete.delete()
        return redirect('meetups')
    meetup = Meetups.objects.get(id=meetupid)
    return render(request, 'deletemeetup.html', {'meetup': meetup})


def deletemeetupview(request, meetupid):
    meetup = Meetups.objects.get(id=meetupid)
    return render(request, 'deletemeetup.html', {'meetup': meetup})
