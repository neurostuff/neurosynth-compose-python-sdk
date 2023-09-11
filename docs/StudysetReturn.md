# StudysetReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neurostore_id** | **str** | The id of the studyset on neurostore. | [optional] 
**snapshot** | **object** | The snapshot of the studyset pending a successful run of the meta-analysis. | [optional] 
**neurostore_url** | **str** |  | [optional] [readonly] 
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str** | Who owns the resource. | [optional] 
**username** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.studyset_return import StudysetReturn

# TODO update the JSON string below
json = "{}"
# create an instance of StudysetReturn from a JSON string
studyset_return_instance = StudysetReturn.from_json(json)
# print the JSON string representation of the object
print StudysetReturn.to_json()

# convert the object into a dict
studyset_return_dict = studyset_return_instance.to_dict()
# create an instance of StudysetReturn from a dict
studyset_return_form_dict = studyset_return.from_dict(studyset_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


