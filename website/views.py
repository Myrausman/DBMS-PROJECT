# <-------------------imports---------------->
from django.shortcuts import render,redirect,get_object_or_404
import random
from database.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import sqlite3,os,datetime,random,string
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

#<----------- Create your views here.--------->
def home(request):
    if request.method == 'POST':
            login = Login.objects.filter(email=request.POST.get('email')).first()
            return render(request, 'index.html', {'email':login.email,'login':True})
    return render(request, 'index.html', {})




def ask_view(request):
    return render(request, 'ask.html', {})
def mytopics_view(request):
    
    return render(request, 'mytopics.html')
def login(request):
    return render (request,'login.html',{})

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import sqlite3
import random
import string

@csrf_exempt
def register(request):
    if request.method == 'POST':
        # Retrieve the form data
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')


        # Insert the user data into the database
        with sqlite3.connect('datbase.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users ( fname, lname, email, password, gender) VALUES ( ?, ?, ?, ?, ?)",
                           ( first_name, last_name, email, password, gender))

        return redirect('home')

    return render (request,'register.html',{})


def details(request):
    if request.method=='POST':
         questionTitle=request.POST['questionTitle']
         questionDetails=request.POST['questionDetails']
         tags=request.POST['tags']
         question=Question.objects.create(
              title=questionTitle,
              details=questionDetails,
              tag=tags
         )
         question.save()
         return redirect('/details')

    return render (request,'details.html',{})