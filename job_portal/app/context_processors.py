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
