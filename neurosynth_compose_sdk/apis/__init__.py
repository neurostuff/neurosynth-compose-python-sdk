
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.annotation_api import AnnotationApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from neurosynth_compose_sdk.api.annotation_api import AnnotationApi
from neurosynth_compose_sdk.api.meta_analysis_api import MetaAnalysisApi
from neurosynth_compose_sdk.api.studyset_api import StudysetApi
from neurosynth_compose_sdk.api.user_api import UserApi
