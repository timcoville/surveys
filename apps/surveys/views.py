from django.shortcuts import render,redirect

def index(request):
    return render (request, "surveys/index.html")

def process(request):
    if "count" not in request.session:
        request.session['count'] = 0
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    print request.session
    return redirect("/result/")

def result(request):
    request.session['count'] += 1
    context = {
        "name": request.session['name'],
        "location": request.session['location'],
        "language": request.session['language'],
        "comment": request.session['comment'],
        "count": request.session['count']
    }
    return render(request, "surveys/result.html", context)

def back(request):
    return redirect("/")