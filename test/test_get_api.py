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
from neurosynth_compose_sdk.api.get_api import GetApi  # noqa: E501
from neurosynth_compose_sdk.rest import ApiException


class TestGetApi(unittest.TestCase):
    """GetApi unit test stubs"""

    def setUp(self):
        self.api = neurosynth_compose_sdk.api.get_api.GetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_annotations_get(self):
        """Test case for annotations_get

        GET a list of annotations  # noqa: E501
        """
        pass

    def test_annotations_id_get(self):
        """Test case for annotations_id_get

        GET information about an annotation  # noqa: E501
        """
        pass

    def test_meta_analyses_get(self):
        """Test case for meta_analyses_get

        GET a list of meta-analyses  # noqa: E501
        """
        pass

    def test_meta_analyses_id_get(self):
        """Test case for meta_analyses_id_get

        GET meta-analysis information  # noqa: E501
        """
        pass

    def test_meta_analysis_results_get(self):
        """Test case for meta_analysis_results_get

        Your GET endpoint  # noqa: E501
        """
        pass

    def test_meta_analysis_results_id_get(self):
        """Test case for meta_analysis_results_id_get

        Your GET endpoint  # noqa: E501
        """
        pass

    def test_neurovault_collections_get(self):
        """Test case for neurovault_collections_get

        Get neurovault collections  # noqa: E501
        """
        pass

    def test_neurovault_collections_id_get(self):
        """Test case for neurovault_collections_id_get

        Your GET endpoint  # noqa: E501
        """
        pass

    def test_neurovault_files_get(self):
        """Test case for neurovault_files_get

        Your GET endpoint  # noqa: E501
        """
        pass

    def test_neurovault_files_id_get(self):
        """Test case for neurovault_files_id_get

        Your GET endpoint  # noqa: E501
        """
        pass

    def test_projects_get(self):
        """Test case for projects_get

        Your GET endpoint  # noqa: E501
        """
        pass

    def test_projects_id_get(self):
        """Test case for projects_id_get

        Your GET endpoint  # noqa: E501
        """
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

    def test_studysets_get(self):
        """Test case for studysets_get

        Get a list of Studysets  # noqa: E501
        """
        pass

    def test_studysets_id_get(self):
        """Test case for studysets_id_get

        Get information about a Studyset  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
