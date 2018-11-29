from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    """ Widok do rejestracji"""
    template_name = 'registration/signup.html'


def home(request):
    """ Widok po zalogowaniu, sprawdza czy ktoś jest studentem czy nauczycielem """
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:quiz_change_list')
        else:
            return redirect('students:quiz_list')
    return render(request, 'classroom/home.html')