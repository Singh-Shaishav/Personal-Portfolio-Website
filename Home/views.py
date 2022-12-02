from django.shortcuts import render, HttpResponse
from Home.models import Contact, Project
from django.contrib import messages



def index(request):
    return render(request, 'index.html')

def resume(request):
    return render(request, 'Resume.html')


def project(request):
    allProject = Project.objects.all()
    context = {'allProject' : allProject}
    return render(request, 'Projects.html', context)

def contact(request):

    
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
           
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, "Your message have been sent successfuly")
    return render(request, 'Contact.html')

def search(request):
    query = request.GET['query']

    if len(query) > 70:
        allProject = Project.objects.none()
    else:
        allProjectName = Project.objects.filter(ProjectName__icontains=query)
        allProjectDescription = Project.objects.filter(ProjectDescription__icontains=query)
        allProject = allProjectName.union(allProjectDescription)
    params = {'allProject' : allProject, 'query' : query}
    return render(request, 'Search.html', params)