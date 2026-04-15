# ResultInit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_analysis_id** | **str** |  | [optional] 
**cached_studyset** | **object** |  | [optional] 
**cached_annotation** | **object** |  | [optional] 
**cached_studyset_id** | **str** | ID of an existing cached studyset snapshot to link to this result. | [optional] 
**cached_annotation_id** | **str** | ID of an existing cached annotation snapshot to link to this result. | [optional] 
**cli_version** | **str** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.result_init import ResultInit

# TODO update the JSON string below
json = "{}"
# create an instance of ResultInit from a JSON string
result_init_instance = ResultInit.from_json(json)
# print the JSON string representation of the object
print(ResultInit.to_json())

# convert the object into a dict
result_init_dict = result_init_instance.to_dict()
# create an instance of ResultInit from a dict
result_init_from_dict = ResultInit.from_dict(result_init_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


