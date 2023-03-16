from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meta_analysis import MetaAnalysis
    from ..models.project_provenance import ProjectProvenance


T = TypeVar("T", bound="Project")


@attr.s(auto_attribs=True)
class Project:
    """
    Attributes:
        provenance (Union[Unset, None, ProjectProvenance]):
        meta_analyses (Union[Unset, List[Union['MetaAnalysis', str]]]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
    """

    provenance: Union[Unset, None, "ProjectProvenance"] = UNSET
    meta_analyses: Union[Unset, List[Union["MetaAnalysis", str]]] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.meta_analysis import MetaAnalysis

        provenance: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.provenance, Unset):
            provenance = self.provenance.to_dict() if self.provenance else None

        meta_analyses: Union[Unset, List[Union[Dict[str, Any], str]]] = UNSET
        if not isinstance(self.meta_analyses, Unset):
            meta_analyses = []
            for meta_analyses_item_data in self.meta_analyses:
                meta_analyses_item: Union[Dict[str, Any], str]

                if isinstance(meta_analyses_item_data, MetaAnalysis):
                    meta_analyses_item = meta_analyses_item_data.to_dict()

                else:
                    meta_analyses_item = meta_analyses_item_data

                meta_analyses.append(meta_analyses_item)

        name = self.name
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provenance is not UNSET:
            field_dict["provenance"] = provenance
        if meta_analyses is not UNSET:
            field_dict["meta_analyses"] = meta_analyses
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.meta_analysis import MetaAnalysis
        from ..models.project_provenance import ProjectProvenance

        d = src_dict.copy()
        _provenance = d.pop("provenance", UNSET)
        provenance: Union[Unset, None, ProjectProvenance]
        if _provenance is None:
            provenance = None
        elif isinstance(_provenance, Unset):
            provenance = UNSET
        else:
            provenance = ProjectProvenance.from_dict(_provenance)

        meta_analyses = []
        _meta_analyses = d.pop("meta_analyses", UNSET)
        for meta_analyses_item_data in _meta_analyses or []:

            def _parse_meta_analyses_item(data: object) -> Union["MetaAnalysis", str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    meta_analyses_item_type_0 = MetaAnalysis.from_dict(data)

                    return meta_analyses_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["MetaAnalysis", str], data)

            meta_analyses_item = _parse_meta_analyses_item(meta_analyses_item_data)

            meta_analyses.append(meta_analyses_item)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        project = cls(
            provenance=provenance,
            meta_analyses=meta_analyses,
            name=name,
            description=description,
        )

        project.additional_properties = d
        return project

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
