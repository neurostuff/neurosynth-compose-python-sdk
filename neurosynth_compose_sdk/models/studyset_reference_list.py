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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, conlist
from neurosynth_compose_sdk.models.studyset_reference_return import StudysetReferenceReturn

class StudysetReferenceList(BaseModel):
    """
    StudysetReferenceList
    """
    results: Optional[conlist(StudysetReferenceReturn)] = None
    metadata: Optional[Dict[str, Any]] = None
    __properties = ["results", "metadata"]

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
    def from_json(cls, json_str: str) -> StudysetReferenceList:
        """Create an instance of StudysetReferenceList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StudysetReferenceList:
        """Create an instance of StudysetReferenceList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StudysetReferenceList.parse_obj(obj)

        _obj = StudysetReferenceList.parse_obj({
            "results": [StudysetReferenceReturn.from_dict(_item) for _item in obj.get("results")] if obj.get("results") is not None else None,
            "metadata": obj.get("metadata")
        })
        return _obj

