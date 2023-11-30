from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count


from .forms import AuthorForm, QuoteForm
from quotes.models import Quote, Tag, Author


# Create your views here.
# from .utils import get_mongodb

# # def main(request):
# def main(request, page=1):
#     db = get_mongodb()
#     quotes = db.quotes.find()
#     per_page = 5
#     paginator = Paginator(list(quotes), per_page)
#     quotes_on_page = paginator.page(page)
#     return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})
    # return render(request, 'quotes/index.html', context={})



def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 5 #qutes per page
    paginator = Paginator(list(quotes), per_page) 
    quotes_on_page = paginator.page(page)

    top_tags = Tag.objects.annotate(tag_count=Count('quote')).order_by('-tag_count')[:10]

    return render(request, "quotes/index.html", context={'quotes': quotes_on_page, 'top_tags': top_tags})

def about(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {
        'fullname': author.fullname,
        'born_date': author.born_date,
        'born_location': author.born_location,
        'description': author.description,
    }
    return render(request, 'quotes/about.html', context)


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save()
        
            return redirect("quotes:about", author_id=new_author.id)

    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save()
            return render(request, "quotes/view_quote.html", context={'quote': quote}) 
 
    else:
        form = QuoteForm()
    
    return render(request, 'quotes/add_quote.html', {'form': form})

def tag_quotes(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    quotes = Quote.objects.filter(tags=tag)
    paginator = Paginator(quotes, 10)

    page = request.GET.get('page')
    try:
        quotes = paginator.page(page)
    except PageNotAnInteger:
        quotes = paginator.page(1)
    except EmptyPage:
        quotes = paginator.page(paginator.num_pages)

    context = {
        'tag': tag,
        'quotes': quotes,
    }

    return render(request, 'quotes/tag_quotes.html', context)