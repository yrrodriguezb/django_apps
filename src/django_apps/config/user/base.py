from django.urls import reverse_lazy


ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('account:user_detail', args=[ u.username ])
}