from django import forms


class PredictionForm(forms.Form):

    Year_Built = forms.IntegerField(
        label="Année de construction",
        min_value=1800,
        max_value=2010,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Année de construction',
            'title': 'Entrez une année au format YYYY'
        })
    )


    Total_Bsmt_SF = forms.DecimalField(
        label="Surface de la cave (m²)",
        min_value=0,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Surface de la cave (m²)'
        })
    )


    First_Flr_SF = forms.DecimalField(
        label="Surface du premier étage (m²)",
        min_value=0,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Surface du 1er étage (m²)'
        })
    )


    Gr_Liv_Area = forms.DecimalField(
        label="Surface habitable au sol (m²)",
        min_value=0,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Surface habitable (m²)'
        })
    )


    Garage_Area = forms.DecimalField(
        label="Surface du garage (m²)",
        min_value=0,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Surface du garage (m²)'
        })
    )
 
    choices = {
        10: 'Very Excellent',
        9: 'Excellent',
        8: 'Very Good',
        7: 'Good',
        6: 'Above Average',
        5: 'Average',
        4: 'Below Average',
        3: 'Fair',
        2: 'Poor',
        1: 'Very Poor',
    }


    Overall_Qual = forms.ChoiceField(
        label="Qualité générale des finitions et des matériaux",
        choices=[
            (10, 'Very Excellent (10)'),
            (9, 'Excellent (9)'),
            (8, 'Very Good (8)'),
            (7, 'Good (7)'),
            (6, 'Above Average (6)'),
            (5, 'Average (5)'),
            (4, 'Below Average (4)'),
            (3, 'Fair (3)'),
            (2, 'Poor (2)'),
            (1, 'Very Poor (1)'),
        ],
        widget=forms.Select(attrs={'class': 'form-control-2'})
    )
    

    Full_Bath = forms.IntegerField(
        label="Nombre de salle de bain",
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de salles de bain'})
    )
    

    Exter_Qual = forms.ChoiceField(
        label="Qualité des matériaux extérieurs",
        choices=[
            ('Ex', 'Excellent'),
            ('Gd', 'Good'),
            ('TA', 'Typical/Average'),
            ('Fa', 'Fair'),
            ('Po', 'Poor'),
        ],
        widget=forms.Select(attrs={'class': 'form-control-2'})
    )

    
    Kitchen_Qual = forms.ChoiceField(
        label="Qualité des matériaux de la cuisine",
        choices=[
            ('Ex', 'Excellent'),
            ('Gd', 'Good'),
            ('TA', 'Typical/Average'),
            ('Fa', 'Fair'),
            ('Po', 'Poor'),
        ],
        widget=forms.Select(attrs={'class': 'form-control-2'})
    )


    Neighborhood = forms.ChoiceField(
        label="Quartier",
        choices=[
            ('Blmngtn', 'Bloomington Heights'),
            ('Blueste', 'Bluestem'),
            ('BrDale', 'Briardale'),
            ('BrkSide', 'Brookside'),
            ('ClearCr', 'Clear Creek'),
            ('CollgCr', 'College Creek'),
            ('Crawfor', 'Crawford'),
            ('Edwards', 'Edwards'),
            ('Gilbert', 'Gilbert'),
            ('IDOTRR', 'Iowa DOT and Rail Road'),
            ('Landmrk' 'Landmark'),
            ('MeadowV', 'Meadow Village'),
            ('Mitchel', 'Mitchell'),
            ('Names', 'North Ames'),
            ('NoRidge', 'Northridge'),
            ('NPkVill', 'Northpark Villa'),
            ('NridgHt', 'Northridge Heights'),
            ('NWAmes', 'Northwest Ames'),
            ('OldTown', 'Old Town'),
            ('SWISU', 'South & West of Iowa State University'),
            ('Sawyer', 'Sawyer'),
            ('SawyerW', 'Sawyer West'),
            ('Somerst', 'Somerset'),
            ('StoneBr', 'Stone Brook'),
            ('Timber', 'Timberland'),
            ('Veenker', 'Veenker'),
        ],
        widget=forms.Select(attrs={'class': 'form-control-2'})
    )
 
