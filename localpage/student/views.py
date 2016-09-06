from django.shortcuts import render
from student.models import SchoolYear, Semister, Module, Instructor, Block, Student, Subject, SubjectSchedule
# Create your views here.
def studentIndex(request):
	student=Student.objects.all()
	context={
		"title": 'Student list',
		"student_list": student,
	}
	return render(request, "student/student_list.html", context)