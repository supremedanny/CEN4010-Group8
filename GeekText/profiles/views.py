from urllib import request
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
import pyrebase

config={
	'apiKey': "AIzaSyCYylW6ebm5WJRb0TYiUBvTJPQxLTK_3uw",
	'authDomain': "cen4010-group8.firebaseapp.com",
	'databaseURL': "https://cen4010-group8-default-rtdb.firebaseio.com",
	'projectId': "cen4010-group8",
	'storageBucket': "cen4010-group8.appspot.com",
	'messagingSenderId': "1073702750284",
	'appId': "1:1073702750284:web:f4a2e8d7b2994ffa3b0ce9",
	'measurementId': "G-18KRKN3G8Q"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
db=firebase.database()
storage = firebase.storage()

#signin page
def signin(request):
    return render(request, "Login.html")

#after correct credentials
def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "Invalid Credentials!"
        return render(request, "Login.html",{"message": message})
    session_id = user['idToken']
    idtoken = request.session['uid'] = str(session_id)
    userinfo = authe.get_account_info(idtoken)
    userinfo = userinfo['users']
    print(userinfo)
    userinfo = userinfo[0]
    userinfo = userinfo['localId']

    email = db.child('Users').child(userinfo).child('Email').get().val()
    print(email+ "\n\n\n")
    return render(request, "Home.html")

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"Home.html")

def register(request):
    return render(request, "Registration.html")

def postregister(request):
    fname = request.POST.get('first_name')
    lname = request.POST.get('last_name')
    email = request.POST.get('email')
    pw = request.POST.get('pass')
    address = request.POST.get('address')
    zipcode = request.POST.get('zip_code')
    phone = request.POST.get('phone')
    

    try:
        #start point of creating user
        user = authe.create_user_with_email_and_password(email, pw)
        uid = user['localId']
        data={"First Name":fname,"Last Name":lname,"Email":email,"Password":pw,"Address":address,"Zip Code":zipcode,"Phone":phone}
        db.child("Users").child(uid).set(data)
    except:
        return render(request, "Registration.html")
    
    return render(request, "Home.html")
