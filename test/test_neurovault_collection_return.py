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

from neurosynth_compose_sdk.models.neurovault_collection_return import NeurovaultCollectionReturn

class TestNeurovaultCollectionReturn(unittest.TestCase):
    """NeurovaultCollectionReturn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NeurovaultCollectionReturn:
        """Test NeurovaultCollectionReturn
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NeurovaultCollectionReturn`
        """
        model = NeurovaultCollectionReturn()
        if include_optional:
            return NeurovaultCollectionReturn(
                collection_id = '',
                files = None,
                url = '',
                id = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user = '',
                username = ''
            )
        else:
            return NeurovaultCollectionReturn(
        )
        """

    def testNeurovaultCollectionReturn(self):
        """Test NeurovaultCollectionReturn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
