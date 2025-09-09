from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password,check_password
from .models import Faculty


def index(request):
    return render(request, 'index.html')

def viewtimetable(request):
    return render(request, "viewtimetable.html")

def about(request):
    return render(request,"about.html")

def home(request):
    faculty = None
    faculty_id = request.session.get('faculty_id')
    if faculty_id:
        try:
            faculty = Faculty.objects.get(id=faculty_id)
        except Faculty.DoesNotExist:
            pass
    return render(request, 'home.html', {'faculty': faculty})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        subject = request.POST.get('subject')

        if not username or not password or not confirm_password:
            return render(request, "accounts/register.html", {"error": "All fields are required."})

        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        
        if not subject:
               error = "Subject is required"
               return render(request, 'register.html', {'error': error})
        
        if Faculty.objects.filter(name=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        
        secure = make_password(password)
        
        faculty = Faculty.objects.create(name=username, password=secure,subject=subject)
        faculty.save()
        return render(request, 'login.html', {'success': 'Registration successful. Please log in.'})
         
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
 
        if not username or not password:
            return render(request, 'login.html', {'error': 'Please enter both username and password.'})
 
        try:
            user = Faculty.objects.get(name=username)
        except Faculty.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
 
        
        if not check_password(password, user.password):
            return render(request, 'login.html', {'error': 'Incorrect password.'})

        request.session['faculty_id'] = user.id
        return redirect('/')  
    return render(request, 'login.html')

def profile(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        return redirect('login')
    
    faculty = Faculty.objects.get(id=faculty_id)

    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not check_password(old_password, faculty.password):
            return render(request, 'profile.html', {'faculty': faculty, 'error': 'Current password is incorrect.'})
        
        if new_password != confirm_password:
            return render(request, 'profile.html', {'faculty': faculty, 'error': 'New passwords do not match.'})
 
        faculty.password = make_password(new_password)
        faculty.save()

        return render(request, 'profile.html', {'faculty': faculty, 'success': 'Password updated successfully.'})

    return render(request, 'profile.html', {'faculty': faculty})



def logout(request): 
    if 'faculty_id' in request.session:
        del request.session['faculty_id']
    return redirect('home') 

def managetimetable(request):
    return render('managetimetable.html')