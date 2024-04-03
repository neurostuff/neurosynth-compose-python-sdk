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


class Specification(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    a machine readable specification of how to run a meta-analysis (currently specifically tailored to NiMARE).
    """


    class MetaOapg:
        
        class properties:
            type = schemas.StrSchema
        
            @staticmethod
            def estimator() -> typing.Type['Estimator']:
                return Estimator
            
            
            class mask(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mask':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class conditions(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class one_of_0(
                        schemas.ListBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneTupleMixin
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                            min_items = 1
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[list, tuple, None, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'one_of_0':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                            )
                    
                    
                    class one_of_1(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.BoolSchema
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, bool, ]], typing.List[typing.Union[MetaOapg.items, bool, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'one_of_1':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.one_of_0,
                            cls.one_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'conditions':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class weights(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'weights':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class transformer(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transformer':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def corrector() -> typing.Type['Corrector']:
                return Corrector
            
            
            class filter(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'filter':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class database_studyset(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'database_studyset':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "type": type,
                "estimator": estimator,
                "mask": mask,
                "conditions": conditions,
                "weights": weights,
                "transformer": transformer,
                "corrector": corrector,
                "filter": filter,
                "database_studyset": database_studyset,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["estimator"]) -> 'Estimator': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mask"]) -> MetaOapg.properties.mask: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weights"]) -> MetaOapg.properties.weights: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transformer"]) -> MetaOapg.properties.transformer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["corrector"]) -> 'Corrector': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filter"]) -> MetaOapg.properties.filter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["database_studyset"]) -> MetaOapg.properties.database_studyset: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "estimator", "mask", "conditions", "weights", "transformer", "corrector", "filter", "database_studyset", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["estimator"]) -> typing.Union['Estimator', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mask"]) -> typing.Union[MetaOapg.properties.mask, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union[MetaOapg.properties.conditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weights"]) -> typing.Union[MetaOapg.properties.weights, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transformer"]) -> typing.Union[MetaOapg.properties.transformer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["corrector"]) -> typing.Union['Corrector', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filter"]) -> typing.Union[MetaOapg.properties.filter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["database_studyset"]) -> typing.Union[MetaOapg.properties.database_studyset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "estimator", "mask", "conditions", "weights", "transformer", "corrector", "filter", "database_studyset", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        estimator: typing.Union['Estimator', schemas.Unset] = schemas.unset,
        mask: typing.Union[MetaOapg.properties.mask, None, str, schemas.Unset] = schemas.unset,
        conditions: typing.Union[MetaOapg.properties.conditions, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        weights: typing.Union[MetaOapg.properties.weights, list, tuple, None, schemas.Unset] = schemas.unset,
        transformer: typing.Union[MetaOapg.properties.transformer, None, str, schemas.Unset] = schemas.unset,
        corrector: typing.Union['Corrector', schemas.Unset] = schemas.unset,
        filter: typing.Union[MetaOapg.properties.filter, None, str, schemas.Unset] = schemas.unset,
        database_studyset: typing.Union[MetaOapg.properties.database_studyset, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Specification':
        return super().__new__(
            cls,
            *_args,
            type=type,
            estimator=estimator,
            mask=mask,
            conditions=conditions,
            weights=weights,
            transformer=transformer,
            corrector=corrector,
            filter=filter,
            database_studyset=database_studyset,
            _configuration=_configuration,
            **kwargs,
        )

from neurosynth_compose_sdk.model.corrector import Corrector
from neurosynth_compose_sdk.model.estimator import Estimator
