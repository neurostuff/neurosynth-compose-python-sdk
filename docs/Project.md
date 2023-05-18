# Project


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provenance** | **object** |  | [optional] 
**meta_analyses** | [**ProjectMetaAnalyses**](ProjectMetaAnalyses.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**public** | **bool** | whether the project is public or private | [optional] 
**neurostore_id** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print Project.to_json()

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_form_dict = project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


