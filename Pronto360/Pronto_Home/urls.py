from django.urls import path
from Pronto_Home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('services/', views.services, name='services'),
    path('electrician/', views.services, name='electrician'),
    path('plumbing/', views.services, name='plumbing'),
    path('handyman/', views.services, name='handyman'),
    path('roofing/', views.services, name='roofing'),
    path('HVAC/', views.services, name='HVAC'),
    path('carpenter/', views.services, name='carpenter'),
    path('other/', views.services, name='other'),
    path('blog-post', views.blogpost, name='blog_post'),
    path('blog/', views.blog, name='blog'),
    path('account/', views.account, name='account'),
    path('help/', views.help, name='help'),
    path('faq/', views.faq, name='faq'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_listing/', views.account, name='add_listing'),
    path('detail-restaurant/', views.detail_restaurant, name='detail-restaurant'),
    path('media-gallery/', views.media_gallery, name='media_gallery'),
    path('checkout/', views.checkout, name='checkout'),
    path('sidebar-search/', views.sidebarsearch, name='sidebar_search'),
    path('full-search/', views.fullsearch, name='full_search'),
    path('full-isotope/', views.fullisotope, name = 'full-isotope'),
    path('listing-map/', views.listingmap, name='listing_map'),
    path('confirm/', views.confirm, name='confirm'),
    path('bookings/', views.bookings, name = 'bookings'),
    path('detail-hotel/', views.detail_hotel, name='detail-hotel'),
    path('detail-shop/', views.detail_shop, name = 'detail-shop'),
    path('detail-carousel/', views.detailcarousel, name='detail-carousel'),
    path('detail-carousel-2/', views.detailcarousel_2, name='detail-carousel-2'),
    path("pricing-tables/", views.pricing_tables, name='pricing_tables'),
    path('error-404/', views.err_404, name='404'),
    path('contacts-2/', views.contacts2, name='contacts_2'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('menu-options/', views.menu_options, name='menu_options'),
    path('invoice/', views.invoice, name='invoice'),
    path('col-search-aside/', views.filterscolsearchaside, name='col_search_aside'),
    path('stop-search-aside/', views.filterstopsearchaside, name='stop_side_search'),
    path('search-aside-openstreetmap/', views.searchasideopenstreetmap, name='col_search_aside_openstreetmap'),
    path('stop-aside-openstreetmap/', views.stopopenstreetmap, name='stop_search_aside_openstreetmap'),
    path('col-openstreetmap/', views.colopenstreetmap, name='col_openstreetmap'),
    path('isotope-openstreetmap/', views.isotopeopenstreetmap, name='isotope_openstreetmap'),
    path('row-col-openstreetmap/', views.rowcolopenstreetmap, name='row_col_openstreetmap'),
    path('row-stop-openstreetmap/', views.rowstopopenstreetmap, name='row_stop_openstreetmap'),
    path('row-isotope-openstreetmap/', views.rowisotopeopenstreetmap, name='row_isotope_openstreetmap'),
    path("detail-hotel-openstreetmap/", views.detailhotelopenstreetmap, name='detail_hotel_openstreeetmap'),
    path("listing-map-openstreetmap/", views.listingmapopenstreetmap, name='listing_map_openstreetmap'),
    path('icon-pack-1', views.iconpack1, name='iconpack1'),
    path('icon-pack-2/', views.iconpack2, name='iconpack2'),
    path('icon-pack-3/', views.iconpack3, name='iconpack3'),
    path('icon-pack-4/', views.iconpack4, name='iconpack4'),
    path('admin_dashboard/admin-bookmarks', views.admin_bookmark,name='admin_bookmarks' ),
    path('admin_dashboard/admin-add-listing/', views.admin_addlisting, name='admin_add_listing'),
    path('admin_dashboard/admin-bookings/', views.admin_bookings, name='admin_bookings'),
    path('admin_dashboard/admin-charts/', views.admin_charts, name='admin_charts'),
    path('admin_dashboard/admin-listings', views.admin_listings, name='admin_listings'),
    path('admin_dashboard/admin-messages', views.admin_messages, name='admin_messages'),
    path('admin_dashboard/admin-reviews/', views.admin_reviews, name='admin_reviews'),
    path('admin_dashboard/admin-tables', views.admin_tables, name='admin_tables'),
    path('admin_dashboard/admin-user-profile', views.admin_user_profile, name='admin_user_profile'),
    path('admin-dashboard/', views.admin_home, name='admin_home')
]
