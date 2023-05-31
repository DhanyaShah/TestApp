from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from testdb.models import Teacher
import json

# Create your views here.

def home_page(request):
    template = loader.get_template('test.html')
    teacher_objs = Teacher.objects.get(id=1)
    json_data = json.dumps(teacher_objs.students)
    context = {
    'Teachers': teacher_objs,
    'Students': json_data,}
    return HttpResponse(template.render(context, request))

def t_detail(request, teacher_id):
    # teacher = get_object_or_404(Teacher, id = teacher_id)
    return render(request, 't_detail.html', {'name': teacher_id})