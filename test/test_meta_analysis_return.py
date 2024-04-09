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
from neurosynth_compose_sdk.models.meta_analysis_return import MetaAnalysisReturn  # noqa: E501
from neurosynth_compose_sdk.rest import ApiException

class TestMetaAnalysisReturn(unittest.TestCase):
    """MetaAnalysisReturn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MetaAnalysisReturn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetaAnalysisReturn`
        """
        model = neurosynth_compose_sdk.models.meta_analysis_return.MetaAnalysisReturn()  # noqa: E501
        if include_optional :
            return MetaAnalysisReturn(
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
                id = '', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                user = '', 
                username = ''
            )
        else :
            return MetaAnalysisReturn(
        )
        """

    def testMetaAnalysisReturn(self):
        """Test MetaAnalysisReturn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
