# StudysetSnapshotSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Compose snapshot studyset identifier. | [optional] 
**md5** | **str** | Canonical md5 hash of the snapshot payload. | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.studyset_snapshot_summary import StudysetSnapshotSummary

# TODO update the JSON string below
json = "{}"
# create an instance of StudysetSnapshotSummary from a JSON string
studyset_snapshot_summary_instance = StudysetSnapshotSummary.from_json(json)
# print the JSON string representation of the object
print(StudysetSnapshotSummary.to_json())

# convert the object into a dict
studyset_snapshot_summary_dict = studyset_snapshot_summary_instance.to_dict()
# create an instance of StudysetSnapshotSummary from a dict
studyset_snapshot_summary_from_dict = StudysetSnapshotSummary.from_dict(studyset_snapshot_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


