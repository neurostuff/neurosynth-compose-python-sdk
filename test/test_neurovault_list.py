# coding: utf-8

"""
    Analysis Specification for Meta-analysis

    api to create a meta-analysis specification

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from neurosynth_compose_sdk.models.neurovault_list import NeurovaultList

class TestNeurovaultList(unittest.TestCase):
    """NeurovaultList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NeurovaultList:
        """Test NeurovaultList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NeurovaultList`
        """
        model = NeurovaultList()
        if include_optional:
            return NeurovaultList(
                results = [
                    null
                    ],
                metadata = neurosynth_compose_sdk.models.metadata.metadata()
            )
        else:
            return NeurovaultList(
        )
        """

    def testNeurovaultList(self):
        """Test NeurovaultList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
