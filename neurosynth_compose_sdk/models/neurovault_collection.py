from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.neurovault_file import NeurovaultFile


T = TypeVar("T", bound="NeurovaultCollection")


@attr.s(auto_attribs=True)
class NeurovaultCollection:
    """
    Attributes:
        collection_id (Union[Unset, str]):
        files (Union[Unset, List[Union['NeurovaultFile', str]]]):
        result (Union[Unset, str]):
    """

    collection_id: Union[Unset, str] = UNSET
    files: Union[Unset, List[Union["NeurovaultFile", str]]] = UNSET
    result: Union[Unset, str] = UNSET
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if files is not UNSET:
            field_dict["files"] = files
        if result is not UNSET:
            field_dict["result"] = result

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

        neurovault_collection = cls(
            collection_id=collection_id,
            files=files,
            result=result,
        )

        neurovault_collection.additional_properties = d
        return neurovault_collection

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
