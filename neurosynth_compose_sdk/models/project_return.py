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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from neurosynth_compose_sdk.models.neurostore_study import NeurostoreStudy
from neurosynth_compose_sdk.models.project_meta_analyses import ProjectMetaAnalyses

class ProjectReturn(BaseModel):
    """
    ProjectReturn
    """
    id: Optional[StrictStr] = Field(None, description="the identifier for the resource.")
    updated_at: Optional[datetime] = Field(None, description="when the resource was last modified.")
    created_at: Optional[datetime] = Field(None, description="When the resource was created.")
    user: Optional[StrictStr] = Field(None, description="Who owns the resource.")
    provenance: Optional[Dict[str, Any]] = None
    meta_analyses: Optional[ProjectMetaAnalyses] = None
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    public: Optional[StrictBool] = Field(None, description="whether the project is public or private")
    neurostore_study: Optional[NeurostoreStudy] = None
    neurostore_url: Optional[StrictStr] = None
    __properties = ["id", "updated_at", "created_at", "user", "provenance", "meta_analyses", "name", "description", "public", "neurostore_study", "neurostore_url"]

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
    def from_json(cls, json_str: str) -> ProjectReturn:
        """Create an instance of ProjectReturn from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "updated_at",
                            "created_at",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of meta_analyses
        if self.meta_analyses:
            _dict['meta_analyses'] = self.meta_analyses.to_dict()
        # override the default output from pydantic by calling `to_dict()` of neurostore_study
        if self.neurostore_study:
            _dict['neurostore_study'] = self.neurostore_study.to_dict()
        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        # set to None if user (nullable) is None
        # and __fields_set__ contains the field
        if self.user is None and "user" in self.__fields_set__:
            _dict['user'] = None

        # set to None if provenance (nullable) is None
        # and __fields_set__ contains the field
        if self.provenance is None and "provenance" in self.__fields_set__:
            _dict['provenance'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if neurostore_url (nullable) is None
        # and __fields_set__ contains the field
        if self.neurostore_url is None and "neurostore_url" in self.__fields_set__:
            _dict['neurostore_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProjectReturn:
        """Create an instance of ProjectReturn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProjectReturn.parse_obj(obj)

        _obj = ProjectReturn.parse_obj({
            "id": obj.get("id"),
            "updated_at": obj.get("updated_at"),
            "created_at": obj.get("created_at"),
            "user": obj.get("user"),
            "provenance": obj.get("provenance"),
            "meta_analyses": ProjectMetaAnalyses.from_dict(obj.get("meta_analyses")) if obj.get("meta_analyses") is not None else None,
            "name": obj.get("name"),
            "description": obj.get("description"),
            "public": obj.get("public"),
            "neurostore_study": NeurostoreStudy.from_dict(obj.get("neurostore_study")) if obj.get("neurostore_study") is not None else None,
            "neurostore_url": obj.get("neurostore_url")
        })
        return _obj

