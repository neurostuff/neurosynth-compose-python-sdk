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


from typing import Optional, Union
from pydantic import BaseModel, StrictBytes, StrictStr

class NeurovaultFile(BaseModel):
    """
    NeurovaultFile
    """
    collection_id: Optional[StrictStr] = None
    exception: Optional[StrictStr] = None
    traceback: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    file: Optional[Union[StrictBytes, StrictStr]] = None
    image_id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    map_type: Optional[StrictStr] = None
    cognitive_contrast_cogatlas: Optional[StrictStr] = None
    cognitive_contrast_cogatlas_id: Optional[StrictStr] = None
    cognitive_paradigm_cogatlas: Optional[StrictStr] = None
    cognitive_paradigm_cogatlas_id: Optional[StrictStr] = None
    __properties = ["collection_id", "exception", "traceback", "status", "file", "image_id", "name", "map_type", "cognitive_contrast_cogatlas", "cognitive_contrast_cogatlas_id", "cognitive_paradigm_cogatlas", "cognitive_paradigm_cogatlas_id"]

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
    def from_json(cls, json_str: str) -> NeurovaultFile:
        """Create an instance of NeurovaultFile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
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

        # set to None if map_type (nullable) is None
        # and __fields_set__ contains the field
        if self.map_type is None and "map_type" in self.__fields_set__:
            _dict['map_type'] = None

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

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NeurovaultFile:
        """Create an instance of NeurovaultFile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NeurovaultFile.parse_obj(obj)

        _obj = NeurovaultFile.parse_obj({
            "collection_id": obj.get("collection_id"),
            "exception": obj.get("exception"),
            "traceback": obj.get("traceback"),
            "status": obj.get("status"),
            "file": obj.get("file"),
            "image_id": obj.get("image_id"),
            "name": obj.get("name"),
            "map_type": obj.get("map_type"),
            "cognitive_contrast_cogatlas": obj.get("cognitive_contrast_cogatlas"),
            "cognitive_contrast_cogatlas_id": obj.get("cognitive_contrast_cogatlas_id"),
            "cognitive_paradigm_cogatlas": obj.get("cognitive_paradigm_cogatlas"),
            "cognitive_paradigm_cogatlas_id": obj.get("cognitive_paradigm_cogatlas_id")
        })
        return _obj

