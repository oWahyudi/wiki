from django import forms

# Create your forms classes here.

class ReadonlyTextInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        super(ReadonlyTextInput,self).__init__(*args,**kwargs)
        self.attrs['readonly']=True


class NewPageForm(forms.Form):
    title_field = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={'placeholder': 'Enter text','class':'textbox-medium'}),
        required=True
    )
    
    content_field = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={'placeholder': 'Enter text','class':'textarea-medium'}),
        required=True
    )

class EditPageForm(forms.Form):
    title_field = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={'placeholder': 'Enter text','class':'textbox-medium', 'readonly':'readonly'}),
        required=True
    )
    
    content_field = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={'placeholder': 'Enter text','class':'textarea-medium'}),
        required=True
    )

