from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotation_snapshot import AnnotationSnapshot


T = TypeVar("T", bound="Annotation")


@attr.s(auto_attribs=True)
class Annotation:
    """a holder/reference to the annotation on neurostore

    Attributes:
        neurostore_id (Union[Unset, str]): the id of the annotation on neurostore
        snapshot (Union[Unset, None, AnnotationSnapshot]): the snapshot taken of the annotation pending a successful run
            of the meta-analytic algorithm
        studyset (Union[Unset, str]): The related studyset to this annotation.
    """

    neurostore_id: Union[Unset, str] = UNSET
    snapshot: Union[Unset, None, "AnnotationSnapshot"] = UNSET
    studyset: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        neurostore_id = self.neurostore_id
        snapshot: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.snapshot, Unset):
            snapshot = self.snapshot.to_dict() if self.snapshot else None

        studyset = self.studyset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if neurostore_id is not UNSET:
            field_dict["neurostore_id"] = neurostore_id
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot
        if studyset is not UNSET:
            field_dict["studyset"] = studyset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.annotation_snapshot import AnnotationSnapshot

        d = src_dict.copy()
        neurostore_id = d.pop("neurostore_id", UNSET)

        _snapshot = d.pop("snapshot", UNSET)
        snapshot: Union[Unset, None, AnnotationSnapshot]
        if _snapshot is None:
            snapshot = None
        elif isinstance(_snapshot, Unset):
            snapshot = UNSET
        else:
            snapshot = AnnotationSnapshot.from_dict(_snapshot)

        studyset = d.pop("studyset", UNSET)

        annotation = cls(
            neurostore_id=neurostore_id,
            snapshot=snapshot,
            studyset=studyset,
        )

        annotation.additional_properties = d
        return annotation

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
