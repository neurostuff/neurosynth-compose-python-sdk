# coding: utf-8

"""
    Analysis Specification for Meta-analysis

    api to create a meta-analysis specification  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from neurosynth_compose_sdk import schemas  # noqa: F401


class Result(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    describes the output of a meta-analysis
    """


    class MetaOapg:
        
        class properties:
            meta_analysis_id = schemas.StrSchema
            
            
            class cli_version(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cli_version':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class neurovault_collection_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'neurovault_collection_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class methods_description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'methods_description':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class neurovault_images(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NeurovaultFile']:
                        return NeurovaultFile
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'neurovault_images':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            diagnostic_table = schemas.StrSchema
            cli_args = schemas.DictSchema
            __annotations__ = {
                "meta_analysis_id": meta_analysis_id,
                "cli_version": cli_version,
                "neurovault_collection_id": neurovault_collection_id,
                "methods_description": methods_description,
                "neurovault_images": neurovault_images,
                "diagnostic_table": diagnostic_table,
                "cli_args": cli_args,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta_analysis_id"]) -> MetaOapg.properties.meta_analysis_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cli_version"]) -> MetaOapg.properties.cli_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["neurovault_collection_id"]) -> MetaOapg.properties.neurovault_collection_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["methods_description"]) -> MetaOapg.properties.methods_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["neurovault_images"]) -> MetaOapg.properties.neurovault_images: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["diagnostic_table"]) -> MetaOapg.properties.diagnostic_table: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cli_args"]) -> MetaOapg.properties.cli_args: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["meta_analysis_id", "cli_version", "neurovault_collection_id", "methods_description", "neurovault_images", "diagnostic_table", "cli_args", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta_analysis_id"]) -> typing.Union[MetaOapg.properties.meta_analysis_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cli_version"]) -> typing.Union[MetaOapg.properties.cli_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["neurovault_collection_id"]) -> typing.Union[MetaOapg.properties.neurovault_collection_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["methods_description"]) -> typing.Union[MetaOapg.properties.methods_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["neurovault_images"]) -> typing.Union[MetaOapg.properties.neurovault_images, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["diagnostic_table"]) -> typing.Union[MetaOapg.properties.diagnostic_table, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cli_args"]) -> typing.Union[MetaOapg.properties.cli_args, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["meta_analysis_id", "cli_version", "neurovault_collection_id", "methods_description", "neurovault_images", "diagnostic_table", "cli_args", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        meta_analysis_id: typing.Union[MetaOapg.properties.meta_analysis_id, str, schemas.Unset] = schemas.unset,
        cli_version: typing.Union[MetaOapg.properties.cli_version, None, str, schemas.Unset] = schemas.unset,
        neurovault_collection_id: typing.Union[MetaOapg.properties.neurovault_collection_id, None, str, schemas.Unset] = schemas.unset,
        methods_description: typing.Union[MetaOapg.properties.methods_description, None, str, schemas.Unset] = schemas.unset,
        neurovault_images: typing.Union[MetaOapg.properties.neurovault_images, list, tuple, None, schemas.Unset] = schemas.unset,
        diagnostic_table: typing.Union[MetaOapg.properties.diagnostic_table, str, schemas.Unset] = schemas.unset,
        cli_args: typing.Union[MetaOapg.properties.cli_args, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Result':
        return super().__new__(
            cls,
            *_args,
            meta_analysis_id=meta_analysis_id,
            cli_version=cli_version,
            neurovault_collection_id=neurovault_collection_id,
            methods_description=methods_description,
            neurovault_images=neurovault_images,
            diagnostic_table=diagnostic_table,
            cli_args=cli_args,
            _configuration=_configuration,
            **kwargs,
        )

from neurosynth_compose_sdk.model.neurovault_file import NeurovaultFile
