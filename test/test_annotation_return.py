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
from neurosynth_compose_sdk.model.read_only import ReadOnly
globals()['Annotation'] = Annotation
globals()['ReadOnly'] = ReadOnly
from neurosynth_compose_sdk.model.annotation_return import AnnotationReturn


class TestAnnotationReturn(unittest.TestCase):
    """AnnotationReturn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAnnotationReturn(self):
        """Test AnnotationReturn"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AnnotationReturn()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()