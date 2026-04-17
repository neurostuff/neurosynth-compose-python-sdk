# AnnotationReference

A lightweight reference keyed by the Neurostore annotation ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**List[AnnotationSnapshotSummary]**](AnnotationSnapshotSummary.md) |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.annotation_reference import AnnotationReference

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationReference from a JSON string
annotation_reference_instance = AnnotationReference.from_json(json)
# print the JSON string representation of the object
print(AnnotationReference.to_json())

# convert the object into a dict
annotation_reference_dict = annotation_reference_instance.to_dict()
# create an instance of AnnotationReference from a dict
annotation_reference_from_dict = AnnotationReference.from_dict(annotation_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


