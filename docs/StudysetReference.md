# StudysetReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**List[StudysetReferenceSnapshotsInner]**](StudysetReferenceSnapshotsInner.md) |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.studyset_reference import StudysetReference

# TODO update the JSON string below
json = "{}"
# create an instance of StudysetReference from a JSON string
studyset_reference_instance = StudysetReference.from_json(json)
# print the JSON string representation of the object
print StudysetReference.to_json()

# convert the object into a dict
studyset_reference_dict = studyset_reference_instance.to_dict()
# create an instance of StudysetReference from a dict
studyset_reference_form_dict = studyset_reference.from_dict(studyset_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


