# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from neurosynth_compose_sdk.api.annotations_api import AnnotationsApi
    from neurosynth_compose_sdk.api.default_api import DefaultApi
    from neurosynth_compose_sdk.api.meta_analyses_api import MetaAnalysesApi
    from neurosynth_compose_sdk.api.neurovault_api import NeurovaultApi
    from neurosynth_compose_sdk.api.projects_api import ProjectsApi
    from neurosynth_compose_sdk.api.specifications_api import SpecificationsApi
    from neurosynth_compose_sdk.api.studysets_api import StudysetsApi
    from neurosynth_compose_sdk.api.tags_api import TagsApi
    from neurosynth_compose_sdk.api.users_api import UsersApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from neurosynth_compose_sdk.api.annotations_api import AnnotationsApi
from neurosynth_compose_sdk.api.default_api import DefaultApi
from neurosynth_compose_sdk.api.meta_analyses_api import MetaAnalysesApi
from neurosynth_compose_sdk.api.neurovault_api import NeurovaultApi
from neurosynth_compose_sdk.api.projects_api import ProjectsApi
from neurosynth_compose_sdk.api.specifications_api import SpecificationsApi
from neurosynth_compose_sdk.api.studysets_api import StudysetsApi
from neurosynth_compose_sdk.api.tags_api import TagsApi
from neurosynth_compose_sdk.api.users_api import UsersApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
