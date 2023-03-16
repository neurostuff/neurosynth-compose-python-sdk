# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from neurosynth_compose_sdk.paths.neurovault_files_id import Api

from neurosynth_compose_sdk.paths import PathValues

path = PathValues.NEUROVAULTFILES_ID