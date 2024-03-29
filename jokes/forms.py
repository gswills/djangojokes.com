from django.forms import ModelForm, Textarea

from .models import Joke

class JokeForm(ModelForm):
    class Meta:
        model = Joke
        fields = ['question', 'answer','category','tags']
        widgets = {
            'question': Textarea(
                attrs={'cols': 80, 'rows': 3, 'autofocus': True}
            ),
            'answer': Textarea(
                attrs={'cols': 80, 'rows': 2, 'placeholder': 'Make it funny!'}
            )
        }
        help_texts = {
            'question': 'Please, no dirty jokes.',
            'tags': 'To select multiple tags: On Windows use Ctrl-click, on Mac use Command-click'
        }