from django.shortcuts import render

#create the session with the cokies
#session is same like cookies but data are storedin the formate of name and key
def setsession(request):
    request.session['name'] = 'deepak'          #this create session key is name and value is deepak
    request.session['surname'] = "sharma"
    return render(request,'setsession.html')    #we dont have to send any other think it will first argument is session 

#featching the session
def getsession(request):
    # name = request.session['name']
    name = request.session.get('name',default='Guest')  #if the user not present it will return the Guest
    surname = request.session.get('surname',default='Guest surname')  #if the user not present it will return the Guest
    return render(request,'getsession.html',{'name':name,'surname':surname})

def delsession(request):
    if 'name'in request.session:
        del request.session['name']
    return render(request,'delsession.html')