from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from allauth.account.views import PasswordChangeView

from .forms import CustomUserChangeForm

# Create your views here.
class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('my-account')

class MyAccountPageView(UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'account/my_account.html'

    #see L10-T12 The View Section, things to note step 5 for why this is needed
    def get_object(self):
        return self.request.user