# coding: utf-8

"""
    Analysis Specification for Meta-analysis

    api to create a meta-analysis specification

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from neurosynth_compose_sdk.models.neurovault_collection_files import NeurovaultCollectionFiles
from typing import Optional, Set
from typing_extensions import Self

class NeurovaultCollectionReturn(BaseModel):
    """
    NeurovaultCollectionReturn
    """ # noqa: E501
    collection_id: Optional[StrictStr] = None
    files: Optional[NeurovaultCollectionFiles] = None
    url: Optional[StrictStr] = None
    id: Optional[StrictStr] = Field(default=None, description="the identifier for the resource.")
    updated_at: Optional[datetime] = Field(default=None, description="when the resource was last modified.")
    created_at: Optional[datetime] = Field(default=None, description="When the resource was created.")
    user: Optional[StrictStr] = Field(default=None, description="Who owns the resource.")
    username: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["collection_id", "files", "url", "id", "updated_at", "created_at", "user", "username"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of NeurovaultCollectionReturn from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "collection_id",
            "updated_at",
            "created_at",
            "username",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of files
        if self.files:
            _dict['files'] = self.files.to_dict()
        # set to None if collection_id (nullable) is None
        # and model_fields_set contains the field
        if self.collection_id is None and "collection_id" in self.model_fields_set:
            _dict['collection_id'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NeurovaultCollectionReturn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "collection_id": obj.get("collection_id"),
            "files": NeurovaultCollectionFiles.from_dict(obj["files"]) if obj.get("files") is not None else None,
            "url": obj.get("url"),
            "id": obj.get("id"),
            "updated_at": obj.get("updated_at"),
            "created_at": obj.get("created_at"),
            "user": obj.get("user"),
            "username": obj.get("username")
        })
        return _obj


