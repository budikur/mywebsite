from django.http import HttpResponse
from django.shortcuts import render

# method view
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

# def about(request):
#     return HttpResponse("<h1> About </h1>")






# def index(request):
#     judul = "<h1> Hello World </h1>"
#     subjudul = "<h2> Welcome in my website </h2>"
#     output = judul+subjudul
#     return HttpResponse(output)
#
# def about(request):
#     return HttpResponse("<h1> About </h1>")