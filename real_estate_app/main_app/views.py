from django.shortcuts import render
from django.http import HttpResponse
from .utils import make_prediction
from .models import PredictionForm

fields_group1 = ['Year_Built', 'Total_Bsmt_SF', 'First_Flr_SF', 'Gr_Liv_Area', 'Garage_Area']
fields_group2 = ['Overall_Qual', 'Full_Bath', 'Exter_Qual', 'Kitchen_Qual', 'Neighborhood']

def index(request):

    form = PredictionForm()
    

    context = {'form': form,
               'fields_group1': [form[field] for field in fields_group1],
               'fields_group2': [form[field] for field in fields_group2]
            }
    
    return render(request, 'index.html', context)


def predict(request):

    if request.method == 'POST':
        form = PredictionForm(request.POST)  # Utilisez votre modèle de formulaire
        
        if form.is_valid():
            X_predict = form.cleaned_data  # Utilisez les données propres et validées du formulaire
        
            pred = make_prediction(X_predict)

            if pred != 0:
                context = {'form': form,
                           'fields_group1': [form[field] for field in fields_group1],
                           'fields_group2': [form[field] for field in fields_group2],
                           'data': int(pred)
                        }
                
                return render(request, 'index.html', context)
            else:
                return HttpResponse("Invalid input")
        
        else:
            return HttpResponse("Invalid input")
        
    else:
        return HttpResponse("Method Not Allowed")

