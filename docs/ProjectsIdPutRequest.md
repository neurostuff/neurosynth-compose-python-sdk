# ProjectsIdPutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provenance** | **object** |  | [optional] 
**meta_analyses** | [**ProjectMetaAnalyses**](ProjectMetaAnalyses.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**public** | **bool** | whether the project is public or private | [optional] 
**neurostore_study** | [**NeurostoreStudy**](NeurostoreStudy.md) |  | [optional] 
**neurostore_url** | **str** |  | [optional] 
**create_neurostore_study** | **bool** |  | [optional] [default to True]

## Example

```python
from neurosynth_compose_sdk.models.projects_id_put_request import ProjectsIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsIdPutRequest from a JSON string
projects_id_put_request_instance = ProjectsIdPutRequest.from_json(json)
# print the JSON string representation of the object
print ProjectsIdPutRequest.to_json()

# convert the object into a dict
projects_id_put_request_dict = projects_id_put_request_instance.to_dict()
# create an instance of ProjectsIdPutRequest from a dict
projects_id_put_request_form_dict = projects_id_put_request.from_dict(projects_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


