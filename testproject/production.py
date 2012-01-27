from testproject.settings import *

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
    )

try:
    from local_settings import *
except ImportError:
    pass
