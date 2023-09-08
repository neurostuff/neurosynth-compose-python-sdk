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
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from neurosynth_compose_sdk.models.neurovault_collection_return import NeurovaultCollectionReturn

class ResultReturn(BaseModel):
    """
    ResultReturn
    """
    meta_analysis_id: Optional[StrictStr] = Field(None, description="the meta analysis this result was derived from.")
    cli_version: Optional[StrictStr] = Field(None, description="version of the command-line-tool that is uploading the results. ")
    neurovault_collection: Optional[NeurovaultCollectionReturn] = None
    methods_description: Optional[StrictStr] = Field(None, description="the description of the methods applied to create this result.")
    diagnostic_table: Optional[StrictStr] = Field(None, description="a text representation of a tsv that marks the contribution of each study to each particular cluster.")
    cli_args: Optional[Dict[str, Any]] = Field(None, description="additional parameters that were passed to the commandline tool at runtime. ")
    status: Optional[StrictStr] = None
    id: Optional[StrictStr] = Field(None, description="the identifier for the resource.")
    updated_at: Optional[datetime] = Field(None, description="when the resource was last modified.")
    created_at: Optional[datetime] = Field(None, description="When the resource was created.")
    user: Optional[StrictStr] = Field(None, description="Who owns the resource.")
    username: Optional[StrictStr] = None
    __properties = ["meta_analysis_id", "cli_version", "neurovault_collection", "methods_description", "diagnostic_table", "cli_args", "status", "id", "updated_at", "created_at", "user", "username"]

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
    def from_json(cls, json_str: str) -> ResultReturn:
        """Create an instance of ResultReturn from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of neurovault_collection
        if self.neurovault_collection:
            _dict['neurovault_collection'] = self.neurovault_collection.to_dict()
        # set to None if cli_version (nullable) is None
        # and __fields_set__ contains the field
        if self.cli_version is None and "cli_version" in self.__fields_set__:
            _dict['cli_version'] = None

        # set to None if methods_description (nullable) is None
        # and __fields_set__ contains the field
        if self.methods_description is None and "methods_description" in self.__fields_set__:
            _dict['methods_description'] = None

        # set to None if diagnostic_table (nullable) is None
        # and __fields_set__ contains the field
        if self.diagnostic_table is None and "diagnostic_table" in self.__fields_set__:
            _dict['diagnostic_table'] = None

        # set to None if cli_args (nullable) is None
        # and __fields_set__ contains the field
        if self.cli_args is None and "cli_args" in self.__fields_set__:
            _dict['cli_args'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

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
    def from_dict(cls, obj: dict) -> ResultReturn:
        """Create an instance of ResultReturn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ResultReturn.parse_obj(obj)

        _obj = ResultReturn.parse_obj({
            "meta_analysis_id": obj.get("meta_analysis_id"),
            "cli_version": obj.get("cli_version"),
            "neurovault_collection": NeurovaultCollectionReturn.from_dict(obj.get("neurovault_collection")) if obj.get("neurovault_collection") is not None else None,
            "methods_description": obj.get("methods_description"),
            "diagnostic_table": obj.get("diagnostic_table"),
            "cli_args": obj.get("cli_args"),
            "status": obj.get("status"),
            "id": obj.get("id"),
            "updated_at": obj.get("updated_at"),
            "created_at": obj.get("created_at"),
            "user": obj.get("user"),
            "username": obj.get("username")
        })
        return _obj

