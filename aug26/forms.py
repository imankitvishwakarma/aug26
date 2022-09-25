from django import forms
class userform(forms.Form):
    num1=forms.CharField(label="num1")
    num2=forms.CharField(label="num2")
    