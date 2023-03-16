# coding: utf-8

"""
    Analysis Specification for Meta-analysis

    api to create a meta-analysis specification  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by: https://openapi-generator.tech
"""

from neurosynth_compose_sdk.paths.annotations_id.put import AnnotationsIdPut
from neurosynth_compose_sdk.paths.meta_analyses_id.put import MetaAnalysesIdPut
from neurosynth_compose_sdk.paths.meta_analysis_results_id.put import MetaAnalysisResultsIdPut
from neurosynth_compose_sdk.paths.neurovault_collections_id.put import NeurovaultCollectionsIdPut
from neurosynth_compose_sdk.paths.neurovault_files_id.put import NeurovaultFilesIdPut
from neurosynth_compose_sdk.paths.projects_id.put import ProjectsIdPut
from neurosynth_compose_sdk.paths.specifications_id.put import SpecificationsIdPut
from neurosynth_compose_sdk.paths.studysets_id.put import StudysetsIdPut


class PutApi(
    AnnotationsIdPut,
    MetaAnalysesIdPut,
    MetaAnalysisResultsIdPut,
    NeurovaultCollectionsIdPut,
    NeurovaultFilesIdPut,
    ProjectsIdPut,
    SpecificationsIdPut,
    StudysetsIdPut,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass