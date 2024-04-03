from neurosynth_compose_sdk.paths.meta_analyses_id.get import ApiForget
from neurosynth_compose_sdk.paths.meta_analyses_id.put import ApiForput
from neurosynth_compose_sdk.paths.meta_analyses_id.delete import ApiFordelete


class MetaAnalysesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
