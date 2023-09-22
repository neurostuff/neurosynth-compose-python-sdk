# StudysetReferenceReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**List[StudysetReferenceSnapshotsInner]**](StudysetReferenceSnapshotsInner.md) |  | [optional] 
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str** | Who owns the resource. | [optional] 
**username** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.studyset_reference_return import StudysetReferenceReturn

# TODO update the JSON string below
json = "{}"
# create an instance of StudysetReferenceReturn from a JSON string
studyset_reference_return_instance = StudysetReferenceReturn.from_json(json)
# print the JSON string representation of the object
print StudysetReferenceReturn.to_json()

# convert the object into a dict
studyset_reference_return_dict = studyset_reference_return_instance.to_dict()
# create an instance of StudysetReferenceReturn from a dict
studyset_reference_return_form_dict = studyset_reference_return.from_dict(studyset_reference_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


