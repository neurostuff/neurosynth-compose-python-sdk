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
from neurosynth_compose_sdk.models.neurostore_study import NeurostoreStudy  # noqa: E501
from neurosynth_compose_sdk.rest import ApiException

class TestNeurostoreStudy(unittest.TestCase):
    """NeurostoreStudy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NeurostoreStudy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NeurostoreStudy`
        """
        model = neurosynth_compose_sdk.models.neurostore_study.NeurostoreStudy()  # noqa: E501
        if include_optional :
            return NeurostoreStudy(
                neurostore_id = '', 
                analyses = [
                    neurosynth_compose_sdk.models.neurostore_analysis.neurostore-analysis(
                        neurostore_id = '', 
                        exception = '', 
                        traceback = '', 
                        status = '', )
                    ]
            )
        else :
            return NeurostoreStudy(
        )
        """

    def testNeurostoreStudy(self):
        """Test NeurostoreStudy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()