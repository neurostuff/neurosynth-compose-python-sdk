# CurationStubListResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_id** | **str** |  | [optional] 
**stub** | [**CurationStub**](CurationStub.md) | null for the few stored stubs that are not objects | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.curation_stub_list_results_inner import CurationStubListResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CurationStubListResultsInner from a JSON string
curation_stub_list_results_inner_instance = CurationStubListResultsInner.from_json(json)
# print the JSON string representation of the object
print(CurationStubListResultsInner.to_json())

# convert the object into a dict
curation_stub_list_results_inner_dict = curation_stub_list_results_inner_instance.to_dict()
# create an instance of CurationStubListResultsInner from a dict
curation_stub_list_results_inner_from_dict = CurationStubListResultsInner.from_dict(curation_stub_list_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


