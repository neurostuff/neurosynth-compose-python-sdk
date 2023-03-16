from neurosynth_compose_sdk.paths.neurovault_files.get import ApiForget
from neurosynth_compose_sdk.paths.neurovault_files.post import ApiForpost


class NeurovaultFiles(
    ApiForget,
    ApiForpost,
):
    pass
