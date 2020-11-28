from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Notice,FAQ
from .forms import PostNoticeForm

# Create your views here.
def index(request):
    return render(request,'index.html')
def post_notice(request):
    if request.method=='POST':
        tech_name=request.POST['teachername']
        notice=request.POST['notice']
        branch=request.POST['branch']
        year=request.POST['year']
        section=request.POST['section']
        date=request.POST['date']
        n=Notice(teachername=tech_name,notice=notice,branch=branch,year=year,section=section,date=date)
        n.save()
        return redirect('post_success')
    else:
        return render(request,'post_notice.html')
def post_success(request):
    return render(request,'post_success.html')
def view_notice(request):
    n=Notice.objects.order_by('-year')[:10]
    return render(request,'view_notice.html',{'notice':n})
def view(request,notice_id):
    n=Notice.objects.get(id=notice_id)
    return render(request,'view.html',{'notice':n})
def post_notice1(request):
    if request.method=='POST':
        form=PostNoticeForm(request.POST)
        form.save()
        return redirect('post_success')
    else:
        form=PostNoticeForm()
        return render(request,'post_notice1.html',{'form':form})
def contact(request):
    return render(request,'contact.html')
def FAQ(request):
    if request.method=='POST' :
        name1=request.POST['names']
        email1=request.POST['email']
        query1=request.POST['query']
        p=FAQ(name=name1,email=email1,query=query1)
        p.save()
        return redirect('index')
    else:
        return render(request,'FAQ.html')
