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


class MetaAnalysis(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The combination of the specification determining what meta-analysis to run (required), the studyset to act as input to the meta-analytic algorithm (required), and the annotation to provide human readable annotations as well as acts as an optional filter on which analyses to select within the studyset (optional, but suggested).
    """


    class MetaOapg:
        
        class properties:
            
            
            class specification(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.StrSchema
                    
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
                            Specification,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'specification':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class studyset(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.StrSchema
                    
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
                            Studyset,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'studyset':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class annotation(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class one_of_0(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'one_of_0':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                            )
                    
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
                            Annotation,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'annotation':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'description':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            internal_studyset_id = schemas.StrSchema
            internal_annotation_id = schemas.StrSchema
            
            
            class results(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class one_of_0(
                                schemas.StrBase,
                                schemas.NoneBase,
                                schemas.Schema,
                                schemas.NoneStrMixin
                            ):
                            
                            
                                def __new__(
                                    cls,
                                    *_args: typing.Union[None, str, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'one_of_0':
                                    return super().__new__(
                                        cls,
                                        *_args,
                                        _configuration=_configuration,
                                    )
                            
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
                                    ResultReturn,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'results':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class provenance(
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'provenance':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class project(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'project':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            run_key = schemas.StrSchema
            __annotations__ = {
                "specification": specification,
                "studyset": studyset,
                "annotation": annotation,
                "name": name,
                "description": description,
                "internal_studyset_id": internal_studyset_id,
                "internal_annotation_id": internal_annotation_id,
                "results": results,
                "provenance": provenance,
                "project": project,
                "run_key": run_key,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["specification"]) -> MetaOapg.properties.specification: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["studyset"]) -> MetaOapg.properties.studyset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annotation"]) -> MetaOapg.properties.annotation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internal_studyset_id"]) -> MetaOapg.properties.internal_studyset_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internal_annotation_id"]) -> MetaOapg.properties.internal_annotation_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["results"]) -> MetaOapg.properties.results: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provenance"]) -> MetaOapg.properties.provenance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project"]) -> MetaOapg.properties.project: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["run_key"]) -> MetaOapg.properties.run_key: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["specification", "studyset", "annotation", "name", "description", "internal_studyset_id", "internal_annotation_id", "results", "provenance", "project", "run_key", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["specification"]) -> typing.Union[MetaOapg.properties.specification, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["studyset"]) -> typing.Union[MetaOapg.properties.studyset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annotation"]) -> typing.Union[MetaOapg.properties.annotation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internal_studyset_id"]) -> typing.Union[MetaOapg.properties.internal_studyset_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internal_annotation_id"]) -> typing.Union[MetaOapg.properties.internal_annotation_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["results"]) -> typing.Union[MetaOapg.properties.results, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provenance"]) -> typing.Union[MetaOapg.properties.provenance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project"]) -> typing.Union[MetaOapg.properties.project, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["run_key"]) -> typing.Union[MetaOapg.properties.run_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["specification", "studyset", "annotation", "name", "description", "internal_studyset_id", "internal_annotation_id", "results", "provenance", "project", "run_key", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        specification: typing.Union[MetaOapg.properties.specification, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        studyset: typing.Union[MetaOapg.properties.studyset, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        annotation: typing.Union[MetaOapg.properties.annotation, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
        internal_studyset_id: typing.Union[MetaOapg.properties.internal_studyset_id, str, schemas.Unset] = schemas.unset,
        internal_annotation_id: typing.Union[MetaOapg.properties.internal_annotation_id, str, schemas.Unset] = schemas.unset,
        results: typing.Union[MetaOapg.properties.results, list, tuple, schemas.Unset] = schemas.unset,
        provenance: typing.Union[MetaOapg.properties.provenance, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        project: typing.Union[MetaOapg.properties.project, None, str, schemas.Unset] = schemas.unset,
        run_key: typing.Union[MetaOapg.properties.run_key, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MetaAnalysis':
        return super().__new__(
            cls,
            *_args,
            specification=specification,
            studyset=studyset,
            annotation=annotation,
            name=name,
            description=description,
            internal_studyset_id=internal_studyset_id,
            internal_annotation_id=internal_annotation_id,
            results=results,
            provenance=provenance,
            project=project,
            run_key=run_key,
            _configuration=_configuration,
            **kwargs,
        )

from neurosynth_compose_sdk.model.annotation import Annotation
from neurosynth_compose_sdk.model.result_return import ResultReturn
from neurosynth_compose_sdk.model.specification import Specification
from neurosynth_compose_sdk.model.studyset import Studyset
