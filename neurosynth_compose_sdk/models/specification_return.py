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
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from neurosynth_compose_sdk.models.corrector import Corrector
from neurosynth_compose_sdk.models.estimator import Estimator
from neurosynth_compose_sdk.models.specification_conditions import SpecificationConditions

class SpecificationReturn(BaseModel):
    """
    The view of the specification through an endpoint.
    """
    type: Optional[StrictStr] = Field(None, description="the type of meta-analysis being run, typically either cbma or ibma, but others may become available in the future.")
    estimator: Optional[Estimator] = None
    mask: Optional[StrictStr] = Field(None, description="a string representing a binary nifti file to select which voxels a user wants to include in the analysis.")
    conditions: Optional[SpecificationConditions] = None
    weights: Optional[conlist(Union[StrictFloat, StrictInt])] = None
    transformer: Optional[StrictStr] = Field(None, description="A transformation applied to column(s) (e.g., binarize based on a threshold). This is likely to become deprecated.")
    corrector: Optional[Corrector] = None
    filter: Optional[StrictStr] = Field(None, description="a column from annotations selecting which analyses to include in the meta-analysis")
    database_studyset: Optional[StrictStr] = None
    id: Optional[StrictStr] = Field(None, description="the identifier for the resource.")
    updated_at: Optional[datetime] = Field(None, description="when the resource was last modified.")
    created_at: Optional[datetime] = Field(None, description="When the resource was created.")
    user: Optional[StrictStr] = Field(None, description="Who owns the resource.")
    username: Optional[StrictStr] = None
    __properties = ["type", "estimator", "mask", "conditions", "weights", "transformer", "corrector", "filter", "database_studyset", "id", "updated_at", "created_at", "user", "username"]

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
    def from_json(cls, json_str: str) -> SpecificationReturn:
        """Create an instance of SpecificationReturn from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of estimator
        if self.estimator:
            _dict['estimator'] = self.estimator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conditions
        if self.conditions:
            _dict['conditions'] = self.conditions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of corrector
        if self.corrector:
            _dict['corrector'] = self.corrector.to_dict()
        # set to None if mask (nullable) is None
        # and __fields_set__ contains the field
        if self.mask is None and "mask" in self.__fields_set__:
            _dict['mask'] = None

        # set to None if weights (nullable) is None
        # and __fields_set__ contains the field
        if self.weights is None and "weights" in self.__fields_set__:
            _dict['weights'] = None

        # set to None if transformer (nullable) is None
        # and __fields_set__ contains the field
        if self.transformer is None and "transformer" in self.__fields_set__:
            _dict['transformer'] = None

        # set to None if corrector (nullable) is None
        # and __fields_set__ contains the field
        if self.corrector is None and "corrector" in self.__fields_set__:
            _dict['corrector'] = None

        # set to None if filter (nullable) is None
        # and __fields_set__ contains the field
        if self.filter is None and "filter" in self.__fields_set__:
            _dict['filter'] = None

        # set to None if database_studyset (nullable) is None
        # and __fields_set__ contains the field
        if self.database_studyset is None and "database_studyset" in self.__fields_set__:
            _dict['database_studyset'] = None

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
    def from_dict(cls, obj: dict) -> SpecificationReturn:
        """Create an instance of SpecificationReturn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpecificationReturn.parse_obj(obj)

        _obj = SpecificationReturn.parse_obj({
            "type": obj.get("type"),
            "estimator": Estimator.from_dict(obj.get("estimator")) if obj.get("estimator") is not None else None,
            "mask": obj.get("mask"),
            "conditions": SpecificationConditions.from_dict(obj.get("conditions")) if obj.get("conditions") is not None else None,
            "weights": obj.get("weights"),
            "transformer": obj.get("transformer"),
            "corrector": Corrector.from_dict(obj.get("corrector")) if obj.get("corrector") is not None else None,
            "filter": obj.get("filter"),
            "database_studyset": obj.get("database_studyset"),
            "id": obj.get("id"),
            "updated_at": obj.get("updated_at"),
            "created_at": obj.get("created_at"),
            "user": obj.get("user"),
            "username": obj.get("username")
        })
        return _obj

