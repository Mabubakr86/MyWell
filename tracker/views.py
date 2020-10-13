from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *


def index(request):
    fields = Field.objects.all()
    data = {}
    for field in fields:
        field_wells = field.well_set.all()
        data[field.name] = field_wells
    context = {'data': data}

    return render(request, 'index.html', context=context)


def well(request,id):
    well = Well.objects.get(id=id)
    events = Event.objects.filter(well=well)

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event_form = form.save(commit=False)
            event_form.well = well
            event_form.save()
            return redirect(reverse('tracker:well', kwargs={'id':well.id}))

    else:
        form = EventForm()

    return render(request, 'well.html', {'events':events,'form':form})

def delete_event(request, id):
    event = Event.objects.get(id=id)
    well = event.well
    event.delete()
    return redirect(reverse('tracker:well' ,kwargs={'id': event.well.id}))


def edit_event(request,id):
    event = Event.objects.get(id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event_form = form.save(commit=False)
            event_form.well = event.well
            event_form.save()
            return redirect(reverse('tracker:well', kwargs={'id':event.well.id}))

    else:
        form = EventForm(instance=event)

    return render(request, 'event_edit.html', {'form':form})

def add_well(request):
    if request.method == 'POST':
        form = WellForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tracker:index'))

    else:
        form = WellForm()

    return render(request, 'add_well.html', {'form':form})


def add_field(request):
    if request.method == 'POST':
        form = FieldForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tracker:index'))

    else:
        form = FieldForm()

    return render(request, 'add_field.html', {'form':form})


