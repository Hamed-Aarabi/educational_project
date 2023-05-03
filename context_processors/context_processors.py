from django.urls import resolve, reverse, reverse_lazy



def user_panel_urls(request):
    profile_url = reverse('account:user_panel', args=[request.user.username])
    profile_update_url = reverse('account:user_panel_update', args=[request.user.username])
    # profile_url = reverse('account:user_panel', args=[request.user.username])
    # profile_url = reverse('account:user_panel', args=[request.user.username])
    # profile_url = reverse('account:user_panel', args=[request.user.username])
    return {'profile':profile_url, 'profile_update':profile_update_url}