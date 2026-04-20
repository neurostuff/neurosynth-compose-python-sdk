# AnnotationSnapshotSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Compose snapshot annotation identifier. | [optional] 
**md5** | **str** | Canonical md5 hash of the snapshot payload. | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.annotation_snapshot_summary import AnnotationSnapshotSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationSnapshotSummary from a JSON string
annotation_snapshot_summary_instance = AnnotationSnapshotSummary.from_json(json)
# print the JSON string representation of the object
print(AnnotationSnapshotSummary.to_json())

# convert the object into a dict
annotation_snapshot_summary_dict = annotation_snapshot_summary_instance.to_dict()
# create an instance of AnnotationSnapshotSummary from a dict
annotation_snapshot_summary_from_dict = AnnotationSnapshotSummary.from_dict(annotation_snapshot_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


