from django.db import models

class Course(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=100)
    c_semester = models.CharField(max_length=50)

    class Meta:
        db_table = 'Course'
        managed = True
        
    
class Faculty(models.Model):
    f_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=100)
    f_subject = models.CharField(max_length=100)

    class Meta:
        db_table = 'Faculty'
        managed = True

class Subject(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=100)
    s_credits = models.IntegerField()
    s_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Subject'
        managed = True

class FacultySubject(models.Model):
    f_name = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    s_name = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        db_table="Faculty's Subject"
        unique_together = ('f_name', 's_name')

class Timeslot(models.Model):
    t_id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        db_table = 'Timeslot'
        managed = True

class Classroom(models.Model):
    r_id = models.AutoField(primary_key=True)
    r_name = models.CharField(max_length=50)
    r_capacity = models.IntegerField()
    r_type = models.CharField(max_length=50)

    class Meta:
        db_table = 'Classroom'
        managed = True

class Timetable(models.Model):
    timetable_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    room = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50)

    class Meta:
        db_table = 'Timetable'
        managed = True