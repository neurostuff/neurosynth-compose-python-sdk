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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr

class AnnotationPostBody(BaseModel):
    """
    AnnotationPostBody
    """
    cached_studyset_id: StrictStr = Field(...)
    neurostore_id: Optional[StrictStr] = Field(None, description="the id of the annotation on neurostore")
    snapshot: Optional[Dict[str, Any]] = Field(None, description="the snapshot taken of the annotation pending a successful run of the meta-analytic algorithm")
    studyset: Optional[StrictStr] = Field(None, description="The related cached studyset to this annotation.")
    __properties = ["cached_studyset_id", "neurostore_id", "snapshot", "studyset"]

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
    def from_json(cls, json_str: str) -> AnnotationPostBody:
        """Create an instance of AnnotationPostBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "studyset",
                          },
                          exclude_none=True)
        # set to None if snapshot (nullable) is None
        # and __fields_set__ contains the field
        if self.snapshot is None and "snapshot" in self.__fields_set__:
            _dict['snapshot'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AnnotationPostBody:
        """Create an instance of AnnotationPostBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AnnotationPostBody.parse_obj(obj)

        _obj = AnnotationPostBody.parse_obj({
            "cached_studyset_id": obj.get("cached_studyset_id"),
            "neurostore_id": obj.get("neurostore_id"),
            "snapshot": obj.get("snapshot"),
            "studyset": obj.get("studyset")
        })
        return _obj

