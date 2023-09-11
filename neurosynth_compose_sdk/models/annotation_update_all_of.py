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
from pydantic import BaseModel, StrictStr

class AnnotationUpdateAllOf(BaseModel):
    """
    AnnotationUpdateAllOf
    """
    cached_studyset_id: Optional[StrictStr] = None
    __properties = ["cached_studyset_id"]

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
    def from_json(cls, json_str: str) -> AnnotationUpdateAllOf:
        """Create an instance of AnnotationUpdateAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AnnotationUpdateAllOf:
        """Create an instance of AnnotationUpdateAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AnnotationUpdateAllOf.parse_obj(obj)

        _obj = AnnotationUpdateAllOf.parse_obj({
            "cached_studyset_id": obj.get("cached_studyset_id")
        })
        return _obj
