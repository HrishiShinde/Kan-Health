from django.shortcuts import render
from app.forms import SymptomCheckerForm
from user_profile.models import UserProfile
from model.model import HealthAI

# Create your views here.
def home(request):
    return render(request, 'home.html')

def get_plan(request):
    symptom_form = SymptomCheckerForm()
    ai_response = ""

    if request.method == 'POST':
        user = request.user
        user_profile = UserProfile.objects.get(user=user)
        symptom_form_data = SymptomCheckerForm(request.POST)

        if symptom_form_data.is_valid():
            symptom_form = symptom_form_data
            symptoms = symptom_form_data.cleaned_data
            
            # Prepare prompt for AI model
            prompt = generate_prompt(user_profile, symptoms)

            # ai_response = dummy_ai_model(prompt)

            healthai = HealthAI()
            ai_response = healthai.generate_health_plan2(prompt)

            ai_response = [ai_response.get("generated_health_plan")]

    response_data = {
        'symptom_form': symptom_form,
        'ai_response': ai_response,
    }

    return render(request, 'consult.html', response_data)

def generate_prompt(user_profile, symptoms):
    prompt = f"""
    Generate a personalized health plan based on the following user information:

    Age: {user_profile.age}
    Gender: {user_profile.gender}
    Health History: {user_profile.health_history}
    Medications: {user_profile.medications}
    Allergies: {user_profile.allergies}

    Symptoms: {symptoms.get('symptoms')}
    Symptom Onset: {symptoms.get('symptom_onset')}
    Symptom Severity: {symptoms.get('symptom_severity')}
    Symptom Frequency: {symptoms.get('symptom_frequency')}
    Symptom Triggers: {symptoms.get('symptom_triggers')}
    Symptom Relievers: {symptoms.get('symptom_relievers')}

    Based on the above information, suggest at least two personalized health plans.
    """
    return prompt

def dummy_ai_model(prompt):
    # This is a placeholder function. Replace with actual AI model logic.
    plan1 = "Health Plan 1: \n- Drink plenty of fluids\n- Rest and avoid strenuous activities\n- Take over-the-counter pain relievers as needed\n- If symptoms persist for more than 3 days, consult a physician"
    plan2 = "Health Plan 2: \n- Follow a balanced diet with plenty of fruits and vegetables\n- Engage in moderate exercise like walking or yoga\n- Avoid known triggers for your symptoms\n- Monitor your symptoms closely and seek medical advice if they worsen"

    return [plan1, plan2]
