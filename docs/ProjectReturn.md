# ProjectReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str** | Who owns the resource. | [optional] 
**username** | **str** |  | [optional] [readonly] 
**provenance** | **object** |  | [optional] 
**meta_analyses** | [**ProjectMetaAnalyses**](ProjectMetaAnalyses.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**public** | **bool** | whether the project is public or private | [optional] 
**neurostore_study** | [**NeurostoreStudy**](NeurostoreStudy.md) |  | [optional] 
**neurostore_url** | **str** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.project_return import ProjectReturn

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectReturn from a JSON string
project_return_instance = ProjectReturn.from_json(json)
# print the JSON string representation of the object
print ProjectReturn.to_json()

# convert the object into a dict
project_return_dict = project_return_instance.to_dict()
# create an instance of ProjectReturn from a dict
project_return_form_dict = project_return.from_dict(project_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


