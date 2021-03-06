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
from neurosynth_compose_sdk.model.corrector import Corrector
from neurosynth_compose_sdk.model.estimator import Estimator
from neurosynth_compose_sdk.model.specification import Specification
globals()['Corrector'] = Corrector
globals()['Estimator'] = Estimator
globals()['Specification'] = Specification
from neurosynth_compose_sdk.model.specification_post_body import SpecificationPostBody


class TestSpecificationPostBody(unittest.TestCase):
    """SpecificationPostBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSpecificationPostBody(self):
        """Test SpecificationPostBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SpecificationPostBody()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
