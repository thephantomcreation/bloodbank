from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import Donor, Contact, Test, Blood
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator


def index(request):
	if request.method == 'POST':
		bloodgroup = request.POST['bloodgroup']
		location = request.POST['location']
		if bloodgroup == 'Select Blood Type:' or location == 'Select location:':
			error_msg = "Please Select Blood Group and Location Properly."
			return render(request, 'core/donorlist.html', {'error_msg' : error_msg})

		bloodrecords = Donor.objects.all().filter(bloodgroup=bloodgroup).filter(location=location)

		if not bloodrecords.count():
			bloodrecords= 'Noresult'

		context = {
			'bloodrecords' : bloodrecords,	
		}

		return render(request, 'core/donorlist.html', context)

		
	'''	else:
			bloodgroup = request.POST['bloodgroup']
			location = request.POST['location']

			bloodrecords = Donor.objects.all().filter(bloodgroup=bloodgroup).filter(location=location)


			context = {
				'bloodrecords' : bloodrecords,
				
			}

			 

			return render(request, 'core/donorlist.html', context)



'''
	return render(request, 'core/index.html')




def contact(request):
	pass


class DonorCreate(CreateView):
	model = Donor
	fields = ['name','age', 'gender', 'phone', 'bloodgroup', 'location']
	template_name = 'core/regdonor.html'
	success_url = reverse_lazy('donorconf')

	
#	model = Donor
#	fields = ['name','age', 'gender', 'phone', 'bloodgroup', 'location']
#	template_name = 'core/regdonor.html'
#	success_url = reverse_lazy('index')

class PendingDonorsView(LoginRequiredMixin, ListView):
	model = Donor
	template_name= 'core/pendingdonors.html'
	context_object_name= 'donors'
	ordering = ['-date_joined']
	login_url = 'admin/login/?next=/admin/'

	def get_queryset(self):
	    queryset = super(PendingDonorsView , self).get_queryset()
	    #your condition here.
	    return queryset.filter(verified= False)



class DonorUpdateView(LoginRequiredMixin, UpdateView):
	model = Donor
	fields = ['name','age', 'gender', 'phone', 'bloodgroup', 'location', 'verified']
	
	success_url = reverse_lazy('pendingdonors')
	login_url = 'admin/login/?next=/admin/'


class DonorView(ListView):
	model = Donor
	template_name= 'core/donorlist.html'
	context_object_name= 'donors'
	ordering = ['-date_joined']

	def get_queryset(self):
	    queryset = super(PendingDonorsView , self).get_queryset()
	    #your condition here.
	    return queryset.filter(verified= True)

class BloodRecordCreateView(LoginRequiredMixin, CreateView):
	model = Blood
	fields = ['bloodgroup', 'amount', 'donate_date', 'expiry_date']       
	template_name = 'core/addrecord.html'
	success_url = reverse_lazy('bloodregister')


def searchblood(request):

	if request.method == 'POST':


		
		bloodgroup = request.POST['bloodgroup']
		bloodrecords = Blood.objects.all().filter(bloodgroup=bloodgroup)
		
		if bloodgroup == 'Select Blood Type:':
			error_msg = "Please Select Blood Group Properly."
			return render(request, 'core/searchblood.html', {'error_msg' : error_msg})

		if not bloodrecords.count():
			bloodrecords= 'Noresult'





		context = {'bloodrecords': bloodrecords,
					'bloodgroup' : bloodgroup
				}

		return render(request, 'core/searchblood.html', context)


	return render(request, 'core/searchblood.html')

def searchdonor(request):
	if request.method == 'POST':
		bloodgroup = request.POST['bloodgroup']
		location = request.POST['location']

		if bloodgroup == 'Select Blood Type:' or location == 'Select location:':
			error_msg = "Please Select Blood Group and Location Properly."
			return render(request, 'core/donorlist.html', {'error_msg' : error_msg})

		bloodrecords = Donor.objects.all().filter(bloodgroup=bloodgroup).filter(location=location)

		if not bloodrecords.count():
			bloodrecords= 'Noresult'

		context = {
			'bloodrecords' : bloodrecords,
			
		}
		return render(request, 'core/donorlist.html', context)
	return render(request, 'core/donorlist.html')

		

def DonorConf(request):
	return render(request, 'core/donorconf.html')


def search(request):
	return render(request, 'core/searchresult.html')

def donor(request):
	return render(request, 'core/donorlist.html')

def addrecord(request):
	return render(request, 'core/addrecord.html')