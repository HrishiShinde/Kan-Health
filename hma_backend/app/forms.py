from django import forms

class SymptomCheckerForm(forms.Form):
    symptoms = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 4, 
            'placeholder': 'E.g., Coughing, headache, and fever'
        }), 
        label='Describe your symptoms'
    )
    symptom_onset = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'E.g., Since morning, Since two days'
        }), 
        label='When did the symptoms start?'
    )
    symptom_severity = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class': 'form-select'
        }), 
        choices=[('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe')], 
        label='Severity of symptoms'
    )
    symptom_frequency = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class': 'form-select'
        }), 
        choices=[('Occasional', 'Occasional'), ('Intermittent', 'Intermittent'), ('Constant', 'Constant')], 
        label='Frequency of symptoms'
    )
    symptom_triggers = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 2, 
            'placeholder': 'E.g., Exposure to cold air or pollen'
        }), 
        label='What triggers your symptoms?', 
        required=False
    )
    symptom_relievers = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 2, 
            'placeholder': 'E.g., Resting or taking medication'
        }), 
        label='What relieves your symptoms?', 
        required=False
    )
