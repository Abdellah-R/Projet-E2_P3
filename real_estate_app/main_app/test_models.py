import pytest
from .models import PredictionForm

@pytest.mark.django_db
def test_prediction_form_valid_data():
    data = {
        'Year_Built': 1990,
        'Total_Bsmt_SF': 1000,
        'First_Flr_SF': 1200,
        'Gr_Liv_Area': 1800,
        'Garage_Area': 500,
        'Overall_Qual': 8,
        'Full_Bath': 2,
        'Exter_Qual': 'TA',
        'Kitchen_Qual': 'Gd',
        'Neighborhood': 'CollgCr',
    }
    
    form = PredictionForm(data=data)
    assert form.is_valid()

@pytest.mark.django_db
def test_prediction_form_invalid_data():
    data = {
        'Year_Built': 1990,
        'Total_Bsmt_SF': -1000,
        'First_Flr_SF': 1200,
        'Gr_Liv_Area': -1800,
        'Garage_Area': 500,
        'Overall_Qual': 8,
        'Full_Bath': 2,
        'Exter_Qual': 'TA',
        'Kitchen_Qual': 'Gd',
        'Neighborhood': 'CollgCr',
    }

    form = PredictionForm(data=data)
    assert form.is_valid() == False