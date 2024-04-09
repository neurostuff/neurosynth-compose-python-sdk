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
from neurosynth_compose_sdk.models.project_return import ProjectReturn  # noqa: E501
from neurosynth_compose_sdk.rest import ApiException

class TestProjectReturn(unittest.TestCase):
    """ProjectReturn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectReturn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectReturn`
        """
        model = neurosynth_compose_sdk.models.project_return.ProjectReturn()  # noqa: E501
        if include_optional :
            return ProjectReturn(
                id = '', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                user = '', 
                username = '', 
                provenance = neurosynth_compose_sdk.models.provenance.provenance(), 
                meta_analyses = None, 
                name = '', 
                description = '', 
                public = True, 
                neurostore_study = neurosynth_compose_sdk.models.neurostore_study.neurostore-study(
                    neurostore_id = '', 
                    analyses = [
                        neurosynth_compose_sdk.models.neurostore_analysis.neurostore-analysis(
                            neurostore_id = '', 
                            exception = '', 
                            traceback = '', 
                            status = '', )
                        ], 
                    exception = '', 
                    traceback = '', 
                    status = '', ), 
                neurostore_url = ''
            )
        else :
            return ProjectReturn(
        )
        """

    def testProjectReturn(self):
        """Test ProjectReturn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
