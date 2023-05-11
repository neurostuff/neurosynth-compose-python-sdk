# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from neurosynth_compose_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    USERS_ID = "/users/{id}"
    USERS = "/users"
    METAANALYSES = "/meta-analyses"
    METAANALYSES_ID = "/meta-analyses/{id}"
    STUDYSETS = "/studysets"
    STUDYSETS_ID = "/studysets/{id}"
    ANNOTATIONS = "/annotations"
    ANNOTATIONS_ID = "/annotations/{id}"
    SPECIFICATIONS = "/specifications"
    SPECIFICATIONS_ID = "/specifications/{id}"
    METAANALYSISRESULTS = "/meta-analysis-results"
    METAANALYSISRESULTS_ID = "/meta-analysis-results/{id}"
    NEUROVAULTCOLLECTIONS = "/neurovault-collections"
    NEUROVAULTCOLLECTIONS_ID = "/neurovault-collections/{id}"
    NEUROVAULTFILES = "/neurovault-files"
    NEUROVAULTFILES_ID = "/neurovault-files/{id}"
    PROJECTS = "/projects"
    PROJECTS_ID = "/projects/{id}"
    NEUROSTORESTUDIES = "/neurostore-studies"
    NEUROSTORESTUDIES_ID = "/neurostore-studies/{id}"
