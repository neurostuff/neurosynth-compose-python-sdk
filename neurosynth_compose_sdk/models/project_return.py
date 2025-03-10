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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from neurosynth_compose_sdk.models.neurostore_study import NeurostoreStudy
from neurosynth_compose_sdk.models.project_meta_analyses import ProjectMetaAnalyses
from typing import Optional, Set
from typing_extensions import Self

class ProjectReturn(BaseModel):
    """
    ProjectReturn
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="the identifier for the resource.")
    updated_at: Optional[datetime] = Field(default=None, description="when the resource was last modified.")
    created_at: Optional[datetime] = Field(default=None, description="When the resource was created.")
    user: Optional[StrictStr] = Field(default=None, description="Who owns the resource.")
    username: Optional[StrictStr] = None
    provenance: Optional[Dict[str, Any]] = None
    meta_analyses: Optional[ProjectMetaAnalyses] = None
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    public: Optional[StrictBool] = Field(default=None, description="whether the project is public or private")
    neurostore_study: Optional[NeurostoreStudy] = None
    neurostore_url: Optional[StrictStr] = None
    draft: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "updated_at", "created_at", "user", "username", "provenance", "meta_analyses", "name", "description", "public", "neurostore_study", "neurostore_url", "draft"]

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
        """Create an instance of ProjectReturn from a JSON string"""
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
            "updated_at",
            "created_at",
            "username",
            "draft",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of meta_analyses
        if self.meta_analyses:
            _dict['meta_analyses'] = self.meta_analyses.to_dict()
        # override the default output from pydantic by calling `to_dict()` of neurostore_study
        if self.neurostore_study:
            _dict['neurostore_study'] = self.neurostore_study.to_dict()
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

        # set to None if provenance (nullable) is None
        # and model_fields_set contains the field
        if self.provenance is None and "provenance" in self.model_fields_set:
            _dict['provenance'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if neurostore_url (nullable) is None
        # and model_fields_set contains the field
        if self.neurostore_url is None and "neurostore_url" in self.model_fields_set:
            _dict['neurostore_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectReturn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "updated_at": obj.get("updated_at"),
            "created_at": obj.get("created_at"),
            "user": obj.get("user"),
            "username": obj.get("username"),
            "provenance": obj.get("provenance"),
            "meta_analyses": ProjectMetaAnalyses.from_dict(obj["meta_analyses"]) if obj.get("meta_analyses") is not None else None,
            "name": obj.get("name"),
            "description": obj.get("description"),
            "public": obj.get("public"),
            "neurostore_study": NeurostoreStudy.from_dict(obj["neurostore_study"]) if obj.get("neurostore_study") is not None else None,
            "neurostore_url": obj.get("neurostore_url"),
            "draft": obj.get("draft")
        })
        return _obj


