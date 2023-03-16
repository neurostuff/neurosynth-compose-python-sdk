import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.corrector import Corrector
    from ..models.estimator import Estimator


T = TypeVar("T", bound="SpecificationReturn")


@attr.s(auto_attribs=True)
class SpecificationReturn:
    """The view of the specification through an endpoint.

    Attributes:
        type (Union[Unset, str]): the type of meta-analysis being run, typically either cbma or ibma, but others may
            become available in the future.
        estimator (Union[Unset, Estimator]): the specification for the function/class running the meta-analysis
        mask (Union[Unset, None, str]): a string representing a binary nifti file to select which voxels a user wants to
            include in the analysis.
        contrast (Union[Unset, None, str]): underspecified selection of columns to contrast (TODO, make better).
        transformer (Union[Unset, None, str]): A transformation applied to column(s) (e.g., binarize based on a
            threshold). This is likely to become deprecated.
        corrector (Union[Unset, None, Corrector]): The function/class applying statistical adjustments to the output of
            the meta-analysis (optional).
        filter_ (Union[Unset, None, str]): a boolean column from annotations selecting which analyses to include in the
            meta-analysis
        id (Union[Unset, str]): the identifier for the resource.
        updated_at (Union[Unset, None, datetime.datetime]): when the resource was last modified.
        created_at (Union[Unset, datetime.datetime]): When the resource was created.
        user (Union[Unset, None, str]): Who owns the resource.
    """

    type: Union[Unset, str] = UNSET
    estimator: Union[Unset, "Estimator"] = UNSET
    mask: Union[Unset, None, str] = UNSET
    contrast: Union[Unset, None, str] = UNSET
    transformer: Union[Unset, None, str] = UNSET
    corrector: Union[Unset, None, "Corrector"] = UNSET
    filter_: Union[Unset, None, str] = UNSET
    id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, None, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        estimator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.estimator, Unset):
            estimator = self.estimator.to_dict()

        mask = self.mask
        contrast = self.contrast
        transformer = self.transformer
        corrector: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.corrector, Unset):
            corrector = self.corrector.to_dict() if self.corrector else None

        filter_ = self.filter_
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
        if type is not UNSET:
            field_dict["type"] = type
        if estimator is not UNSET:
            field_dict["estimator"] = estimator
        if mask is not UNSET:
            field_dict["mask"] = mask
        if contrast is not UNSET:
            field_dict["contrast"] = contrast
        if transformer is not UNSET:
            field_dict["transformer"] = transformer
        if corrector is not UNSET:
            field_dict["corrector"] = corrector
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
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
        from ..models.corrector import Corrector
        from ..models.estimator import Estimator

        d = src_dict.copy()
        type = d.pop("type", UNSET)

        _estimator = d.pop("estimator", UNSET)
        estimator: Union[Unset, Estimator]
        if isinstance(_estimator, Unset):
            estimator = UNSET
        else:
            estimator = Estimator.from_dict(_estimator)

        mask = d.pop("mask", UNSET)

        contrast = d.pop("contrast", UNSET)

        transformer = d.pop("transformer", UNSET)

        _corrector = d.pop("corrector", UNSET)
        corrector: Union[Unset, None, Corrector]
        if _corrector is None:
            corrector = None
        elif isinstance(_corrector, Unset):
            corrector = UNSET
        else:
            corrector = Corrector.from_dict(_corrector)

        filter_ = d.pop("filter", UNSET)

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

        specification_return = cls(
            type=type,
            estimator=estimator,
            mask=mask,
            contrast=contrast,
            transformer=transformer,
            corrector=corrector,
            filter_=filter_,
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            user=user,
        )

        specification_return.additional_properties = d
        return specification_return

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
