from django.contrib import admin
from student.models import SchoolYear, Department, Semister, Module, Instructor, Block, Student, Subject, SubjectSchedule
# Register your models here.





admin.site.register(SchoolYear)
admin.site.register(Department)
admin.site.register(Semister)
admin.site.register(Module)
admin.site.register(Instructor)
admin.site.register(Block)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(SubjectSchedule)
