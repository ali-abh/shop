from django.shortcuts import render
from django.http import HttpResponse
from makeup.models import Shop,Skincare,Makeup,Digitalstuff,Comment

# Create your views here.
def Shops(request):
    shops = Shop.objects.all()
    context = {
        "shoplist":shops

    }
    return render(request,"makeup/shoplist.html",context)

def shop_details(request, shop_id):
    shop = Shop.objects.get(pk = shop_id)
    
    context = {
        "shopha":shop,
        
        }
    return render(request, "makeup/shop_details.html",context)


def allposts(request): 
    makeup_posts = Makeup.objects.all()
    skincare_posts = Skincare.objects.all()
    digitalstuff_posts = Digitalstuff.objects.all()
    context = {
        "makeupposts":makeup_posts,
        "skincareposts":skincare_posts,
        "digitalstufposts":digitalstuff_posts,
    }
    return render(request, "makeup/allposts.html",context)


# def makeup_comments(request, post_id):
#     comments = Makeup.objects.get(pk = post_id) 
    
#     context = {
#         "Mcomments" : comments,
#     }
#     return render(request,"makeup/comments.html",context)


# def skincare_comments(request, pk_id):
#     comments = Skincare.objects.get(pk = pk_id) 
    
#     context = {
#         "Scomments" : comments,
#     }
#     return render(request,"makeup/comments.html",context)


# def digitalstuf_comments(request, p_id):
#     comments = Digitalstuff.objects.get(pk = p_id) 
    
#     context = {
#         "Dcomments" : comments,
#     }
#     return render(request,"makeup/comments.html",context)