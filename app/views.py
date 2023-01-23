from django.shortcuts import render

#create the session with the cokies
#session is same like cookies but data are storedin the formate of name and key
def setsession(request):
    request.session['name'] = 'deepak'          #this create session key is name and value is deepak
    request.session['surname'] = "sharma"
    request.session.set_expiry(2000)            #set the session in second and 0 second mean browserclose session close
    return render(request,'setsession.html')    #we dont have to send any other think it will first argument is session 

#featching the session
def getsession(request):
    # name = request.session['name']
    name = request.session.get('name',default='Guest')  #if the user not present it will return the Guest
    surname = request.session.get('surname',default='Guest surname')  #if the user not present it will return the Guest

    #also we can print this value in home page without passing the any argument
    print(request.session.get_session_cookie_age())             #forfatching the session age in second
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())                    #at date in form
    print(request.session.get_expire_at_browser_close())        # return the boolean value 

    return render(request,'getsession.html',{'name':name,'surname':surname})

def delsession(request):
    if 'name'in request.session:
        del request.session['name']
    return render(request,'delsession.html')