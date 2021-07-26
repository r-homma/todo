from django import forms# フォーム用のフィールドを使う宣言
from .models import MyToDoList

# your code...
# Add Form
class todoAddForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    contents = forms.CharField(label="Contents", widget=forms.Textarea)
    deadline = forms.DateField(label="Deadline")

class todoDeleteForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    contents = forms.CharField(label="Contents", widget=forms.Textarea)
    entryDate = forms.DateField(label="Entry Date")
    deadline = forms.DateField(label="Deadline")
    done = forms.BooleanField(label="Completed?", required=False)# required=Falseで空のデータを送ることができる

class todoEditForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    contents = forms.CharField(label="Contents", widget=forms.Textarea)
    deadline = forms.DateField(label="Deadline")
    done = forms.BooleanField(label="Completed?", required=False)
