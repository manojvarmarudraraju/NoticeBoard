from django import forms
from .models import Notice
from django.utils import timezone
BRANCHES=[
    ('it','IT'),
    ('cse','CSE'),
    ('eee','EEE'),
    ('ece','ECE'),
    ('mec','MEC'),
    ('civil','CIVIL'),
    ('all','ALL BRANCHES'),
]
SECTION=[
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
    ('E','E'),
    ('F','F'),
    ('all','ALL SECTIONS'),
]
YEARS=[
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (0,'ALL YEARS'),
]
class PostNoticeForm(forms.ModelForm):
    branch=forms.CharField(widget=forms.Select(choices=BRANCHES))
    section = forms.CharField(widget=forms.Select(choices=SECTION))
    year = forms.IntegerField(widget=forms.Select(choices=YEARS))
    date=forms.DateTimeField(initial=timezone.now())
    class Meta:
        model=Notice
        fields=('teachername','notice','branch','section','year','date')