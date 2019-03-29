from  django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Course
from .models import Step
from .import forms

def course_list(request):

    courses = Course.objects.all()
    return render (request, 'courses/course_list.html', {'courses':courses} )


def course_detail(request, pk):

    course=get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html',{'course':course})

def step_detail(request, course_pk, step_pk):

    step=get_object_or_404(Step, course_id=course_pk, id=step_pk)
    return render(request, 'courses/step_detail.html',{'step':step})

def suggestion_view(request):
    form=forms.Suggestion()
    if request.method == 'POST': #if the form on the webpage returns apost rquest ie tclicking the submit button on the html page
        form=forms.Suggestion(request.POST) #takes all the form data we put in the form and put it on the form
        if form.is_valid():
            print('its a valid form')
            send_mail(
                'Suggestion form{}'.format(form.cleaned_data['name']),
                form.cleaned_data['suggestion'],
                '{name} <{email}>'.format(**form.cleaned_data),
                ['hkv@core.com']
            )
            messages.add_message(request, messages.SUCCESS, 'tHANKS FOR YOUR SUGGESTIONS')
            return HttpResponseRedirect(reverse('suggestion'))
    return render(request, 'courses/suggestion_form.html',  {'form':form})
