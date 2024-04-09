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
from neurosynth_compose_sdk.api.specifications_api import SpecificationsApi  # noqa: E501
from neurosynth_compose_sdk.rest import ApiException


class TestSpecificationsApi(unittest.TestCase):
    """SpecificationsApi unit test stubs"""

    def setUp(self):
        self.api = neurosynth_compose_sdk.api.specifications_api.SpecificationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_specifications_get(self):
        """Test case for specifications_get

        Get a list of Specifications  # noqa: E501
        """
        pass

    def test_specifications_id_get(self):
        """Test case for specifications_id_get

        Get information about a Specification  # noqa: E501
        """
        pass

    def test_specifications_id_put(self):
        """Test case for specifications_id_put

        Update Meta-Analysis specification  # noqa: E501
        """
        pass

    def test_specifications_post(self):
        """Test case for specifications_post

        Create a Specification  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
