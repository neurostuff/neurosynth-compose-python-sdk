# coding: utf-8

"""
    Analysis Specification for Meta-analysis

    api to create a meta-analysis specification  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from neurosynth_compose_sdk.models.corrector import Corrector
from neurosynth_compose_sdk.models.estimator import Estimator

class SpecificationPostBody(BaseModel):
    """
    SpecificationPostBody
    """
    type: Optional[StrictStr] = Field(None, description="the type of meta-analysis being run, typically either cbma or ibma, but others may become available in the future.")
    estimator: Optional[Estimator] = None
    mask: Optional[StrictStr] = Field(None, description="a string representing a binary nifti file to select which voxels a user wants to include in the analysis.")
    contrast: Optional[StrictStr] = Field(None, description="selection of categories in the filter column to differentiate groups, or \"neurosynth\", \"neuroquery\", or \"neurostore\" to compare to a database reference group")
    transformer: Optional[StrictStr] = Field(None, description="A transformation applied to column(s) (e.g., binarize based on a threshold). This is likely to become deprecated.")
    corrector: Optional[Corrector] = None
    filter: Optional[StrictStr] = Field(None, description="a column from annotations selecting which analyses to include in the meta-analysis")
    __properties = ["type", "estimator", "mask", "contrast", "transformer", "corrector", "filter"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SpecificationPostBody:
        """Create an instance of SpecificationPostBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of estimator
        if self.estimator:
            _dict['estimator'] = self.estimator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of corrector
        if self.corrector:
            _dict['corrector'] = self.corrector.to_dict()
        # set to None if mask (nullable) is None
        # and __fields_set__ contains the field
        if self.mask is None and "mask" in self.__fields_set__:
            _dict['mask'] = None

        # set to None if contrast (nullable) is None
        # and __fields_set__ contains the field
        if self.contrast is None and "contrast" in self.__fields_set__:
            _dict['contrast'] = None

        # set to None if transformer (nullable) is None
        # and __fields_set__ contains the field
        if self.transformer is None and "transformer" in self.__fields_set__:
            _dict['transformer'] = None

        # set to None if corrector (nullable) is None
        # and __fields_set__ contains the field
        if self.corrector is None and "corrector" in self.__fields_set__:
            _dict['corrector'] = None

        # set to None if filter (nullable) is None
        # and __fields_set__ contains the field
        if self.filter is None and "filter" in self.__fields_set__:
            _dict['filter'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpecificationPostBody:
        """Create an instance of SpecificationPostBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpecificationPostBody.parse_obj(obj)

        _obj = SpecificationPostBody.parse_obj({
            "type": obj.get("type"),
            "estimator": Estimator.from_dict(obj.get("estimator")) if obj.get("estimator") is not None else None,
            "mask": obj.get("mask"),
            "contrast": obj.get("contrast"),
            "transformer": obj.get("transformer"),
            "corrector": Corrector.from_dict(obj.get("corrector")) if obj.get("corrector") is not None else None,
            "filter": obj.get("filter")
        })
        return _obj

