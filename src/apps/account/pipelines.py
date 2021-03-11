from requests import request, HTTPError
from django.core.files.base import ContentFile
from apps.account.models import Profile


def save_profile(backend, user, response, *args, **kwargs):
    def save_image_profile(profile, url_image):
        try:
            response = request('GET', url_image, params={'type': 'large'})
            response.raise_for_status()
        except HTTPError as ex:
            pass
        else:
            profile.photo.save('{0}_social.jpg'.format(user.username), 
                ContentFile(response.content))
            profile.save()

    profile, created = Profile.objects.get_or_create(user=user)

    if backend.name == 'facebook':
        url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        save_image_profile(profile, url)
    elif backend.name == 'google-oauth2':
        url = response.get('picture', None)
        if url is not None:
            save_image_profile(profile, url)