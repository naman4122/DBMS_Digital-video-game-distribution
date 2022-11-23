from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from videogame.models import game, tournament, user
from videogame.forms import userforms
from django.db import connection

def index(request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def showuser(request):
    showall=user.objects.all()
    context = {
        'data': showall
    }
    return render(request,'showuser.html',context)

def Insertuser(request):
    if request.method=="POST":
        if request.POST.get('user_id') and request.POST.get('user_name') and request.POST.get('country') and request.POST.get('u_age') and request.POST.get('pincode') and request.POST.get('city') and request.POST.get('passwords') :
            saverecord = user()
            saverecord.user_id=request.POST.get('user_id')
            saverecord.user_name=request.POST.get('user_name')
            saverecord.country=request.POST.get('country')
            saverecord.u_age=request.POST.get('u_age')
            saverecord.pincode=request.POST.get('pincode')
            saverecord.city=request.POST.get('city')
            saverecord.passwords=request.POST.get('passwords')
            saverecord.save()
            messages.success(request,'User '+saverecord.user_name+' is saved successfully..!')
            return render(request,'Insertuser.html')
    else:
        return render(request, 'Insertuser.html')
    
def showgame(request):
    showall=game.objects.all()
    context = {
        'data': showall
    }
    return render(request,'showgame.html',context)


def Insertgame(request):
    if request.method=="POST":
        if request.POST.get('game_id') and request.POST.get('game_name') and request.POST.get('game_type') and request.POST.get('age_rest') and request.POST.get('rate') :
            saverecord = game()
            saverecord.game_id=request.POST.get('game_id')
            saverecord.game_name=request.POST.get('game_name')
            saverecord.game_type=request.POST.get('game_type')
            saverecord.age_rest=request.POST.get('age_rest')
            saverecord.rate=request.POST.get('rate')
            saverecord.save()
            messages.success(request,'Game '+saverecord.game_name+' is saved successfully..!')
            return render(request,'Insertgame.html')
    else:
        return render(request, 'Insertgame.html')
    
def showtournament(request):
    showall=tournament.objects.all()
    context = {
        'data': showall
    }
    return render(request,'showtournament.html',context)

def Inserttournament(request):
    if request.method=="POST":
        if request.POST.get('tournament_id') and request.POST.get('tournament_name') and request.POST.get('tournament_type') and request.POST.get('prize') :
            saverecord = tournament()
            saverecord.tournament_id=request.POST.get('tournament_id')
            saverecord.tournament_name=request.POST.get('tournament_name')
            saverecord.tournament_type=request.POST.get('tournament_type')
            saverecord.prize=request.POST.get('prize')
            saverecord.save()
            messages.success(request,'Tournament '+saverecord.tournament_name+' is saved successfully..!')
            return render(request,'Inserttournament.html')
    else:
        return render(request, 'Inserttournament.html')

def Deluser(request,id):
    DeluserObj=user.objects.get(user_id=id)
    DeluserObj.delete()
    showall=user.objects.all()
    messages.success(request,'Record deleted succesfully!!')
    context={
        "user":DeluserObj
    }
    return render(request,'Deluser.html',context)

def Delgame(request,id):
    DelgameObj=game.objects.get(game_id=id)
    DelgameObj.delete()
    showall=game.objects.all()
    messages.success(request,'Record deleted succesfully!!')
    context={
        "game":DelgameObj
    }
    return render(request,'Delgame.html',context)

def Deltournament(request,id):
    DeltournamentObj=tournament.objects.get(tournament_id=id)
    DeltournamentObj.delete()
    showall=tournament.objects.all()
    messages.success(request,'Record deleted succesfully!!')
    context={
        "tournament":DeltournamentObj
    }
    return render(request,'Deltournament.html',context)

def sortuser(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=user.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'sortuser.html',context)
    else:
        return render(request,'sortuser.html')
    
def sortgame(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=game.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'sortgame.html',context)
    else:
        return render(request,'sortgame.html')
    
def sorttournament(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=tournament.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'sorttournament.html',context)
    else:
        return render(request,'sorttournament.html')
    
def edituser(request,id):
    Edituser=user.objects.get(user_id=id)
    return render(request,'Edituser.html',{"user":Edituser})
 
def updateuser(request,id):
    Updateuser=user.objects.get(user_id=id)
    form=userforms(request.POST,instance=Updateuser)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updates succesfully!!')
        return render(request,'Edituser.html',{"user":Updateuser})
    
def InputCustomQuery(request):
    return render(request, 'Query.html', {})


def runQueryuser(request):
    raw_query = "select \"User\".\"user_id\",\"User\".\"user_name\",\"User\".\"country\",\"User\".\"u_age\",\"User\".\"pincode\",\"User\".\"city\",\"User\".\"passwords\" from \"User\" "
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()

    return render(request, 'Query.html', {'data': alldata})


def ProcessCustomQuery(request):
    raw_query = request.POST.get('query')

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    print(alldata)

    return render(request, 'runQueryuser.html', {'data':alldata,'colnames':colnames, 'lencol':range(len(colnames))})