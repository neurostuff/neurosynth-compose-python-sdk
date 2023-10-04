# coding: utf-8

# flake8: noqa
"""
    Analysis Specification for Meta-analysis

    api to create a meta-analysis specification  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


# import models into model package
from neurosynth_compose_sdk.models.annotation import Annotation
from neurosynth_compose_sdk.models.annotation_list import AnnotationList
from neurosynth_compose_sdk.models.annotation_post_body import AnnotationPostBody
from neurosynth_compose_sdk.models.annotation_return import AnnotationReturn
from neurosynth_compose_sdk.models.annotation_update import AnnotationUpdate
from neurosynth_compose_sdk.models.annotation_update_all_of import AnnotationUpdateAllOf
from neurosynth_compose_sdk.models.corrector import Corrector
from neurosynth_compose_sdk.models.estimator import Estimator
from neurosynth_compose_sdk.models.meta_analyses_get400_response import MetaAnalysesGet400Response
from neurosynth_compose_sdk.models.meta_analysis import MetaAnalysis
from neurosynth_compose_sdk.models.meta_analysis_annotation import MetaAnalysisAnnotation
from neurosynth_compose_sdk.models.meta_analysis_list import MetaAnalysisList
from neurosynth_compose_sdk.models.meta_analysis_post_body import MetaAnalysisPostBody
from neurosynth_compose_sdk.models.meta_analysis_results import MetaAnalysisResults
from neurosynth_compose_sdk.models.meta_analysis_return import MetaAnalysisReturn
from neurosynth_compose_sdk.models.meta_analysis_specification import MetaAnalysisSpecification
from neurosynth_compose_sdk.models.meta_analysis_studyset import MetaAnalysisStudyset
from neurosynth_compose_sdk.models.neurostore_analysis import NeurostoreAnalysis
from neurosynth_compose_sdk.models.neurostore_study import NeurostoreStudy
from neurosynth_compose_sdk.models.neurostore_study_list import NeurostoreStudyList
from neurosynth_compose_sdk.models.neurostore_study_return import NeurostoreStudyReturn
from neurosynth_compose_sdk.models.neurovault_collection import NeurovaultCollection
from neurosynth_compose_sdk.models.neurovault_collection_files import NeurovaultCollectionFiles
from neurosynth_compose_sdk.models.neurovault_collection_return import NeurovaultCollectionReturn
from neurosynth_compose_sdk.models.neurovault_file import NeurovaultFile
from neurosynth_compose_sdk.models.neurovault_file_list import NeurovaultFileList
from neurosynth_compose_sdk.models.neurovault_file_return import NeurovaultFileReturn
from neurosynth_compose_sdk.models.neurovault_list import NeurovaultList
from neurosynth_compose_sdk.models.project import Project
from neurosynth_compose_sdk.models.project_list import ProjectList
from neurosynth_compose_sdk.models.project_meta_analyses import ProjectMetaAnalyses
from neurosynth_compose_sdk.models.project_return import ProjectReturn
from neurosynth_compose_sdk.models.read_only import ReadOnly
from neurosynth_compose_sdk.models.result import Result
from neurosynth_compose_sdk.models.result_init import ResultInit
from neurosynth_compose_sdk.models.result_list import ResultList
from neurosynth_compose_sdk.models.result_list_results import ResultListResults
from neurosynth_compose_sdk.models.result_return import ResultReturn
from neurosynth_compose_sdk.models.specification import Specification
from neurosynth_compose_sdk.models.specification_conditions import SpecificationConditions
from neurosynth_compose_sdk.models.specification_list import SpecificationList
from neurosynth_compose_sdk.models.specification_post_body import SpecificationPostBody
from neurosynth_compose_sdk.models.specification_return import SpecificationReturn
from neurosynth_compose_sdk.models.studyset import Studyset
from neurosynth_compose_sdk.models.studyset_list import StudysetList
from neurosynth_compose_sdk.models.studyset_post_body import StudysetPostBody
from neurosynth_compose_sdk.models.studyset_reference import StudysetReference
from neurosynth_compose_sdk.models.studyset_reference_list import StudysetReferenceList
from neurosynth_compose_sdk.models.studyset_reference_return import StudysetReferenceReturn
from neurosynth_compose_sdk.models.studyset_reference_snapshots_inner import StudysetReferenceSnapshotsInner
from neurosynth_compose_sdk.models.studyset_return import StudysetReturn
from neurosynth_compose_sdk.models.user import User
from neurosynth_compose_sdk.models.user_list import UserList
from neurosynth_compose_sdk.models.user_return import UserReturn
