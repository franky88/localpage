from django.shortcuts import render, get_object_or_404
from student.models import SchoolYear, Semister, Module, Instructor, Block, Student, Subject, SubjectSchedule
# Create your views here.
def studentIndex(request):
	student=Student.objects.all()
	context={
		"title": 'Student list',
		"student_list": student,
	}
	return render(request, "student/student_list.html", context)

def studentDetail(request, pk):
	instance=get_object_or_404(Student, pk=pk)
	context={
		"title": 'Student Detail',
		"instance": instance,
	}
	return render(request, "student/student_list.html", context)