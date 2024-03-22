from django.shortcuts import render

# Create your views here.


def home(request):
    name="Akash"
    myDict={"name":name,"age":25}
    return render(request,"home.html",myDict)


def about(request):
    return render(request,"about.html")


def getInput(request):
    if(request.method=="POST"):
        name=request.POST.get("studentName")

        print("name\n\n",name)


    return render(request,"getInput.html")