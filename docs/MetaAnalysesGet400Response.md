# MetaAnalysesGet400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.meta_analyses_get400_response import MetaAnalysesGet400Response

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysesGet400Response from a JSON string
meta_analyses_get400_response_instance = MetaAnalysesGet400Response.from_json(json)
# print the JSON string representation of the object
print(MetaAnalysesGet400Response.to_json())

# convert the object into a dict
meta_analyses_get400_response_dict = meta_analyses_get400_response_instance.to_dict()
# create an instance of MetaAnalysesGet400Response from a dict
meta_analyses_get400_response_from_dict = MetaAnalysesGet400Response.from_dict(meta_analyses_get400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


