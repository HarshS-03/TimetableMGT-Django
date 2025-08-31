from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def viewtimetable(request):
    timetable = [
        {"day": "Monday", "time": "9:00 - 11:00", "subject": "Python (GPU)", "teacher": "-", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Monday", "time": "11:00 - 12:00", "subject": "Python", "teacher": "Dr. Suchit Purohit", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Monday", "time": "12:00 - 1:00", "subject": "Artificial Intelligence", "teacher": "Ms. Anju Jha", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Monday", "time": "2:00 - 3:00", "subject": "Mathematical Foundation", "teacher": "Mr. Vishal Prajapati", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Monday", "time": "3:00 - 4:00", "subject": "OOCP", "teacher": "Dr. Jigna Satani", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Tuesday", "time": "9:00 - 11:00", "subject": "Python (GPU)", "teacher": "-", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Tuesday", "time": "11:00 - 12:00", "subject": "Mathematical Foundation", "teacher": "Mr. Vishal Prajapati", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Tuesday", "time": "12:00 - 1:00", "subject": "Linear Algebra & Numerical Methods", "teacher": "Ms.Arpana Sonawane", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Tuesday", "time": "2:00 - 3:00", "subject": "Python", "teacher": "Dr. Suchit Purohit", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Tuesday", "time": "3:00 - 4:00", "subject": "Artificial Intelligence", "teacher": "Ms. Anju Jha", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Wednesday", "time": "9:00 - 11:00", "subject": "OOCP", "teacher": "-", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Wednesday", "time": "11:00 - 12:00", "subject": "Python", "teacher": "Dr. Suchit Purohit", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Wednesday", "time": "12:00 - 1:00", "subject": "Linear Algebra & Numerical Methods", "teacher": "Ms.Arpana Sonawane", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Wednesday", "time": "2:00 - 3:00", "subject": "OOCP", "teacher": "Dr. Jigna Satani", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Wednesday", "time": "3:00 - 4:00", "subject": "Artificial Intelligence", "teacher": "Ms. Anju Jha", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Thursday", "time": "9:00 - 11:00", "subject": "OOCP", "teacher": "-", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Thursday", "time": "11:00 - 12:00", "subject": "Mathematical Foundation", "teacher": "Mr. Vishal Prajapati", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Thursday", "time": "12:00 - 1:00", "subject": "Linear Algebra & Numerical Methods", "teacher": "Ms.Arpana Sonawane", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Thursday", "time": "2:00 - 3:00", "subject": "OOCP", "teacher": "Dr. Jigna Satani", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Thursday", "time": "3:00 - 4:00", "subject": "Artificial Intelligence", "teacher": "Ms. Anju Jha", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Friday", "time": "9:00 - 11:00", "subject": "Project", "teacher": "-", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Friday", "time": "11:00 - 12:00", "subject": "Python", "teacher": "Dr. Suchit Purohit", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Friday", "time": "12:00 - 1:00", "subject": "Linear Algebra & Numerical Methods", "teacher": "Ms.Arpana Sonawane", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Friday", "time": "2:00 - 3:00", "subject": "OOCP", "teacher": "Dr. Jigna Satani", "room": "4", "course": "M.Sc. AI&ML", "year": "1"},
        {"day": "Friday", "time": "3:00 - 4:00", "subject": "Mathematical Foundation", "teacher": "Mr. Vishal Prajapati", "room": "4", "course": "M.Sc. AI&ML", "year": "1"}
    ]
    
    faculty = request.GET.get('faculty', '').strip()
    subject = request.GET.get('subject', '').strip()
    course = request.GET.get('course', '').strip()
    year = request.GET.get('year', '').strip()
    
    filtered = timetable

    if faculty:
        filtered = [t for t in filtered if t['teacher'] == faculty]
    if subject:
        filtered = [t for t in filtered if t['subject'] == subject]
    if course:
        filtered = [t for t in filtered if t['course'] == course]
    if year:
        filtered = [t for t in filtered if t['year'] == year]

    # --- NEW LOGIC FOR YEAR OPTIONS ---
    if course in ['M.Sc. AI&ML', 'MCA']:
        year_options = ['1', '2']
    else:
        # Default for other courses like 'M.Sc. Computer Science'
        year_options = ['1', '2', '3', '4', '5']

    context = {
        "timetable": filtered,
        "faculty_filter": faculty,
        "subject_filter": subject,
        "course_filter": course,
        "year_filter": year,
        "year_options": year_options
    }

    return render(request, 'viewtimetable.html', context)

def manangetimetable(request):
    return render(request, 'managetimetable.html')