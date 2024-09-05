def user_types(request):
    context = {
        'is_candidate': hasattr(request.user, 'candidate_profile'),
        'is_employer': hasattr(request.user, 'employers'),
    }
    return context

def candidate_id_pass(request):
    context = {}
    if request.user.is_authenticated and hasattr(request.user, 'candidate_profile'):
        context['candidate_id'] = request.user.candidate_profile.id
    else:
        context['candidate_id'] = None
    return context