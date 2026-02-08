from django import forms

INPUT_CLASS = ("w-full px-4 py-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-yellow-500 focus:border-transparent outline-none transition duration-200 my-4")

class formInput(forms.Form):
    duration = forms.IntegerField(widget=forms.NumberInput(attrs={'class':INPUT_CLASS,'placeholder':'Enter the timer duration:'}))
    interval = forms.IntegerField(widget=forms.NumberInput(attrs={'class':INPUT_CLASS,'placeholder':'Enter the timer interval:'}))
    msg = forms.CharField(widget=forms.TextInput(attrs={'class':INPUT_CLASS,'placeholder':'Enter your pop up message:'}))
    