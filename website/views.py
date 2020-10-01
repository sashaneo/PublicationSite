from django.shortcuts import render, redirect
from datetime import datetime
from BlogSite.settings import PUBLISH_PASSWORD
from .models import Contact, Publication, FeedbackForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .weather import get_weather_today


def index(request):
    city_id = 706483
    appid = "e14a34b19e13c330d813b9b5901a3d9c"
    weather = get_weather_today(city_id, appid)
    return render(request, 'index.html', {'weather': weather})


def contacts(request):
    if request.method == 'POST':
        amn = request.POST.get('name', '')
        ame = request.POST.get('email', '')
        mt = request.POST.get('text', '')

        if not amn or not ame or not mt:
            return render(request, 'contacts.html', {'error': 'Empty field!'})

   
        FeedbackForm.objects.create(author_message_name=amn,
                                    author_message_email=ame,
                                    message_text=mt)

        return render(request, 'contacts.html', {'MessageOk': 'Your message was successfully sent!'})

    contact_details = Contact.objects.all()
    return render(request, 'contacts.html', context={
        'contact_details': contact_details,
    })


def publications(request):

 
    if request.POST.get('q'):
        search_req = request.POST.get('q')
        publication_object = Publication.objects.filter(title__icontains=search_req).order_by('-date')

        #Pagination NEED REFACTOR FOR 'DRY'
        paginator = Paginator(publication_object, 10)  # 10 posts in each page
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            posts = paginator.page(paginator.num_pages)
   
        qty = publication_object.count()
        search_info = 'Search results qty: ' + str(qty)
        search_info = f'Number of results by "{search_req}" : {qty}'

        return render(request, 'publications.html', context={
            'posts': posts,
            'search_info': search_info,
            'page': page,
            'servertime': datetime.now(),

        })

    publication_object = Publication.objects.all().order_by('-date')

    #Pagination

    paginator = Paginator(publication_object, 10)  # 10 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'publications.html', context={
        'page': page,
        'posts': posts,
        'servertime': datetime.now(),
    })


def publication(request, pk):
    try:
        publication_ = Publication.objects.get(id=pk)
        return render(request, 'publication.html', context={'publication': publication_})
    except Publication.DoesNotExist:
        return redirect('/publications')


def publish(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        title = request.POST.get('title', '').strip()
        text = request.POST.get('text', '').strip()

        if not password or not title or not text:
            return render(request, 'publish.html', {'error': 'Empty field!'})
        if password != PUBLISH_PASSWORD:
            return render(request, 'publish.html', {'error': 'Incorrect password!'})

        publication = Publication(title=title, text=text)
        publication.save()
        return redirect('/publications/' + str(publication.id))

    return render(request, 'publish.html')

def about(request):
    return render(request, 'about.html')



