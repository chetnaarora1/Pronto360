from urllib import request
from django.shortcuts import render

def index(request):
    return render(request, 'index-2.html')

def services(request):
    return render(request, 'grid-listings-filterstop-search-aside.html')

def blog(request):
    return render(request, 'blog.html')

def account(request):
    return render(request, 'account.html')

def faq(request):
    return render(request, 'faq.html')

def help(request):
    return render(request, 'help.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def contacts(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')

def admin_dashboard(request):
    return render(request, 'admin_section/index.html')

def detail_restaurant(request):
    return render(request, 'detail-restaurant.html')

def media_gallery(request):
    return render(request, 'media-gallery.html')

def checkout(request):
    return render(request, 'checkout.html')

def sidebarsearch(request):
    return render(request, 'grid-listings-filterscol.html')

def fullsearch(request):
    return render(request, 'grid-listings-filterstop.html')

def fullisotope(request):
    return render(request, 'grid-listings-isotope.html')

def listingmap(request):
    return render(request, "listing-map.html")

def confirm(request):
    return render(request, 'confirm.html')

def bookings(request):
    return render(request, 'bookings.html')

def detail_hotel(request):
    return render(request, 'detail-hotel.html')

def detail_shop(request):
    return render(request, 'detail-shop.html')

def detailcarousel(request):
    return render(request, 'detail-carousel.html')

def detailcarousel_2(request):
    return render(request, 'detail-carousel-2.html')

def err_404(request):
    return render(request, '404.html')

def contacts2(request):
    return render(request, 'contacts-2.html')

def pricing_tables(request):
    return render(request, 'pricing-tables.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def menu_options(request):
    return render(request, 'menu-options.html')

def invoice(request):
    return render(request, 'invoice.html')

def blogpost(request):
    return render(request, 'blog-post.html')


def filterscolsearchaside(request):
    return render(request, 'grid-listings-filterscol-search-aside.html')

def filterstopsearchaside(request):
    return render(request, 'grid-listings-filterstop-search-aside.html')

def searchasideopenstreetmap(request):
    return render(request, 'grid-listings-filterscol-search-aside-openstreetmap.html')

def stopopenstreetmap(request):
    return render(request, 'grid-listings-filterstop-search-aside-openstreetmap.html')

def colopenstreetmap(request):
    return render(request, 'grid-listings-filterscol-openstreetmap.html')

def isotopeopenstreetmap(request):
    return render(request, 'grid-listings-isotope-openstreetmap.html')

def rowcolopenstreetmap(request):
    return render(request, 'row-listings-filterscol-search-aside-openstreetmap.html')

def rowstopopenstreetmap(request):
    return render(request, 'row-listings-filterstop-openstreetmap.html')

def rowisotopeopenstreetmap(request):
    return render(request, 'row-listings-isotope-openstreetmap.html')

def detailhotelopenstreetmap(request):
    return render(request, 'detail-hotel-openstreetmap.html')

def listingmapopenstreetmap(request):
    return render(request, 'listing-map-openstreetmap.html')

def iconpack1(request):
    return render(request, 'icon-pack-1.html')

def iconpack2(request):
    return render(request, 'icon-pack-2.html')

def iconpack3(request):
    return render(request, 'icon-pack-3.html')

def iconpack4(request):
    return render(request, 'icon-pack-4.html')

def admin_addlisting(request):
    return render(request, 'admin_section/add-listing.html')

def admin_bookings(request):
    return render(request, 'admin_section/bookings.html')

def admin_charts(request):
    return render(request, 'admin_section/charts.html')

def admin_listings(request):
    return render(request, 'admin_section/listings.html')

def admin_messages(request):
    return render(request, 'admin_section/messages.html')

def admin_reviews(request):
    return render(request, 'admin_section/reviews.html')

def admin_tables(request):
    return render(request, 'admin_section/tables.html')

def admin_user_profile(request):
    return render(request, 'admin_section/user-profile.html')

def admin_bookmark(request):
    return render(request, 'admin_section/bookmarks.html')

def admin_home(request):
    return render(request, 'admin_section/index.html')
# def _(request):
#     return render(request, '')