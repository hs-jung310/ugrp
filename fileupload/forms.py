# fileupload/forms.py
from django.forms import ModelForm
from .models import FileUpload

class FileUploadForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = [ 'imgfile', 'content']
        # labels = {
        #     'title': '제목',
        #     'imgfile': '이 미 지',
        #     'content': 'content',
        # }
