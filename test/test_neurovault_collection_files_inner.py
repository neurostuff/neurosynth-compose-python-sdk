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
from neurosynth_compose_sdk.models.neurovault_collection_files_inner import NeurovaultCollectionFilesInner  # noqa: E501
from neurosynth_compose_sdk.rest import ApiException

class TestNeurovaultCollectionFilesInner(unittest.TestCase):
    """NeurovaultCollectionFilesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NeurovaultCollectionFilesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NeurovaultCollectionFilesInner`
        """
        model = neurosynth_compose_sdk.models.neurovault_collection_files_inner.NeurovaultCollectionFilesInner()  # noqa: E501
        if include_optional :
            return NeurovaultCollectionFilesInner(
                collection_id = '', 
                exception = '', 
                traceback = '', 
                status = '', 
                file = 'YQ==', 
                image_id = '', 
                name = '', 
                map_type = '', 
                cognitive_contrast_cogatlas = '', 
                cognitive_contrast_cogatlas_id = '', 
                cognitive_paradigm_cogatlas = '', 
                cognitive_paradigm_cogatlas_id = ''
            )
        else :
            return NeurovaultCollectionFilesInner(
        )
        """

    def testNeurovaultCollectionFilesInner(self):
        """Test NeurovaultCollectionFilesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
