import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.neurovault_file import NeurovaultFile


T = TypeVar("T", bound="NeurovaultCollectionReturn")


@attr.s(auto_attribs=True)
class NeurovaultCollectionReturn:
    """
    Attributes:
        collection_id (Union[Unset, str]):
        files (Union[Unset, List[Union['NeurovaultFile', str]]]):
        result (Union[Unset, str]):
        id (Union[Unset, str]): the identifier for the resource.
        updated_at (Union[Unset, None, datetime.datetime]): when the resource was last modified.
        created_at (Union[Unset, datetime.datetime]): When the resource was created.
        user (Union[Unset, None, str]): Who owns the resource.
    """

    collection_id: Union[Unset, str] = UNSET
    files: Union[Unset, List[Union["NeurovaultFile", str]]] = UNSET
    result: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, None, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.neurovault_file import NeurovaultFile

        collection_id = self.collection_id
        files: Union[Unset, List[Union[Dict[str, Any], str]]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item: Union[Dict[str, Any], str]

                if isinstance(files_item_data, NeurovaultFile):
                    files_item = files_item_data.to_dict()

                else:
                    files_item = files_item_data

                files.append(files_item)

        result = self.result
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
        if files is not UNSET:
            field_dict["files"] = files
        if result is not UNSET:
            field_dict["result"] = result
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
        from ..models.neurovault_file import NeurovaultFile

        d = src_dict.copy()
        collection_id = d.pop("collection_id", UNSET)

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:

            def _parse_files_item(data: object) -> Union["NeurovaultFile", str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    files_item_type_1 = NeurovaultFile.from_dict(data)

                    return files_item_type_1
                except:  # noqa: E722
                    pass
                return cast(Union["NeurovaultFile", str], data)

            files_item = _parse_files_item(files_item_data)

            files.append(files_item)

        result = d.pop("result", UNSET)

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

        neurovault_collection_return = cls(
            collection_id=collection_id,
            files=files,
            result=result,
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            user=user,
        )

        neurovault_collection_return.additional_properties = d
        return neurovault_collection_return

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
