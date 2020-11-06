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

def well_info(request,id):
    well = Well.objects.get(id=id)
    return render(request, 'well_info.html', {'well':well})


def well_history(request,id):
    well = Well.objects.get(id=id)
    events = Event.objects.filter(well=well)
    context = {
            'events':events,
            'well':well
    }
    return render(request, 'well_history.html', context=context)

def delete_event(request, id):
    event = Event.objects.get(id=id)
    well = event.well
    event.delete()
    return redirect(reverse('tracker:well' ,kwargs={'id': event.well.id}))

def add_event(request,id):
    well = Well.objects.get(id=id)
    events = Event.objects.filter(well=well)    
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event_form = form.save(commit=False)
            event_form.well = well
            event_form.save()
            return redirect(reverse('tracker:well_history', kwargs={'id':well.id}))
    else:
        form = EventForm()
    context = {
            'form':form,
            'well':well
    }
    return render(request, 'well_add_event.html', context=context)


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


