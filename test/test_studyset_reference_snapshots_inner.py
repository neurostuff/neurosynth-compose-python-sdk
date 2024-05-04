# coding: utf-8

"""
    Analysis Specification for Meta-analysis

    api to create a meta-analysis specification  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.studyset_reference_snapshots_inner import StudysetReferenceSnapshotsInner  # noqa: E501
from neurosynth_compose_sdk.rest import ApiException

class TestStudysetReferenceSnapshotsInner(unittest.TestCase):
    """StudysetReferenceSnapshotsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StudysetReferenceSnapshotsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StudysetReferenceSnapshotsInner`
        """
        model = neurosynth_compose_sdk.models.studyset_reference_snapshots_inner.StudysetReferenceSnapshotsInner()  # noqa: E501
        if include_optional :
            return StudysetReferenceSnapshotsInner(
                neurostore_id = '', 
                snapshot = neurosynth_compose_sdk.models.snapshot.snapshot(), 
                neurostore_url = '', 
                version = ''
            )
        else :
            return StudysetReferenceSnapshotsInner(
        )
        """

    def testStudysetReferenceSnapshotsInner(self):
        """Test StudysetReferenceSnapshotsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()