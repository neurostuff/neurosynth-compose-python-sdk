# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from neurosynth_compose_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from neurosynth_compose_sdk.model.annotation import Annotation
from neurosynth_compose_sdk.model.annotation_list import AnnotationList
from neurosynth_compose_sdk.model.annotation_return import AnnotationReturn
from neurosynth_compose_sdk.model.annotation_update import AnnotationUpdate
from neurosynth_compose_sdk.model.annotation_update_all_of import AnnotationUpdateAllOf
from neurosynth_compose_sdk.model.corrector import Corrector
from neurosynth_compose_sdk.model.estimator import Estimator
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
from neurosynth_compose_sdk.model.meta_analysis import MetaAnalysis
from neurosynth_compose_sdk.model.meta_analysis_list import MetaAnalysisList
from neurosynth_compose_sdk.model.meta_analysis_return import MetaAnalysisReturn
from neurosynth_compose_sdk.model.read_only import ReadOnly
from neurosynth_compose_sdk.model.specification import Specification
from neurosynth_compose_sdk.model.specification_list import SpecificationList
from neurosynth_compose_sdk.model.specification_return import SpecificationReturn
from neurosynth_compose_sdk.model.studyset import Studyset
from neurosynth_compose_sdk.model.studyset_list import StudysetList
from neurosynth_compose_sdk.model.studyset_return import StudysetReturn
from neurosynth_compose_sdk.model.user import User
from neurosynth_compose_sdk.model.user_list import UserList
from neurosynth_compose_sdk.model.user_return import UserReturn
