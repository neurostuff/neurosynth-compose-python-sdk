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
from neurosynth_compose_sdk.models.neurovault_collection_return import NeurovaultCollectionReturn
from typing import Optional, Set
from typing_extensions import Self

class ResultReturn(BaseModel):
    """
    ResultReturn
    """ # noqa: E501
    meta_analysis_id: Optional[StrictStr] = Field(default=None, description="the meta analysis this result was derived from.")
    cli_version: Optional[StrictStr] = Field(default=None, description="version of the command-line-tool that is uploading the results. ")
    neurovault_collection: Optional[NeurovaultCollectionReturn] = None
    methods_description: Optional[StrictStr] = Field(default=None, description="the description of the methods applied to create this result.")
    diagnostic_table: Optional[StrictStr] = Field(default=None, description="a text representation of a tsv that marks the contribution of each study to each particular cluster.")
    cli_args: Optional[Dict[str, Any]] = Field(default=None, description="additional parameters that were passed to the commandline tool at runtime. ")
    status: Optional[StrictStr] = None
    id: Optional[StrictStr] = Field(default=None, description="the identifier for the resource.")
    updated_at: Optional[datetime] = Field(default=None, description="when the resource was last modified.")
    created_at: Optional[datetime] = Field(default=None, description="When the resource was created.")
    user: Optional[StrictStr] = Field(default=None, description="Who owns the resource.")
    username: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["meta_analysis_id", "cli_version", "neurovault_collection", "methods_description", "diagnostic_table", "cli_args", "status", "id", "updated_at", "created_at", "user", "username"]

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
        """Create an instance of ResultReturn from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "updated_at",
            "created_at",
            "username",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of neurovault_collection
        if self.neurovault_collection:
            _dict['neurovault_collection'] = self.neurovault_collection.to_dict()
        # set to None if cli_version (nullable) is None
        # and model_fields_set contains the field
        if self.cli_version is None and "cli_version" in self.model_fields_set:
            _dict['cli_version'] = None

        # set to None if methods_description (nullable) is None
        # and model_fields_set contains the field
        if self.methods_description is None and "methods_description" in self.model_fields_set:
            _dict['methods_description'] = None

        # set to None if diagnostic_table (nullable) is None
        # and model_fields_set contains the field
        if self.diagnostic_table is None and "diagnostic_table" in self.model_fields_set:
            _dict['diagnostic_table'] = None

        # set to None if cli_args (nullable) is None
        # and model_fields_set contains the field
        if self.cli_args is None and "cli_args" in self.model_fields_set:
            _dict['cli_args'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

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
        """Create an instance of ResultReturn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "meta_analysis_id": obj.get("meta_analysis_id"),
            "cli_version": obj.get("cli_version"),
            "neurovault_collection": NeurovaultCollectionReturn.from_dict(obj["neurovault_collection"]) if obj.get("neurovault_collection") is not None else None,
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


