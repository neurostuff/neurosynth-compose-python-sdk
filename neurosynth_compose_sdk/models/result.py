from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.estimator import Estimator
    from ..models.neurovault_collection import NeurovaultCollection
    from ..models.result_images import ResultImages


T = TypeVar("T", bound="Result")


@attr.s(auto_attribs=True)
class Result:
    """describes the output of a meta-analysis

    Attributes:
        images (Union[Unset, ResultImages]):
        meta_analysis_id (Union[Unset, str]):
        cli_version (Union[Unset, None, str]):
        estimator (Union[Unset, Estimator]): the specification for the function/class running the meta-analysis
        neurostore_id (Union[Unset, None, str]):
        neurovault_collection (Union[Unset, NeurovaultCollection]):
    """

    images: Union[Unset, "ResultImages"] = UNSET
    meta_analysis_id: Union[Unset, str] = UNSET
    cli_version: Union[Unset, None, str] = UNSET
    estimator: Union[Unset, "Estimator"] = UNSET
    neurostore_id: Union[Unset, None, str] = UNSET
    neurovault_collection: Union[Unset, "NeurovaultCollection"] = UNSET
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

        result = cls(
            images=images,
            meta_analysis_id=meta_analysis_id,
            cli_version=cli_version,
            estimator=estimator,
            neurostore_id=neurostore_id,
            neurovault_collection=neurovault_collection,
        )

        result.additional_properties = d
        return result

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
