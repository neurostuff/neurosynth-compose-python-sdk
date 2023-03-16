from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NeurovaultFile")


@attr.s(auto_attribs=True)
class NeurovaultFile:
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

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        collection_id = (
            self.collection_id
            if isinstance(self.collection_id, Unset)
            else (None, str(self.collection_id).encode(), "text/plain")
        )
        exception = (
            self.exception if isinstance(self.exception, Unset) else (None, str(self.exception).encode(), "text/plain")
        )
        traceback = (
            self.traceback if isinstance(self.traceback, Unset) else (None, str(self.traceback).encode(), "text/plain")
        )
        status = self.status if isinstance(self.status, Unset) else (None, str(self.status).encode(), "text/plain")
        file = self.file if isinstance(self.file, Unset) else (None, str(self.file).encode(), "text/plain")
        image_id = (
            self.image_id if isinstance(self.image_id, Unset) else (None, str(self.image_id).encode(), "text/plain")
        )
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        map_type = (
            self.map_type if isinstance(self.map_type, Unset) else (None, str(self.map_type).encode(), "text/plain")
        )
        cognitive_contrast_cogatlas = (
            self.cognitive_contrast_cogatlas
            if isinstance(self.cognitive_contrast_cogatlas, Unset)
            else (None, str(self.cognitive_contrast_cogatlas).encode(), "text/plain")
        )
        cognitive_contrast_cogatlas_id = (
            self.cognitive_contrast_cogatlas_id
            if isinstance(self.cognitive_contrast_cogatlas_id, Unset)
            else (None, str(self.cognitive_contrast_cogatlas_id).encode(), "text/plain")
        )
        cognitive_paradigm_cogatlas = (
            self.cognitive_paradigm_cogatlas
            if isinstance(self.cognitive_paradigm_cogatlas, Unset)
            else (None, str(self.cognitive_paradigm_cogatlas).encode(), "text/plain")
        )
        cognitive_paradigm_cogatlas_id = (
            self.cognitive_paradigm_cogatlas_id
            if isinstance(self.cognitive_paradigm_cogatlas_id, Unset)
            else (None, str(self.cognitive_paradigm_cogatlas_id).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
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

        neurovault_file = cls(
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
        )

        neurovault_file.additional_properties = d
        return neurovault_file

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
