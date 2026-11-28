# CurationStubList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CurationStubListResultsInner]**](CurationStubListResultsInner.md) |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.curation_stub_list import CurationStubList

# TODO update the JSON string below
json = "{}"
# create an instance of CurationStubList from a JSON string
curation_stub_list_instance = CurationStubList.from_json(json)
# print the JSON string representation of the object
print(CurationStubList.to_json())

# convert the object into a dict
curation_stub_list_dict = curation_stub_list_instance.to_dict()
# create an instance of CurationStubList from a dict
curation_stub_list_from_dict = CurationStubList.from_dict(curation_stub_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


