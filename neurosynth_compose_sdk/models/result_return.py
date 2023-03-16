import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.estimator import Estimator
    from ..models.neurovault_collection import NeurovaultCollection
    from ..models.result_images import ResultImages


T = TypeVar("T", bound="ResultReturn")


@attr.s(auto_attribs=True)
class ResultReturn:
    """
    Attributes:
        images (Union[Unset, ResultImages]):
        meta_analysis_id (Union[Unset, str]):
        cli_version (Union[Unset, None, str]):
        estimator (Union[Unset, Estimator]): the specification for the function/class running the meta-analysis
        neurostore_id (Union[Unset, None, str]):
        neurovault_collection (Union[Unset, NeurovaultCollection]):
        id (Union[Unset, str]): the identifier for the resource.
        updated_at (Union[Unset, None, datetime.datetime]): when the resource was last modified.
        created_at (Union[Unset, datetime.datetime]): When the resource was created.
        user (Union[Unset, None, str]): Who owns the resource.
    """

    images: Union[Unset, "ResultImages"] = UNSET
    meta_analysis_id: Union[Unset, str] = UNSET
    cli_version: Union[Unset, None, str] = UNSET
    estimator: Union[Unset, "Estimator"] = UNSET
    neurostore_id: Union[Unset, None, str] = UNSET
    neurovault_collection: Union[Unset, "NeurovaultCollection"] = UNSET
    id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, None, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        meta_analysis_id = self.meta_analysis_id
        cli_version = self.cli_version
        estimator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.estimator, Unset):
            estimator = self.estimator.to_dict()

        neurostore_id = self.neurostore_id
        neurovault_collection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.neurovault_collection, Unset):
            neurovault_collection = self.neurovault_collection.to_dict()

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
        if images is not UNSET:
            field_dict["images"] = images
        if meta_analysis_id is not UNSET:
            field_dict["meta_analysis_id"] = meta_analysis_id
        if cli_version is not UNSET:
            field_dict["cli_version"] = cli_version
        if estimator is not UNSET:
            field_dict["estimator"] = estimator
        if neurostore_id is not UNSET:
            field_dict["neurostore_id"] = neurostore_id
        if neurovault_collection is not UNSET:
            field_dict["neurovault_collection"] = neurovault_collection
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
        from ..models.estimator import Estimator
        from ..models.neurovault_collection import NeurovaultCollection
        from ..models.result_images import ResultImages

        d = src_dict.copy()
        _images = d.pop("images", UNSET)
        images: Union[Unset, ResultImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = ResultImages.from_dict(_images)

        meta_analysis_id = d.pop("meta_analysis_id", UNSET)

        cli_version = d.pop("cli_version", UNSET)

        _estimator = d.pop("estimator", UNSET)
        estimator: Union[Unset, Estimator]
        if isinstance(_estimator, Unset):
            estimator = UNSET
        else:
            estimator = Estimator.from_dict(_estimator)

        neurostore_id = d.pop("neurostore_id", UNSET)

        _neurovault_collection = d.pop("neurovault_collection", UNSET)
        neurovault_collection: Union[Unset, NeurovaultCollection]
        if isinstance(_neurovault_collection, Unset):
            neurovault_collection = UNSET
        else:
            neurovault_collection = NeurovaultCollection.from_dict(_neurovault_collection)

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

        result_return = cls(
            images=images,
            meta_analysis_id=meta_analysis_id,
            cli_version=cli_version,
            estimator=estimator,
            neurostore_id=neurostore_id,
            neurovault_collection=neurovault_collection,
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            user=user,
        )

        result_return.additional_properties = d
        return result_return

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
