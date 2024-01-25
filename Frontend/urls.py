from django.urls import path
from Frontend import views
from django.urls import path
from Frontend import views

urlpatterns = [
    path('homepage',views.homepage,name="homepage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('categorypage/',views.categorypage,name="categorypage"),
    path('disproduct/<itemcatg>/',views.disproduct,name="disproduct"),
    path('productsingle/<int:dataid>',views.productsingle,name="productsingle"),
    path('savecontactus/',views.savecontactus,name="savecontactus"),
    path('',views.weblogin,name="weblogin"),
    path('savecustomer/',views.savecustomer,name="savecustomer"),
    path('custemerlogin/',views.custemerlogin,name="custemerlogin"),
    path('logout/',views.logout,name="logout"),
    path('protected/', views.some_protected_view, name='protected_view'),

    path('savecart/',views.savecart,name="savecart"),
    path('viewcartpage/',views.viewcartpage,name="viewcartpage"),
    path('deletecartfont/<int:dataid>',views.deletecartfont,name="deletecartfont"),
    path('check/',views.check,name="check"),
    path('savecheck/',views.savecheck,name="savecheck"),
    path('search/',views.search_results, name='search_results'),

    path('wishlist/',views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/',views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:wishlist_id>/',views.remove_from_wishlist, name='remove_from_wishlist'),
]
