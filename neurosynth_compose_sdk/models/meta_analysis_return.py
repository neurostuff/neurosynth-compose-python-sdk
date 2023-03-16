import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotation import Annotation
    from ..models.meta_analysis_provenance import MetaAnalysisProvenance
    from ..models.result_return import ResultReturn
    from ..models.specification import Specification
    from ..models.studyset import Studyset


T = TypeVar("T", bound="MetaAnalysisReturn")


@attr.s(auto_attribs=True)
class MetaAnalysisReturn:
    """
    Attributes:
        specification (Union['Specification', Unset, str]):
        studyset (Union['Studyset', Unset, str]):
        annotation (Union['Annotation', Unset, str]):
        name (Union[Unset, None, str]): Human-readable name of the meta-analysis.
        description (Union[Unset, None, str]): Long form description of the meta-analysis.
        internal_studyset_id (Union[Unset, str]): The id of the studyset on neurosynth-compose (as opposed to the id of
            the studyset on neurostore). Multiple snapshots of the studyset can be stored on neurosynth-compose so knowing
            which snapshot is being referenced is necessary.
        internal_annotation_id (Union[Unset, str]): The id of the annotation on neurosynth-compose (as opposed to the id
            of the annotation on neurostore). Multiple snapshots of the annotation can be stored on neurosynth-compose so
            knowing which snapshot is being referenced is necessary.
        results (Union[Unset, List[Union['ResultReturn', str]]]): array of neurostore ids representing the results of
            this meta-analysis (nominally all results should be the same, but machine architecture differences/algorithm
            stochastic-ness may lead to slightly different outcomes for each result.
        provenance (Union[Unset, None, MetaAnalysisProvenance]):
        project (Union[Unset, None, str]):
        id (Union[Unset, str]): the identifier for the resource.
        updated_at (Union[Unset, None, datetime.datetime]): when the resource was last modified.
        created_at (Union[Unset, datetime.datetime]): When the resource was created.
        user (Union[Unset, None, str]): Who owns the resource.
    """

    specification: Union["Specification", Unset, str] = UNSET
    studyset: Union["Studyset", Unset, str] = UNSET
    annotation: Union["Annotation", Unset, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    internal_studyset_id: Union[Unset, str] = UNSET
    internal_annotation_id: Union[Unset, str] = UNSET
    results: Union[Unset, List[Union["ResultReturn", str]]] = UNSET
    provenance: Union[Unset, None, "MetaAnalysisProvenance"] = UNSET
    project: Union[Unset, None, str] = UNSET
    id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, None, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.annotation import Annotation
        from ..models.result_return import ResultReturn
        from ..models.specification import Specification
        from ..models.studyset import Studyset

        specification: Union[Dict[str, Any], Unset, str]
        if isinstance(self.specification, Unset):
            specification = UNSET

        elif isinstance(self.specification, Specification):
            specification = UNSET
            if not isinstance(self.specification, Unset):
                specification = self.specification.to_dict()

        else:
            specification = self.specification

        studyset: Union[Dict[str, Any], Unset, str]
        if isinstance(self.studyset, Unset):
            studyset = UNSET

        elif isinstance(self.studyset, Studyset):
            studyset = UNSET
            if not isinstance(self.studyset, Unset):
                studyset = self.studyset.to_dict()

        else:
            studyset = self.studyset

        annotation: Union[Dict[str, Any], Unset, str]
        if isinstance(self.annotation, Unset):
            annotation = UNSET

        elif isinstance(self.annotation, Annotation):
            annotation = UNSET
            if not isinstance(self.annotation, Unset):
                annotation = self.annotation.to_dict()

        else:
            annotation = self.annotation

        name = self.name
        description = self.description
        internal_studyset_id = self.internal_studyset_id
        internal_annotation_id = self.internal_annotation_id
        results: Union[Unset, List[Union[Dict[str, Any], str]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item: Union[Dict[str, Any], str]

                if isinstance(results_item_data, ResultReturn):
                    results_item = results_item_data.to_dict()

                else:
                    results_item = results_item_data

                results.append(results_item)

        provenance: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.provenance, Unset):
            provenance = self.provenance.to_dict() if self.provenance else None

        project = self.project
        id = self.id
        updated_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat() if self.updated_at else None

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if specification is not UNSET:
            field_dict["specification"] = specification
        if studyset is not UNSET:
            field_dict["studyset"] = studyset
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if internal_studyset_id is not UNSET:
            field_dict["internal_studyset_id"] = internal_studyset_id
        if internal_annotation_id is not UNSET:
            field_dict["internal_annotation_id"] = internal_annotation_id
        if results is not UNSET:
            field_dict["results"] = results
        if provenance is not UNSET:
            field_dict["provenance"] = provenance
        if project is not UNSET:
            field_dict["project"] = project
        if id is not UNSET:
            field_dict["id"] = id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.annotation import Annotation
        from ..models.meta_analysis_provenance import MetaAnalysisProvenance
        from ..models.result_return import ResultReturn
        from ..models.specification import Specification
        from ..models.studyset import Studyset

        d = src_dict.copy()

        def _parse_specification(data: object) -> Union["Specification", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _specification_type_1 = data
                specification_type_1: Union[Unset, Specification]
                if isinstance(_specification_type_1, Unset):
                    specification_type_1 = UNSET
                else:
                    specification_type_1 = Specification.from_dict(_specification_type_1)

                return specification_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Specification", Unset, str], data)

        specification = _parse_specification(d.pop("specification", UNSET))

        def _parse_studyset(data: object) -> Union["Studyset", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _studyset_type_1 = data
                studyset_type_1: Union[Unset, Studyset]
                if isinstance(_studyset_type_1, Unset):
                    studyset_type_1 = UNSET
                else:
                    studyset_type_1 = Studyset.from_dict(_studyset_type_1)

                return studyset_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Studyset", Unset, str], data)

        studyset = _parse_studyset(d.pop("studyset", UNSET))

        def _parse_annotation(data: object) -> Union["Annotation", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _annotation_type_1 = data
                annotation_type_1: Union[Unset, Annotation]
                if isinstance(_annotation_type_1, Unset):
                    annotation_type_1 = UNSET
                else:
                    annotation_type_1 = Annotation.from_dict(_annotation_type_1)

                return annotation_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Annotation", Unset, str], data)

        annotation = _parse_annotation(d.pop("annotation", UNSET))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        internal_studyset_id = d.pop("internal_studyset_id", UNSET)

        internal_annotation_id = d.pop("internal_annotation_id", UNSET)

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:

            def _parse_results_item(data: object) -> Union["ResultReturn", str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    results_item_type_1 = ResultReturn.from_dict(data)

                    return results_item_type_1
                except:  # noqa: E722
                    pass
                return cast(Union["ResultReturn", str], data)

            results_item = _parse_results_item(results_item_data)

            results.append(results_item)

        _provenance = d.pop("provenance", UNSET)
        provenance: Union[Unset, None, MetaAnalysisProvenance]
        if _provenance is None:
            provenance = None
        elif isinstance(_provenance, Unset):
            provenance = UNSET
        else:
            provenance = MetaAnalysisProvenance.from_dict(_provenance)

        project = d.pop("project", UNSET)

        id = d.pop("id", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, None, datetime.datetime]
        if _updated_at is None:
            updated_at = None
        elif isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        user = d.pop("user", UNSET)

        meta_analysis_return = cls(
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
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            user=user,
        )

        meta_analysis_return.additional_properties = d
        return meta_analysis_return

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
