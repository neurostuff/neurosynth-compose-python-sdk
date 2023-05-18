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


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist
from neurosynth_compose_sdk.models.neurovault_collection_files_inner import NeurovaultCollectionFilesInner

class NeurovaultCollection(BaseModel):
    """
    NeurovaultCollection
    """
    collection_id: Optional[StrictStr] = None
    files: Optional[conlist(NeurovaultCollectionFilesInner)] = None
    result: Optional[StrictStr] = None
    __properties = ["collection_id", "files", "result"]

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
    def from_json(cls, json_str: str) -> NeurovaultCollection:
        """Create an instance of NeurovaultCollection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "collection_id",
                            "result",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item in self.files:
                if _item:
                    _items.append(_item.to_dict())
            _dict['files'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NeurovaultCollection:
        """Create an instance of NeurovaultCollection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NeurovaultCollection.parse_obj(obj)

        _obj = NeurovaultCollection.parse_obj({
            "collection_id": obj.get("collection_id"),
            "files": [NeurovaultCollectionFilesInner.from_dict(_item) for _item in obj.get("files")] if obj.get("files") is not None else None,
            "result": obj.get("result")
        })
        return _obj

