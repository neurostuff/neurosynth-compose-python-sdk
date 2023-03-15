
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.annotations_api import AnnotationsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from neurosynth_compose_sdk.api.annotations_api import AnnotationsApi
from neurosynth_compose_sdk.api.meta_analyses_api import MetaAnalysesApi
from neurosynth_compose_sdk.api.neurovault_api import NeurovaultApi
from neurosynth_compose_sdk.api.projects_api import ProjectsApi
from neurosynth_compose_sdk.api.specifications_api import SpecificationsApi
from neurosynth_compose_sdk.api.studyset_api import StudysetApi
from neurosynth_compose_sdk.api.users_api import UsersApi
