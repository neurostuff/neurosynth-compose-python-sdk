import typing_extensions

from neurosynth_compose_sdk.paths import PathValues
from neurosynth_compose_sdk.apis.paths.users_id import UsersId
from neurosynth_compose_sdk.apis.paths.users import Users
from neurosynth_compose_sdk.apis.paths.meta_analyses import MetaAnalyses
from neurosynth_compose_sdk.apis.paths.meta_analyses_id import MetaAnalysesId
from neurosynth_compose_sdk.apis.paths.studysets import Studysets
from neurosynth_compose_sdk.apis.paths.studysets_id import StudysetsId
from neurosynth_compose_sdk.apis.paths.annotations import Annotations
from neurosynth_compose_sdk.apis.paths.annotations_id import AnnotationsId
from neurosynth_compose_sdk.apis.paths.specifications import Specifications
from neurosynth_compose_sdk.apis.paths.specifications_id import SpecificationsId
from neurosynth_compose_sdk.apis.paths.meta_analysis_results import MetaAnalysisResults
from neurosynth_compose_sdk.apis.paths.meta_analysis_results_id import MetaAnalysisResultsId
from neurosynth_compose_sdk.apis.paths.neurovault_collections import NeurovaultCollections
from neurosynth_compose_sdk.apis.paths.neurovault_collections_id import NeurovaultCollectionsId
from neurosynth_compose_sdk.apis.paths.neurovault_files import NeurovaultFiles
from neurosynth_compose_sdk.apis.paths.neurovault_files_id import NeurovaultFilesId
from neurosynth_compose_sdk.apis.paths.projects import Projects
from neurosynth_compose_sdk.apis.paths.projects_id import ProjectsId
from neurosynth_compose_sdk.apis.paths.neurostore_studies import NeurostoreStudies
from neurosynth_compose_sdk.apis.paths.neurostore_studies_id import NeurostoreStudiesId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.USERS_ID: UsersId,
        PathValues.USERS: Users,
        PathValues.METAANALYSES: MetaAnalyses,
        PathValues.METAANALYSES_ID: MetaAnalysesId,
        PathValues.STUDYSETS: Studysets,
        PathValues.STUDYSETS_ID: StudysetsId,
        PathValues.ANNOTATIONS: Annotations,
        PathValues.ANNOTATIONS_ID: AnnotationsId,
        PathValues.SPECIFICATIONS: Specifications,
        PathValues.SPECIFICATIONS_ID: SpecificationsId,
        PathValues.METAANALYSISRESULTS: MetaAnalysisResults,
        PathValues.METAANALYSISRESULTS_ID: MetaAnalysisResultsId,
        PathValues.NEUROVAULTCOLLECTIONS: NeurovaultCollections,
        PathValues.NEUROVAULTCOLLECTIONS_ID: NeurovaultCollectionsId,
        PathValues.NEUROVAULTFILES: NeurovaultFiles,
        PathValues.NEUROVAULTFILES_ID: NeurovaultFilesId,
        PathValues.PROJECTS: Projects,
        PathValues.PROJECTS_ID: ProjectsId,
        PathValues.NEUROSTORESTUDIES: NeurostoreStudies,
        PathValues.NEUROSTORESTUDIES_ID: NeurostoreStudiesId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.USERS_ID: UsersId,
        PathValues.USERS: Users,
        PathValues.METAANALYSES: MetaAnalyses,
        PathValues.METAANALYSES_ID: MetaAnalysesId,
        PathValues.STUDYSETS: Studysets,
        PathValues.STUDYSETS_ID: StudysetsId,
        PathValues.ANNOTATIONS: Annotations,
        PathValues.ANNOTATIONS_ID: AnnotationsId,
        PathValues.SPECIFICATIONS: Specifications,
        PathValues.SPECIFICATIONS_ID: SpecificationsId,
        PathValues.METAANALYSISRESULTS: MetaAnalysisResults,
        PathValues.METAANALYSISRESULTS_ID: MetaAnalysisResultsId,
        PathValues.NEUROVAULTCOLLECTIONS: NeurovaultCollections,
        PathValues.NEUROVAULTCOLLECTIONS_ID: NeurovaultCollectionsId,
        PathValues.NEUROVAULTFILES: NeurovaultFiles,
        PathValues.NEUROVAULTFILES_ID: NeurovaultFilesId,
        PathValues.PROJECTS: Projects,
        PathValues.PROJECTS_ID: ProjectsId,
        PathValues.NEUROSTORESTUDIES: NeurostoreStudies,
        PathValues.NEUROSTORESTUDIES_ID: NeurostoreStudiesId,
    }
)
