from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from .models import Person,Email,Phone
from django.db.models import Q
from django.urls import reverse_lazy

def home(request):
	people = Person.objects.all()
	query = request.GET.get("q")
	if query:
		people = Person.objects.filter(Q(name__icontains=query)|Q(surname__icontains=query)|
			Q(emails__email__icontains=query)|Q(phones__phone__icontains=query)).distinct()
	return render(request,'app/home.html',{'users': people})


def add_email_and_phone(request,pk):
	person = get_object_or_404(Person, pk=pk)
	if request.method == 'POST':
		get_email = request.POST.get("email")
		get_phone = request.POST.get("phone")

		Email.objects.create(email=get_email, person=person)
		Phone.objects.create(phone=get_phone, person=person)

	return redirect('/people/')

def delete_user(request,pk):
	person = get_object_or_404(Person, pk=pk)
	if request.method == 'POST':
		if not person.emails.all().exists() and not person.phones.all().exists():
			person.delete()
	return redirect('/people/')




class PersonCreateView(CreateView):
	model = Person
	fields = ['name','surname']
	success_url = reverse_lazy('persons')

class PersonUpdateView(UpdateView):
		model = Person
		fields = ['name','surname']
		success_url = reverse_lazy('persons')







