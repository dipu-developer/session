from django.shortcuts import render

#create the session with the cokies
#session is same like cookies but data are storedin the formate of name and key
def setsession(request):
    request.session['name'] = 'bhuam'          #this create session key is name and value is deepak
    request.session['surname'] = "bham"
    request.session.set_expiry(100)            #set the session in second and 0 second mean browserclose session close
    # request.session.set_expiry(0)            #the value of get_expire_at_brower_close() become true and it expire the
                                                #when the user close the window
    return render(request,'setsession.html')    #we dont have to send any other think it will first argument is session 

#featching the session
def getsession(request):
    # name = request.session['name']            #the value id none it will through the error
    name = request.session.get('name',default='Guest')  #if the user not present it will return the Guest
    # surname = request.session.get('surname',default='Guest surname')  #if the user not present it will return the Guest

    request.session.modified= True              #when we want to use to cheak the user is active mode or idel mode
                                                # when we need to expire the session when the given time of the user
                                                #is doing or not if doing nothink then session will expire otherwise 
                                                #session will increase

    #also we can print this value in home page without passing the any argument
    print(request.session.get_session_cookie_age())             #forfatching the session age in second
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())                    #at date in form
    print(request.session.get_expire_at_browser_close())        # return the boolean value 

    # return render(request,'getsession.html',{'name':name,'surname':surname})
    return render(request,'getsession.html',{'name':name})

def delsession(request):
    # if 'name'in request.session:
    #     del request.session['name']
    request.session.flush()                 #we have to clear the session from database otherwise it save thesesssion in the databae  
    request.session.clear_expired()         
    return render(request,'delsession.html')
