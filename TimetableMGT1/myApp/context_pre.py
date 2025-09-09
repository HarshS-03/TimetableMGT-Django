from .models import Faculty
def current_faculty(request):
    faculty = None
    faculty_id = request.session.get('faculty_id')
    if faculty_id:
        try:
            faculty = Faculty.objects.get(id=faculty_id)
        except Faculty.DoesNotExist:
            faculty = None
    return {'faculty': faculty}