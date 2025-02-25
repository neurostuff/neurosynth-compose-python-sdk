# StudysetReferenceSnapshotsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neurostore_id** | **str** | The id of the studyset on neurostore. | [optional] 
**snapshot** | **object** | The snapshot of the studyset pending a successful run of the meta-analysis. | [optional] 
**neurostore_url** | **str** |  | [optional] [readonly] 
**version** | **str** | A string representing a labeled version of this particular studyset. | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.studyset_reference_snapshots_inner import StudysetReferenceSnapshotsInner

# TODO update the JSON string below
json = "{}"
# create an instance of StudysetReferenceSnapshotsInner from a JSON string
studyset_reference_snapshots_inner_instance = StudysetReferenceSnapshotsInner.from_json(json)
# print the JSON string representation of the object
print(StudysetReferenceSnapshotsInner.to_json())

# convert the object into a dict
studyset_reference_snapshots_inner_dict = studyset_reference_snapshots_inner_instance.to_dict()
# create an instance of StudysetReferenceSnapshotsInner from a dict
studyset_reference_snapshots_inner_from_dict = StudysetReferenceSnapshotsInner.from_dict(studyset_reference_snapshots_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


