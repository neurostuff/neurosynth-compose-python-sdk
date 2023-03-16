# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from neurosynth_compose_sdk.paths.neurovault_collections_id import Api

from neurosynth_compose_sdk.paths import PathValues

path = PathValues.NEUROVAULTCOLLECTIONS_ID