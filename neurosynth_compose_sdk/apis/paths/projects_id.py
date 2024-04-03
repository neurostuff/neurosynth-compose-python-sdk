from neurosynth_compose_sdk.paths.projects_id.get import ApiForget
from neurosynth_compose_sdk.paths.projects_id.put import ApiForput
from neurosynth_compose_sdk.paths.projects_id.delete import ApiFordelete


class ProjectsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
