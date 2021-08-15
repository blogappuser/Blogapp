from todoapp.models import Post
from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Userdata(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')

class Createnewpost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name','report_description','post_description','post_description1','post_description2','section_name','section_name1','section_name2',)

        # 'post_image','post_image1','post_image2'

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'report_description' : forms.Textarea(attrs={'class':'form-control','rows': 3,'cols':40}),
            'section_name':forms.TextInput(attrs={'class':'form-control'}),
            'post_description' : forms.Textarea(attrs={'class':'form-control m-3','rows': 2,'cols':4}),
            'section_name1':forms.TextInput(attrs={'class':'form-control'}),
            'post_description1' : forms.Textarea(attrs={'class':'form-control m-3','rows': 2,'cols':4}),
            'section_name2':forms.TextInput(attrs={'class':'form-control'}),
            'post_description2' : forms.Textarea(attrs={'class':'form-control m-3','rows': 2,'cols':4}),
            
        }

        
        # 'post_image':forms.FileInput(attrs={'name':"post_image",  'class':"custom-file-input",'id':"inputGroupFile01", 'aria-describedby':"inputGroupFileAddon01"}),
        #     'post_image1':forms.FileInput(attrs={'name':"post_image1", 'class':"custom-file-input",'id':"inputGroupFile01", 'aria-describedby':"inputGroupFileAddon01"}),
        #     'post_image2':forms.FileInput(attrs={'name':"post_image2", 'class':"custom-file-input",'id':"inputGroupFile01", 'aria-describedby':"inputGroupFileAddon01"}),


        
# custom-file-input
# name="post_image1" class="custom-file-input post_fields" id="inputGroupFile01" aria-describedby="inputGroupFileAddon01"