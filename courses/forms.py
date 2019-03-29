from django import forms
from django.core import validators
BIRTH_YEAR_CHOICES = range(1982,1990)#('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)
FRUIT_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)


class Suggestion(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label='please enter the same email address')
    suggestion=forms.CharField(widget=forms.Textarea)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
#    favorite_colors = forms.ChoiceField(
#        required=False,
#        widget=forms.CheckboxSelectMultiple(),
#        choices=FAVORITE_COLORS_CHOICES,
#    )
#    favorite_fruit= forms.CharField(
#        label='What is your favorite fruit?', 
#        widget=forms.Select(choices=FRUIT_CHOICES))


    
    def clean(self):
        cleaned_data= super().clean()
        email=cleaned_data.get('email')
        verify_email= cleaned_data.get('verify_email')

        if email!=verify_email:
            raise forms.ValidationError('Please enter same email address on both fields')