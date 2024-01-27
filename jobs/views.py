import html
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

# Create your views here.

# Cannot import send_email -- as the utility is incomplete - no SendGrid account/API Key
#   from common.utils.email import send_email  
from .forms import JobApplicationForm

class JobAppView(FormView):
    template_name = 'jobs/joke_writer.html'
    form_class = JobApplicationForm
    success_url = reverse_lazy('jobs:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'gregwills@live.com'
        subject = 'Application for Joke Writer'
        content = f'''<p>Hey HR Manager!</p>
            <p>Job application received:</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        # send_email(to, subject, content) -- I have no SendGrid API Key
        #   print instead
        print( '\n', to, '\n', subject, '\n', content, '\n' )

        return super().form_valid(form)

class JobAppThanksView(TemplateView):
    template_name = 'jobs/thanks.html'