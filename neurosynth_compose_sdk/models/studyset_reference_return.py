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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from neurosynth_compose_sdk.models.studyset_reference_snapshots_inner import StudysetReferenceSnapshotsInner

class StudysetReferenceReturn(BaseModel):
    """
    StudysetReferenceReturn
    """
    snapshots: Optional[conlist(StudysetReferenceSnapshotsInner)] = None
    id: Optional[StrictStr] = Field(None, description="the identifier for the resource.")
    updated_at: Optional[datetime] = Field(None, description="when the resource was last modified.")
    created_at: Optional[datetime] = Field(None, description="When the resource was created.")
    user: Optional[StrictStr] = Field(None, description="Who owns the resource.")
    username: Optional[StrictStr] = None
    __properties = ["snapshots", "id", "updated_at", "created_at", "user", "username"]

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
    def from_json(cls, json_str: str) -> StudysetReferenceReturn:
        """Create an instance of StudysetReferenceReturn from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "updated_at",
                            "created_at",
                            "username",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in snapshots (list)
        _items = []
        if self.snapshots:
            for _item in self.snapshots:
                if _item:
                    _items.append(_item.to_dict())
            _dict['snapshots'] = _items
        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        # set to None if user (nullable) is None
        # and __fields_set__ contains the field
        if self.user is None and "user" in self.__fields_set__:
            _dict['user'] = None

        # set to None if username (nullable) is None
        # and __fields_set__ contains the field
        if self.username is None and "username" in self.__fields_set__:
            _dict['username'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StudysetReferenceReturn:
        """Create an instance of StudysetReferenceReturn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StudysetReferenceReturn.parse_obj(obj)

        _obj = StudysetReferenceReturn.parse_obj({
            "snapshots": [StudysetReferenceSnapshotsInner.from_dict(_item) for _item in obj.get("snapshots")] if obj.get("snapshots") is not None else None,
            "id": obj.get("id"),
            "updated_at": obj.get("updated_at"),
            "created_at": obj.get("created_at"),
            "user": obj.get("user"),
            "username": obj.get("username")
        })
        return _obj

