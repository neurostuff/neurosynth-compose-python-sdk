import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotation_snapshot import AnnotationSnapshot


T = TypeVar("T", bound="AnnotationReturn")


@attr.s(auto_attribs=True)
class AnnotationReturn:
    """
    Attributes:
        neurostore_id (Union[Unset, str]): the id of the annotation on neurostore
        snapshot (Union[Unset, None, AnnotationSnapshot]): the snapshot taken of the annotation pending a successful run
            of the meta-analytic algorithm
        studyset (Union[Unset, str]): The related studyset to this annotation.
        id (Union[Unset, str]): the identifier for the resource.
        updated_at (Union[Unset, None, datetime.datetime]): when the resource was last modified.
        created_at (Union[Unset, datetime.datetime]): When the resource was created.
        user (Union[Unset, None, str]): Who owns the resource.
    """

    neurostore_id: Union[Unset, str] = UNSET
    snapshot: Union[Unset, None, "AnnotationSnapshot"] = UNSET
    studyset: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, None, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        neurostore_id = self.neurostore_id
        snapshot: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.snapshot, Unset):
            snapshot = self.snapshot.to_dict() if self.snapshot else None

        studyset = self.studyset
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
        if neurostore_id is not UNSET:
            field_dict["neurostore_id"] = neurostore_id
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot
        if studyset is not UNSET:
            field_dict["studyset"] = studyset
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

        annotation_return = cls(
            neurostore_id=neurostore_id,
            snapshot=snapshot,
            studyset=studyset,
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            user=user,
        )

        annotation_return.additional_properties = d
        return annotation_return

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
