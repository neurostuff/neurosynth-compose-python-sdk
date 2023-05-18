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
from neurosynth_compose_sdk.models.meta_analysis_annotation import MetaAnalysisAnnotation
from neurosynth_compose_sdk.models.meta_analysis_results import MetaAnalysisResults
from neurosynth_compose_sdk.models.meta_analysis_specification import MetaAnalysisSpecification
from neurosynth_compose_sdk.models.meta_analysis_studyset import MetaAnalysisStudyset

class MetaAnalysisReturn(BaseModel):
    """
    MetaAnalysisReturn
    """
    specification: Optional[MetaAnalysisSpecification] = None
    studyset: Optional[MetaAnalysisStudyset] = None
    annotation: Optional[MetaAnalysisAnnotation] = None
    name: Optional[StrictStr] = Field(None, description="Human-readable name of the meta-analysis.")
    description: Optional[StrictStr] = Field(None, description="Long form description of the meta-analysis.")
    cached_studyset_id: Optional[StrictStr] = Field(None, description="The id of the studyset on neurosynth-compose (as opposed to the id of the studyset on neurostore). Multiple snapshots of the studyset can be stored on neurosynth-compose so knowing which snapshot is being referenced is necessary.")
    cached_annotation_id: Optional[StrictStr] = Field(None, description="The id of the annotation on neurosynth-compose (as opposed to the id of the annotation on neurostore). Multiple snapshots of the annotation can be stored on neurosynth-compose so knowing which snapshot is being referenced is necessary.")
    results: Optional[MetaAnalysisResults] = None
    provenance: Optional[Dict[str, Any]] = None
    project: Optional[StrictStr] = None
    run_key: Optional[StrictStr] = Field(None, description="a special key used to upload the results of this meta analysis. Can be used as an alternative to using your auth token from login. ")
    neurostore_analysis_id: Optional[StrictStr] = None
    hash: Optional[StrictStr] = Field(None, description="TODO: create hash of studyset and annotation and use that for the run_key")
    cognitive_contrast_cogatlas: Optional[StrictStr] = None
    cognitive_contrast_cogatlas_id: Optional[StrictStr] = None
    cognitive_paradigm_cogatlas: Optional[StrictStr] = None
    cognitive_paradigm_cogatlas_id: Optional[StrictStr] = None
    cached_studyset: Optional[StrictStr] = None
    cached_annotation: Optional[StrictStr] = None
    id: Optional[StrictStr] = Field(None, description="the identifier for the resource.")
    updated_at: Optional[datetime] = Field(None, description="when the resource was last modified.")
    created_at: Optional[datetime] = Field(None, description="When the resource was created.")
    user: Optional[StrictStr] = Field(None, description="Who owns the resource.")
    __properties = ["specification", "studyset", "annotation", "name", "description", "cached_studyset_id", "cached_annotation_id", "results", "provenance", "project", "run_key", "neurostore_analysis_id", "hash", "cognitive_contrast_cogatlas", "cognitive_contrast_cogatlas_id", "cognitive_paradigm_cogatlas", "cognitive_paradigm_cogatlas_id", "cached_studyset", "cached_annotation", "id", "updated_at", "created_at", "user"]

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
    def from_json(cls, json_str: str) -> MetaAnalysisReturn:
        """Create an instance of MetaAnalysisReturn from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "run_key",
                            "neurostore_analysis_id",
                            "cached_studyset",
                            "cached_annotation",
                            "updated_at",
                            "created_at",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of specification
        if self.specification:
            _dict['specification'] = self.specification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of studyset
        if self.studyset:
            _dict['studyset'] = self.studyset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of annotation
        if self.annotation:
            _dict['annotation'] = self.annotation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of results
        if self.results:
            _dict['results'] = self.results.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if provenance (nullable) is None
        # and __fields_set__ contains the field
        if self.provenance is None and "provenance" in self.__fields_set__:
            _dict['provenance'] = None

        # set to None if project (nullable) is None
        # and __fields_set__ contains the field
        if self.project is None and "project" in self.__fields_set__:
            _dict['project'] = None

        # set to None if neurostore_analysis_id (nullable) is None
        # and __fields_set__ contains the field
        if self.neurostore_analysis_id is None and "neurostore_analysis_id" in self.__fields_set__:
            _dict['neurostore_analysis_id'] = None

        # set to None if hash (nullable) is None
        # and __fields_set__ contains the field
        if self.hash is None and "hash" in self.__fields_set__:
            _dict['hash'] = None

        # set to None if cognitive_contrast_cogatlas (nullable) is None
        # and __fields_set__ contains the field
        if self.cognitive_contrast_cogatlas is None and "cognitive_contrast_cogatlas" in self.__fields_set__:
            _dict['cognitive_contrast_cogatlas'] = None

        # set to None if cognitive_contrast_cogatlas_id (nullable) is None
        # and __fields_set__ contains the field
        if self.cognitive_contrast_cogatlas_id is None and "cognitive_contrast_cogatlas_id" in self.__fields_set__:
            _dict['cognitive_contrast_cogatlas_id'] = None

        # set to None if cognitive_paradigm_cogatlas (nullable) is None
        # and __fields_set__ contains the field
        if self.cognitive_paradigm_cogatlas is None and "cognitive_paradigm_cogatlas" in self.__fields_set__:
            _dict['cognitive_paradigm_cogatlas'] = None

        # set to None if cognitive_paradigm_cogatlas_id (nullable) is None
        # and __fields_set__ contains the field
        if self.cognitive_paradigm_cogatlas_id is None and "cognitive_paradigm_cogatlas_id" in self.__fields_set__:
            _dict['cognitive_paradigm_cogatlas_id'] = None

        # set to None if cached_studyset (nullable) is None
        # and __fields_set__ contains the field
        if self.cached_studyset is None and "cached_studyset" in self.__fields_set__:
            _dict['cached_studyset'] = None

        # set to None if cached_annotation (nullable) is None
        # and __fields_set__ contains the field
        if self.cached_annotation is None and "cached_annotation" in self.__fields_set__:
            _dict['cached_annotation'] = None

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
    def from_dict(cls, obj: dict) -> MetaAnalysisReturn:
        """Create an instance of MetaAnalysisReturn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MetaAnalysisReturn.parse_obj(obj)

        _obj = MetaAnalysisReturn.parse_obj({
            "specification": MetaAnalysisSpecification.from_dict(obj.get("specification")) if obj.get("specification") is not None else None,
            "studyset": MetaAnalysisStudyset.from_dict(obj.get("studyset")) if obj.get("studyset") is not None else None,
            "annotation": MetaAnalysisAnnotation.from_dict(obj.get("annotation")) if obj.get("annotation") is not None else None,
            "name": obj.get("name"),
            "description": obj.get("description"),
            "cached_studyset_id": obj.get("cached_studyset_id"),
            "cached_annotation_id": obj.get("cached_annotation_id"),
            "results": MetaAnalysisResults.from_dict(obj.get("results")) if obj.get("results") is not None else None,
            "provenance": obj.get("provenance"),
            "project": obj.get("project"),
            "run_key": obj.get("run_key"),
            "neurostore_analysis_id": obj.get("neurostore_analysis_id"),
            "hash": obj.get("hash"),
            "cognitive_contrast_cogatlas": obj.get("cognitive_contrast_cogatlas"),
            "cognitive_contrast_cogatlas_id": obj.get("cognitive_contrast_cogatlas_id"),
            "cognitive_paradigm_cogatlas": obj.get("cognitive_paradigm_cogatlas"),
            "cognitive_paradigm_cogatlas_id": obj.get("cognitive_paradigm_cogatlas_id"),
            "cached_studyset": obj.get("cached_studyset"),
            "cached_annotation": obj.get("cached_annotation"),
            "id": obj.get("id"),
            "updated_at": obj.get("updated_at"),
            "created_at": obj.get("created_at"),
            "user": obj.get("user")
        })
        return _obj

