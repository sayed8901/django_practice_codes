from django import forms
import datetime
from first_app.models import Model_data

class sample_form(forms.Form):
    name = forms.CharField(initial='Md. Sayed Hossain', max_length=20)
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs = {'rows':3, 'placeholder': 'Leave a comment'}), help_text="You may skip this if you dont want to leave a comment")
    email = forms.EmailField(label='Please enter your email address')

    value = forms.DecimalField()

    # date with initial value
    date = forms.CharField(initial=datetime.date.today,widget=forms.DateInput(attrs={'type':'date'}))

    # date time local
    birthday = forms.CharField(label='Birth Day', widget=forms.DateInput(attrs={'type':'datetime-local'}))

    # single year choice field with custom year range
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    # single year choice field with radio btn
    FAVORITE_COLORS_CHOICES = [
      ('blue', 'Blue'), ('green', 'Green'), ('black', 'Black')
    ]
    # favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)

    # multiple choice field with checkbox
    FAVORITE_COLORS_CHOICES = [
      ('blue', 'Blue'), ('green', 'Green'), ('black', 'Black')
    ]
    # favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    multiple_favorite_color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    
    agree = forms.BooleanField()




class sample_model_form(forms.ModelForm):
    class Meta:
        model = Model_data
        fields = '__all__'

        
