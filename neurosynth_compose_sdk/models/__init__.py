# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from neurosynth_compose_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from neurosynth_compose_sdk.model.annotation import Annotation
from neurosynth_compose_sdk.model.annotation_list import AnnotationList
from neurosynth_compose_sdk.model.annotation_post_body import AnnotationPostBody
from neurosynth_compose_sdk.model.annotation_return import AnnotationReturn
from neurosynth_compose_sdk.model.annotation_update import AnnotationUpdate
from neurosynth_compose_sdk.model.corrector import Corrector
from neurosynth_compose_sdk.model.estimator import Estimator
from neurosynth_compose_sdk.model.meta_analysis import MetaAnalysis
from neurosynth_compose_sdk.model.meta_analysis_list import MetaAnalysisList
from neurosynth_compose_sdk.model.meta_analysis_post_body import MetaAnalysisPostBody
from neurosynth_compose_sdk.model.meta_analysis_return import MetaAnalysisReturn
from neurosynth_compose_sdk.model.neurostore_list import NeurostoreList
from neurosynth_compose_sdk.model.neurostore_study import NeurostoreStudy
from neurosynth_compose_sdk.model.neurostore_study_list import NeurostoreStudyList
from neurosynth_compose_sdk.model.neurostore_study_return import NeurostoreStudyReturn
from neurosynth_compose_sdk.model.neurovault_collection import NeurovaultCollection
from neurosynth_compose_sdk.model.neurovault_collection_return import NeurovaultCollectionReturn
from neurosynth_compose_sdk.model.neurovault_file import NeurovaultFile
from neurosynth_compose_sdk.model.neurovault_file_list import NeurovaultFileList
from neurosynth_compose_sdk.model.neurovault_file_return import NeurovaultFileReturn
from neurosynth_compose_sdk.model.neurovault_list import NeurovaultList
from neurosynth_compose_sdk.model.project import Project
from neurosynth_compose_sdk.model.project_list import ProjectList
from neurosynth_compose_sdk.model.project_return import ProjectReturn
from neurosynth_compose_sdk.model.read_only import ReadOnly
from neurosynth_compose_sdk.model.result import Result
from neurosynth_compose_sdk.model.result_list import ResultList
from neurosynth_compose_sdk.model.result_return import ResultReturn
from neurosynth_compose_sdk.model.specification import Specification
from neurosynth_compose_sdk.model.specification_list import SpecificationList
from neurosynth_compose_sdk.model.specification_post_body import SpecificationPostBody
from neurosynth_compose_sdk.model.specification_return import SpecificationReturn
from neurosynth_compose_sdk.model.studyset import Studyset
from neurosynth_compose_sdk.model.studyset_list import StudysetList
from neurosynth_compose_sdk.model.studyset_post_body import StudysetPostBody
from neurosynth_compose_sdk.model.studyset_return import StudysetReturn
from neurosynth_compose_sdk.model.user import User
from neurosynth_compose_sdk.model.user_list import UserList
from neurosynth_compose_sdk.model.user_return import UserReturn
