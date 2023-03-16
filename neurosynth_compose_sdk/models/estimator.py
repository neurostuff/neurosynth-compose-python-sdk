from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.estimator_args import EstimatorArgs


T = TypeVar("T", bound="Estimator")


@attr.s(auto_attribs=True)
class Estimator:
    """the specification for the function/class running the meta-analysis

    Attributes:
        type (Union[Unset, str]): the meta-analytic algorithm applied to the data. Currently this should be directly
            tied to the function/class running the meta-analysis. For example, ALE, or MKDADensity are valid NiMARE classes
            to put here. Example: MKDADensity.
        args (Union[Unset, EstimatorArgs]): arbitrary keyword arguments to be passed into the function/class to modify
            default functionality, this could modify the kernel, resampling methods, or any other behavior defined in the
            function/class (like MKDADensity).
    """

    type: Union[Unset, str] = UNSET
    args: Union[Unset, "EstimatorArgs"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        args: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if args is not UNSET:
            field_dict["args"] = args

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.estimator_args import EstimatorArgs

        d = src_dict.copy()
        type = d.pop("type", UNSET)

        _args = d.pop("args", UNSET)
        args: Union[Unset, EstimatorArgs]
        if isinstance(_args, Unset):
            args = UNSET
        else:
            args = EstimatorArgs.from_dict(_args)

        estimator = cls(
            type=type,
            args=args,
        )

        estimator.additional_properties = d
        return estimator

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
