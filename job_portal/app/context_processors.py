from .models import Candidate, Employer

def user_types(request):
    context = {}
    if request.user.is_authenticated:
        context = {
            'is_candidate': request.user.user_type == 'candidate',
            'is_employer': request.user.user_type == 'employer',
        }
    else:
        context = {
            'is_candidate': False,
            'is_employer': False,
        }
    return context

def candidate_id_pass(request):
    context = {}
    if request.user.is_authenticated and request.user.user_type == 'candidate' and hasattr(request.user, 'candidate_profile'):
        context['candidate_id'] = request.user.candidate_profile.id
    else:
        context['candidate_id'] = None
    return context

def loggedin_candidate(request):
    if request.user.is_authenticated and request.user.user_type == 'candidate':
        try:
            candidate = Candidate.objects.get(user=request.user)
            contact = candidate.candidate_contacts.first() if candidate.candidate_contacts.exists() else None
            return {'candidate': candidate, 'contact': contact}
        except Candidate.DoesNotExist:
            return {'candidate': None, 'contact': None}
    return {'candidate': None, 'contact': None}



def loggedin_employer(request):
    if request.user.is_authenticated and request.user.user_type == 'employer':
        try:
            employer = Employer.objects.get(user=request.user)
            return {'employer': employer}
        except employer.DoesNotExist:
            return {'employer': None}
    return {'employers': None}