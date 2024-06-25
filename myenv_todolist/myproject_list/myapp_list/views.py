from django.shortcuts import redirect, render
from .forms import MyForm
from .models import MyappList

# Create your views here.
def home(request):
    myforms = MyForm()
    mydata = MyappList.objects.all()
    if mydata!=' ':
        context={'form':myforms,'mydata':mydata}
        return render(request,"home.html",context)
    else:
        context={'form':myforms}
        return render(request,"home.html",context)
    
def uploadtask(request):
    if request.method=='POST':
        form=MyForm(request.POST)
        if form.is_valid():
            try:
                form.save()               
                return redirect("home")
            except:
                pass
    else:      
        form=MyForm()  
    return render(request,'home.html',{'form':form})

def update(request,id):
    mydata=MyappList.objects.get(id=id)
    if request.method=='POST':
        title=request.POST['title']
        description=request.POST['description']
        status=request.POST['status']
        
        mydata.title=title
        mydata.description=description
        mydata.status=status
        mydata.save()
        return redirect('home')
    return render(request,"update.html",{'data':mydata})
        
        

def delete(request,id):
    data=MyappList.objects.get(id=id)
    data.delete()
    return redirect('home')