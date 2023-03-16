from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.corrector_args import CorrectorArgs


T = TypeVar("T", bound="Corrector")


@attr.s(auto_attribs=True)
class Corrector:
    """The function/class applying statistical adjustments to the output of the meta-analysis (optional).

    Attributes:
        type (Union[Unset, str]): the name of the function/class performing the correction. For example FWECorrector
            from NiMARE would be valid. Example: FWECorrector.
        args (Union[Unset, CorrectorArgs]): key word arguments passed to the corrector to modidy default functionality,
            such as number of iterations, or the particular method of correction being applied.
    """

    type: Union[Unset, str] = UNSET
    args: Union[Unset, "CorrectorArgs"] = UNSET
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
        from ..models.corrector_args import CorrectorArgs

        d = src_dict.copy()
        type = d.pop("type", UNSET)

        _args = d.pop("args", UNSET)
        args: Union[Unset, CorrectorArgs]
        if isinstance(_args, Unset):
            args = UNSET
        else:
            args = CorrectorArgs.from_dict(_args)

        corrector = cls(
            type=type,
            args=args,
        )

        corrector.additional_properties = d
        return corrector

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
