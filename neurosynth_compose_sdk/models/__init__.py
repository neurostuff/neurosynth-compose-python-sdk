""" Contains all the data models used in inputs/outputs """

from .annotation import Annotation
from .annotation_list import AnnotationList
from .annotation_post import AnnotationPost
from .annotation_post_body import AnnotationPostBody
from .annotation_return import AnnotationReturn
from .annotation_snapshot import AnnotationSnapshot
from .corrector import Corrector
from .corrector_args import CorrectorArgs
from .estimator import Estimator
from .estimator_args import EstimatorArgs
from .meta_analysis import MetaAnalysis
from .meta_analysis_list import MetaAnalysisList
from .meta_analysis_post_body import MetaAnalysisPostBody
from .meta_analysis_provenance import MetaAnalysisProvenance
from .meta_analysis_return import MetaAnalysisReturn
from .metadata import Metadata
from .neurovault_collection import NeurovaultCollection
from .neurovault_collection_return import NeurovaultCollectionReturn
from .neurovault_file import NeurovaultFile
from .neurovault_file_list import NeurovaultFileList
from .neurovault_file_return import NeurovaultFileReturn
from .neurovault_list import NeurovaultList
from .project import Project
from .project_list import ProjectList
from .project_provenance import ProjectProvenance
from .project_return import ProjectReturn
from .read_only import ReadOnly
from .result import Result
from .result_images import ResultImages
from .result_list import ResultList
from .result_return import ResultReturn
from .specification import Specification
from .specification_list import SpecificationList
from .specification_post_body import SpecificationPostBody
from .specification_return import SpecificationReturn
from .studyset import Studyset
from .studyset_list import StudysetList
from .studyset_post_body import StudysetPostBody
from .studyset_return import StudysetReturn
from .studyset_snapshot import StudysetSnapshot
from .user import User
from .user_list import UserList
from .user_return import UserReturn

__all__ = (
    "Annotation",
    "AnnotationList",
    "AnnotationPost",
    "AnnotationPostBody",
    "AnnotationReturn",
    "AnnotationSnapshot",
    "Corrector",
    "CorrectorArgs",
    "Estimator",
    "EstimatorArgs",
    "MetaAnalysis",
    "MetaAnalysisList",
    "MetaAnalysisPostBody",
    "MetaAnalysisProvenance",
    "MetaAnalysisReturn",
    "Metadata",
    "NeurovaultCollection",
    "NeurovaultCollectionReturn",
    "NeurovaultFile",
    "NeurovaultFileList",
    "NeurovaultFileReturn",
    "NeurovaultList",
    "Project",
    "ProjectList",
    "ProjectProvenance",
    "ProjectReturn",
    "ReadOnly",
    "Result",
    "ResultImages",
    "ResultList",
    "ResultReturn",
    "Specification",
    "SpecificationList",
    "SpecificationPostBody",
    "SpecificationReturn",
    "Studyset",
    "StudysetList",
    "StudysetPostBody",
    "StudysetReturn",
    "StudysetSnapshot",
    "User",
    "UserList",
    "UserReturn",
)
