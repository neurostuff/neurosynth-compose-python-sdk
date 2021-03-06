"""
    Analysis Specification for Meta-analysis

    api to create a meta-analysis specification  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import neurosynth_compose_sdk
from neurosynth_compose_sdk.model.annotation import Annotation
from neurosynth_compose_sdk.model.meta_analysis import MetaAnalysis
from neurosynth_compose_sdk.model.specification import Specification
from neurosynth_compose_sdk.model.studyset import Studyset
globals()['Annotation'] = Annotation
globals()['MetaAnalysis'] = MetaAnalysis
globals()['Specification'] = Specification
globals()['Studyset'] = Studyset
from neurosynth_compose_sdk.model.meta_analysis_post_body import MetaAnalysisPostBody


class TestMetaAnalysisPostBody(unittest.TestCase):
    """MetaAnalysisPostBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetaAnalysisPostBody(self):
        """Test MetaAnalysisPostBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetaAnalysisPostBody()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
