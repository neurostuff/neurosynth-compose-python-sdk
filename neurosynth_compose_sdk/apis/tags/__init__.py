# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from neurosynth_compose_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ANNOTATIONS = "annotations"
    COMPOSE = "compose"
    GET = "get"
    META_ANALYSES = "meta_analyses"
    NEUROVAULT = "neurovault"
    POST = "post"
    PROJECTS = "projects"
    PUT = "put"
    SPECIFICATIONS = "specifications"
    STUDYSETS = "studysets"
    USERS = "users"
    DEFAULT = "default"
