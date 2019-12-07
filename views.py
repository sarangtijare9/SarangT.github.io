from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request,'index.html')


def analyze(request):
    dText=(request.POST.get("Text","default"))
    rmp=(request.POST.get("removepunc","Off"))
    NL = (request.POST.get("Newlinechar","Off"))
    SR = (request.POST.get("Spaceremover", "Off"))
    UP = (request.POST.get("uppercase", "Off"))


    if rmp=="on":




            perfect=""
            punc=''':,.></\][{}^#!'"[]?;'''
            for x in dText:
                if x not in punc:


                        perfect = perfect +  x

            act = {'analyse': perfect}
            dText=perfect


    if NL=="on":

        perfect=""
        for x in dText:
            if x != "\n" and x !="\r":
                perfect = perfect + x

        act = {'analyse': perfect}
        dText=perfect



    if UP =="on":

            perfect =""
            for x in dText:
                perfect = perfect + x.upper()

            act = {'analyse': perfect}
            dText=perfect

    if SR == "on":

        perfect = ""
        for index,x in enumerate(dText):
            if not(dText[index] == " " and dText[index+1]==" "):
                perfect = perfect + x

        act = {'analyse': perfect}


    if(rmp!="on" and NL!="on" and SR != "on" and UP !="on"):
        return HttpResponse('''<h1>ERROR.....<br>
                               please click on check Button</h1>''')


    return render(request, 'analyze.html', act)