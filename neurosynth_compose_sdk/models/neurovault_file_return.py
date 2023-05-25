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
from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class NeurovaultFileReturn(BaseModel):
    """
    NeurovaultFileReturn
    """
    collection_id: Optional[StrictStr] = None
    exception: Optional[StrictStr] = None
    traceback: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    image_id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    id: Optional[StrictStr] = Field(None, description="the identifier for the resource.")
    updated_at: Optional[datetime] = Field(None, description="when the resource was last modified.")
    created_at: Optional[datetime] = Field(None, description="When the resource was created.")
    user: Optional[StrictStr] = Field(None, description="Who owns the resource.")
    __properties = ["collection_id", "exception", "traceback", "status", "image_id", "name", "url", "id", "updated_at", "created_at", "user"]

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
    def from_json(cls, json_str: str) -> NeurovaultFileReturn:
        """Create an instance of NeurovaultFileReturn from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "updated_at",
                            "created_at",
                          },
                          exclude_none=True)
        # set to None if collection_id (nullable) is None
        # and __fields_set__ contains the field
        if self.collection_id is None and "collection_id" in self.__fields_set__:
            _dict['collection_id'] = None

        # set to None if exception (nullable) is None
        # and __fields_set__ contains the field
        if self.exception is None and "exception" in self.__fields_set__:
            _dict['exception'] = None

        # set to None if traceback (nullable) is None
        # and __fields_set__ contains the field
        if self.traceback is None and "traceback" in self.__fields_set__:
            _dict['traceback'] = None

        # set to None if image_id (nullable) is None
        # and __fields_set__ contains the field
        if self.image_id is None and "image_id" in self.__fields_set__:
            _dict['image_id'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        # set to None if user (nullable) is None
        # and __fields_set__ contains the field
        if self.user is None and "user" in self.__fields_set__:
            _dict['user'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NeurovaultFileReturn:
        """Create an instance of NeurovaultFileReturn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NeurovaultFileReturn.parse_obj(obj)

        _obj = NeurovaultFileReturn.parse_obj({
            "collection_id": obj.get("collection_id"),
            "exception": obj.get("exception"),
            "traceback": obj.get("traceback"),
            "status": obj.get("status"),
            "image_id": obj.get("image_id"),
            "name": obj.get("name"),
            "url": obj.get("url"),
            "id": obj.get("id"),
            "updated_at": obj.get("updated_at"),
            "created_at": obj.get("created_at"),
            "user": obj.get("user")
        })
        return _obj

