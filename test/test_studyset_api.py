"""
    Analysis Specification for Meta-analysis

    api to create a meta-analysis specification  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import neurosynth_compose_sdk
from neurosynth_compose_sdk.api.studyset_api import StudysetApi  # noqa: E501
from neurosynth_compose_sdk.api_client import ApiClient

class TestStudysetApi(unittest.TestCase):
    """StudysetApi unit test stubs"""

    def setUp(self):
        self.api = StudysetApi(api_client=ApiClient())  # noqa: E501

    def tearDown(self):
        pass

    def test_studysets_get(self):
        """Test case for studysets_get

        Your GET endpoint  # noqa: E501
        """
        pass

    def test_studysets_id_get(self):
        """Test case for studysets_id_get

        Your GET endpoint  # noqa: E501
        """
        pass

    def test_studysets_id_put(self):
        """Test case for studysets_id_put

        Update Studyset  # noqa: E501
        """
        pass

    def test_studysets_post(self):
        """Test case for studysets_post

        Create Studyset  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()