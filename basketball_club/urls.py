from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("joinus", views.joinus, name="joinus"),
    path("joinus/<str:studentid>/", views.joinus, name="joinus"),


    path("login", views.login, name="login"),

    path("meetups", views.meetups, name="meetups"),
    path("meetups/<str:studentid>/", views.meetups, name="meetups"),


    path("members", views.members, name="members"),
    path("members/<str:studentid>/", views.members, name="members"),


    path("lecturerregister", views.lecturerregister, name="lecturerregister"),
    path("lecturerregister/<str:studentid>/",
         views.lecturerregister, name="lecturerregister"),


    path("tournaments", views.tournaments, name="tournaments"),
    path("tournaments/<str:studentid>/", views.tournaments, name="tournaments"),


    path("profile", views.profile, name="profile"),
    path("profile/<str:studentid>/", views.profile, name="profile"),

    path("update/", views.update, name="update"),
    path("update/<str:studentid>/", views.update, name="update"),
    path("updatedata/<str:studentid>/", views.updatedata, name="updatedata"),

    path("delete", views.delete, name="delete"),
    path("delete/<str:studentid>/", views.delete, name="delete"),
    path("viewdelete/<str:studentid>/", views.viewdelete, name="viewdelete"),

    path("updatemeetup", views.updatemeetup, name="updatemeetup"),
    path('createmeetup/', views.createmeetup, name='createmeetup'),
    path('updatemeetup/<int:meetupid>/',
         views.updatemeetup, name='updatemeetup'),

    path("delete", views.delete, name="delete"),
    path("viewdelete/<int:studentid>/", views.viewdelete, name="viewdelete"),
    path("deletemeetup/<int:meetupid>/",
         views.deletemeetup, name="deletemeetup"),

    path('logout/', views.logout, name='logout'),

]
