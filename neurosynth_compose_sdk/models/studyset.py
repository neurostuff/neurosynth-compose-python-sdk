from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.studyset_snapshot import StudysetSnapshot


T = TypeVar("T", bound="Studyset")


@attr.s(auto_attribs=True)
class Studyset:
    """
    Attributes:
        neurostore_id (Union[Unset, str]): The id of the studyset on neurostore.
        snapshot (Union[Unset, None, StudysetSnapshot]): The snapshot of the studyset pending a successful run of the
            meta-analysis.
    """

    neurostore_id: Union[Unset, str] = UNSET
    snapshot: Union[Unset, None, "StudysetSnapshot"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        neurostore_id = self.neurostore_id
        snapshot: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.snapshot, Unset):
            snapshot = self.snapshot.to_dict() if self.snapshot else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if neurostore_id is not UNSET:
            field_dict["neurostore_id"] = neurostore_id
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.studyset_snapshot import StudysetSnapshot

        d = src_dict.copy()
        neurostore_id = d.pop("neurostore_id", UNSET)

        _snapshot = d.pop("snapshot", UNSET)
        snapshot: Union[Unset, None, StudysetSnapshot]
        if _snapshot is None:
            snapshot = None
        elif isinstance(_snapshot, Unset):
            snapshot = UNSET
        else:
            snapshot = StudysetSnapshot.from_dict(_snapshot)

        studyset = cls(
            neurostore_id=neurostore_id,
            snapshot=snapshot,
        )

        studyset.additional_properties = d
        return studyset

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
