from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_guest:
            return redirect('guests:quiz_change_list')
        else:
            return redirect('admins:quiz_list')
    return render(request, 'logs/home.html')
