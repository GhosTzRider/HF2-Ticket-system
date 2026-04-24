def role_context(request):
    role = request.session.get('role', 'supporter')
    current_user_id = request.session.get('current_user_id')
    return {
        'role': role,
        'current_user_id': current_user_id,
    }
