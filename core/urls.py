from django.urls import path
from . import views
from .views import DonorCreate, PendingDonorsView, DonorUpdateView, BloodRecordCreateView

urlpatterns = [
    path('', views.index, name='index'),
    path('donr-register', DonorCreate.as_view(), name='regdonor'),
    path('donor-confirmation', views.DonorConf, name='donorconf'),
   # path('donorlist', views.donor, name='donorlist'),
    path('pending-donors', PendingDonorsView.as_view(), name='pendingdonors'),
    path('donor/<int:pk>/update', DonorUpdateView.as_view(), name='donor-update'),
    path('search-donor', views.searchdonor, name='searchdonor'),

    #path('add-record', views.addrecord, name='addrecord'),
    # path('searchresult', views.search, name='searchresult'),
    # path('contact', views.contact, name='contact'),
    # path('blood-register', BloodRecordCreateView.as_view(), name='bloodregister'),
    # path('search-blood', views.searchblood, name='searchblood'),
    
]
