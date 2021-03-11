from .secrets import *


SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# Pipelines Social Auth

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.mail.mail_validation',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.user.create_user',
    'apps.account.pipelines.save_profile',
)

SOCIAL_AUTH_RAISE_EXCEPTIONS = True

RAISE_EXCEPTIONS = True


# Authentication Backends

AUTHENTICATION_BACKENDS_SOCIAL_AUTH = [
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
]