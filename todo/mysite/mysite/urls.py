"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
 #Import View from myapp to mysite
from myapp import views
urlpatterns = [
    #For admin site
    path('admin/', admin.site.urls),
    #Pass the index view to the path from view.py
    #name= is to define the name of our url
    #Display in the index page
    path('',views.index,name='index'),
    #taskid because we passed taskid in the views.py
    path('delete/<int:taskid>/',views.delete,name='delete'),
    #for edit/update functionality
    path('update/<int:id>/',views.update,name='update'),
    #cbv=class based view
    path('cbvindex/',views.TaskListView.as_view(),name='cbvindex'),
    #Generic views should be called as a primary key
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),
]

