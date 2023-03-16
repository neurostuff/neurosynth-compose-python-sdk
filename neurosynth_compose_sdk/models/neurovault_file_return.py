import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NeurovaultFileReturn")


@attr.s(auto_attribs=True)
class NeurovaultFileReturn:
    """
    Attributes:
        collection_id (Union[Unset, str]):
        exception (Union[Unset, None, str]):
        traceback (Union[Unset, None, str]):
        status (Union[Unset, str]):
        file (Union[Unset, str]):
        image_id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        map_type (Union[Unset, None, str]):
        cognitive_contrast_cogatlas (Union[Unset, None, str]):
        cognitive_contrast_cogatlas_id (Union[Unset, None, str]):
        cognitive_paradigm_cogatlas (Union[Unset, None, str]):
        cognitive_paradigm_cogatlas_id (Union[Unset, None, str]):
        id (Union[Unset, str]): the identifier for the resource.
        updated_at (Union[Unset, None, datetime.datetime]): when the resource was last modified.
        created_at (Union[Unset, datetime.datetime]): When the resource was created.
        user (Union[Unset, None, str]): Who owns the resource.
    """

    collection_id: Union[Unset, str] = UNSET
    exception: Union[Unset, None, str] = UNSET
    traceback: Union[Unset, None, str] = UNSET
    status: Union[Unset, str] = UNSET
    file: Union[Unset, str] = UNSET
    image_id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    map_type: Union[Unset, None, str] = UNSET
    cognitive_contrast_cogatlas: Union[Unset, None, str] = UNSET
    cognitive_contrast_cogatlas_id: Union[Unset, None, str] = UNSET
    cognitive_paradigm_cogatlas: Union[Unset, None, str] = UNSET
    cognitive_paradigm_cogatlas_id: Union[Unset, None, str] = UNSET
    id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, None, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        collection_id = self.collection_id
        exception = self.exception
        traceback = self.traceback
        status = self.status
        file = self.file
        image_id = self.image_id
        name = self.name
        map_type = self.map_type
        cognitive_contrast_cogatlas = self.cognitive_contrast_cogatlas
        cognitive_contrast_cogatlas_id = self.cognitive_contrast_cogatlas_id
        cognitive_paradigm_cogatlas = self.cognitive_paradigm_cogatlas
        cognitive_paradigm_cogatlas_id = self.cognitive_paradigm_cogatlas_id
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
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if exception is not UNSET:
            field_dict["exception"] = exception
        if traceback is not UNSET:
            field_dict["traceback"] = traceback
        if status is not UNSET:
            field_dict["status"] = status
        if file is not UNSET:
            field_dict["file"] = file
        if image_id is not UNSET:
            field_dict["image_id"] = image_id
        if name is not UNSET:
            field_dict["name"] = name
        if map_type is not UNSET:
            field_dict["map_type"] = map_type
        if cognitive_contrast_cogatlas is not UNSET:
            field_dict["cognitive_contrast_cogatlas"] = cognitive_contrast_cogatlas
        if cognitive_contrast_cogatlas_id is not UNSET:
            field_dict["cognitive_contrast_cogatlas_id"] = cognitive_contrast_cogatlas_id
        if cognitive_paradigm_cogatlas is not UNSET:
            field_dict["cognitive_paradigm_cogatlas"] = cognitive_paradigm_cogatlas
        if cognitive_paradigm_cogatlas_id is not UNSET:
            field_dict["cognitive_paradigm_cogatlas_id"] = cognitive_paradigm_cogatlas_id
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
        d = src_dict.copy()
        collection_id = d.pop("collection_id", UNSET)

        exception = d.pop("exception", UNSET)

        traceback = d.pop("traceback", UNSET)

        status = d.pop("status", UNSET)

        file = d.pop("file", UNSET)

        image_id = d.pop("image_id", UNSET)

        name = d.pop("name", UNSET)

        map_type = d.pop("map_type", UNSET)

        cognitive_contrast_cogatlas = d.pop("cognitive_contrast_cogatlas", UNSET)

        cognitive_contrast_cogatlas_id = d.pop("cognitive_contrast_cogatlas_id", UNSET)

        cognitive_paradigm_cogatlas = d.pop("cognitive_paradigm_cogatlas", UNSET)

        cognitive_paradigm_cogatlas_id = d.pop("cognitive_paradigm_cogatlas_id", UNSET)

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

        neurovault_file_return = cls(
            collection_id=collection_id,
            exception=exception,
            traceback=traceback,
            status=status,
            file=file,
            image_id=image_id,
            name=name,
            map_type=map_type,
            cognitive_contrast_cogatlas=cognitive_contrast_cogatlas,
            cognitive_contrast_cogatlas_id=cognitive_contrast_cogatlas_id,
            cognitive_paradigm_cogatlas=cognitive_paradigm_cogatlas,
            cognitive_paradigm_cogatlas_id=cognitive_paradigm_cogatlas_id,
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            user=user,
        )

        neurovault_file_return.additional_properties = d
        return neurovault_file_return

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
