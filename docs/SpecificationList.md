# SpecificationList

The representation of a list of specifications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[SpecificationReturn]**](SpecificationReturn.md) |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.specification_list import SpecificationList

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificationList from a JSON string
specification_list_instance = SpecificationList.from_json(json)
# print the JSON string representation of the object
print(SpecificationList.to_json())

# convert the object into a dict
specification_list_dict = specification_list_instance.to_dict()
# create an instance of SpecificationList from a dict
specification_list_from_dict = SpecificationList.from_dict(specification_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


