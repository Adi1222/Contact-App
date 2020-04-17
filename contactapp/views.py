from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from .forms import PersonForm



def contact_list(request):
    persons = Person.objects.all().order_by('first_name')
    context = {'persons': persons, 'count': persons.count()}
    return render(request, 'contactapp/contact_list.html', context)


def contact_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    # OR person = Person.objects.get(pk=pk)
    return render(request, 'contactapp/contact_detail.html', {'person': person})


def contact_new(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = PersonForm()
    return render(request, 'contactapp/contact_edit.html', {'form': form})


def contact_edit(request, pk):
    person = Person.objects.get(pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/person/' + str(person.pk))

    else:
        form = PersonForm(instance=person)
    return render(request, 'contactapp/contact_edit.html', {'form': form})


def contact_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('/')


def contact_add(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = PersonForm()
    return render(request, 'contactapp/contact_edit.html', {'form': form})