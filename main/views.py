from django.shortcuts import render
from django.http import HttpResponse
from .forms import CompoundForm
from .models import Compound

# Create your views here.
def home(request):
    return render(request, "main/home.html")


def compound_data(request):
    if request.method == "POST":
        form = CompoundForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            cpd_id = form.cleaned_data['cpd_id']
            is_synthesis_protocol_available = form.cleaned_data['is_synthesis_protocol_available']
            
            compound = Compound.objects.create(
                email=email, 
                cpd_id=cpd_id,
                is_synthesis_protocol_available=is_synthesis_protocol_available)
            compound.save()
            
            return HttpResponse("Compound Data is saved to the compound database")
    form = CompoundForm()
    return render(request, "main/compound.html", {'form': form})

