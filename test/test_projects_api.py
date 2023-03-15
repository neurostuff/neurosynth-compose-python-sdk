"""
    Analysis Specification for Meta-analysis

    api to create a meta-analysis specification  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import neurosynth_compose_sdk
from neurosynth_compose_sdk.api.projects_api import ProjectsApi  # noqa: E501
from neurosynth_compose_sdk.api_client import ApiClient

class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = ProjectsApi(api_client=ApiClient())  # noqa: E501

    def tearDown(self):
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


if __name__ == '__main__':
    unittest.main()