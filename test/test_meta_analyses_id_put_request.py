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
from neurosynth_compose_sdk.models.meta_analyses_id_put_request import MetaAnalysesIdPutRequest  # noqa: E501
from neurosynth_compose_sdk.rest import ApiException

class TestMetaAnalysesIdPutRequest(unittest.TestCase):
    """MetaAnalysesIdPutRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MetaAnalysesIdPutRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetaAnalysesIdPutRequest`
        """
        model = neurosynth_compose_sdk.models.meta_analyses_id_put_request.MetaAnalysesIdPutRequest()  # noqa: E501
        if include_optional :
            return MetaAnalysesIdPutRequest(
                specification = None, 
                studyset = None, 
                annotation = None, 
                name = '', 
                description = '', 
                cached_studyset_id = '', 
                cached_annotation_id = '', 
                results = None, 
                provenance = neurosynth_compose_sdk.models.provenance.provenance(), 
                project = '', 
                run_key = '', 
                neurostore_analysis = neurosynth_compose_sdk.models.neurostore_analysis.neurostore-analysis(
                    neurostore_id = '', 
                    exception = '', 
                    traceback = '', 
                    status = '', ), 
                cognitive_contrast_cogatlas = '', 
                cognitive_contrast_cogatlas_id = '', 
                cognitive_paradigm_cogatlas = '', 
                cognitive_paradigm_cogatlas_id = '', 
                cached_studyset = '', 
                cached_annotation = '', 
                neurostore_url = '', 
                create_neurostore_analysis = True
            )
        else :
            return MetaAnalysesIdPutRequest(
        )
        """

    def testMetaAnalysesIdPutRequest(self):
        """Test MetaAnalysesIdPutRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
