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

import neurosynth_compose_sdk
from neurosynth_compose_sdk.api.default_api import DefaultApi  # noqa: E501
from neurosynth_compose_sdk.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = neurosynth_compose_sdk.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_meta_analyses_id_delete(self):
        """Test case for meta_analyses_id_delete

          # noqa: E501
        """
        pass

    def test_neurostore_studies_get(self):
        """Test case for neurostore_studies_get

        Your GET endpoint  # noqa: E501
        """
        pass

    def test_neurostore_studies_id_get(self):
        """Test case for neurostore_studies_id_get

        Your GET endpoint  # noqa: E501
        """
        pass

    def test_neurostore_studies_id_put(self):
        """Test case for neurostore_studies_id_put

          # noqa: E501
        """
        pass

    def test_neurostore_studies_post(self):
        """Test case for neurostore_studies_post

          # noqa: E501
        """
        pass

    def test_projects_id_delete(self):
        """Test case for projects_id_delete

          # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
