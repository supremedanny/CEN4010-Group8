from urllib import request
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

def home(request):
        #accessing our firebase data and storing it in a variable
        name = db.child('Data').child('Name').get().val()
        stack = db.child('Data').child('Stack').get().val()
        framework = db.child('Data').child('Framework').get().val()
    
        context = {
            'name':name,
            'stack':stack,
            'framework':framework
        }
        return render(request, 'Home.html', context)



