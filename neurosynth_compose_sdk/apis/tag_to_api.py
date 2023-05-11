import typing_extensions

from neurosynth_compose_sdk.apis.tags import TagValues
from neurosynth_compose_sdk.apis.tags.annotations_api import AnnotationsApi
from neurosynth_compose_sdk.apis.tags.compose_api import ComposeApi
from neurosynth_compose_sdk.apis.tags.get_api import GetApi
from neurosynth_compose_sdk.apis.tags.meta_analyses_api import MetaAnalysesApi
from neurosynth_compose_sdk.apis.tags.neurovault_api import NeurovaultApi
from neurosynth_compose_sdk.apis.tags.post_api import PostApi
from neurosynth_compose_sdk.apis.tags.projects_api import ProjectsApi
from neurosynth_compose_sdk.apis.tags.put_api import PutApi
from neurosynth_compose_sdk.apis.tags.specifications_api import SpecificationsApi
from neurosynth_compose_sdk.apis.tags.studysets_api import StudysetsApi
from neurosynth_compose_sdk.apis.tags.users_api import UsersApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ANNOTATIONS: AnnotationsApi,
        TagValues.COMPOSE: ComposeApi,
        TagValues.GET: GetApi,
        TagValues.META_ANALYSES: MetaAnalysesApi,
        TagValues.NEUROVAULT: NeurovaultApi,
        TagValues.POST: PostApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.PUT: PutApi,
        TagValues.SPECIFICATIONS: SpecificationsApi,
        TagValues.STUDYSETS: StudysetsApi,
        TagValues.USERS: UsersApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ANNOTATIONS: AnnotationsApi,
        TagValues.COMPOSE: ComposeApi,
        TagValues.GET: GetApi,
        TagValues.META_ANALYSES: MetaAnalysesApi,
        TagValues.NEUROVAULT: NeurovaultApi,
        TagValues.POST: PostApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.PUT: PutApi,
        TagValues.SPECIFICATIONS: SpecificationsApi,
        TagValues.STUDYSETS: StudysetsApi,
        TagValues.USERS: UsersApi,
    }
)
