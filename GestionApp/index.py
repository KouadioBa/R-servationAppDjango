from django.http import HttpResponse
from django.shortcuts import render, redirect
from classe.models import Classes
from django.contrib.auth.models import User
from django.db.models import Q 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

@login_required(login_url='login')
def INDEX(request):
    emp = Classes.objects.all()

    context = {
        'emp':emp,
    }
    return render(request,'index.html',context)

@login_required(login_url='login')
def VIEWS(request):
    emp = Classes.objects.all()

    context = {
        'emp':emp,
    }
    return render(request,'index1.html',context)

def SINGIN(request):
    if request.method == "POST":
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(username=name).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('views')
            else:
                print("Mot de passe incorrect")
        else:
            print("L'utilisateur n'existe pas")
        # print("=="*5, " NEW POST:",name,password, "=="*5 )
    return render(request, 'login.html')

def REGISTER(request):
    error = False
    message = ""
    if request.method == "POST":
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)
        rpassword = request.POST.get('rpassword', None)

        if error == False:
            if password!=rpassword:
                error=True
                message="Les mots de passe de correspondent pas!"
        # exit
        user = User.objects.filter(Q(username=name) | Q(password=password)).first()
        if user:
            error=True
            message = f"Un utilisateur avec le pseudo {name} ou le mot de passe {password} existe déjà!"
        # register
        if error == False:
            user = User(
                username = name,
            )
            user.save()
            user.password = password
            user.set_password(user.password)
            user.save()
            return redirect('login')    
    context = {
        'error':error,
        'message':message
    }
    return render(request,'register.html', context)
# déconnexion
def LOGOUT(request):
    logout(request)
    return redirect('login')

def ADD(request):
    if request.method == "POST":
        entite = request.POST.get('entite')
        salle = request.POST.get('salle')
        intervenant = request.POST.get('intervenant')
        motif = request.POST.get('motif')
        classe = request.POST.get('classe')
        matiere = request.POST.get('matiere')
        date = request.POST.get('date')
        heure = request.POST.get('heure')

        emp = Classes(
            entite = entite,
            salle = salle,
            intervenant = intervenant,
            motif = motif,
            classe = classe,
            matiere = matiere,
            date = date,
            heure = heure,
        )
        emp.save()
        return redirect('home')

    return render(request, 'index.html')

def EDIT(request):
    emp = Classes.objects.all()

    context = {
        'emp':emp,
    }
    return render(request,'index.html',context)

def UPDATE(request,id):
    if request.method == "POST":
        entite = request.POST.get('entite')
        salle = request.POST.get('salle')
        intervenant = request.POST.get('intervenant')
        motif = request.POST.get('motif')
        classe = request.POST.get('classe')
        matiere = request.POST.get('matiere')
        date = request.POST.get('date')
        heure = request.POST.get('heure')

        emp = Classes(
            id = id,
            entite = entite,
            salle = salle,
            intervenant = intervenant,
            motif = motif,
            classe = classe,
            matiere = matiere,
            date = date,
            heure = heure,
        )
        emp.save()
        return redirect('home')

    return redirect(request,'index.html')

def DELETE(request, id):
    emp = Classes.objects.filter(id = id)
    emp.delete()
    context = {
        'emp':emp,
    }
    return redirect('home')