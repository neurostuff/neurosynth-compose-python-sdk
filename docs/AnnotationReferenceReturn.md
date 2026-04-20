# AnnotationReferenceReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**List[AnnotationSnapshotSummary]**](AnnotationSnapshotSummary.md) |  | [optional] 
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str** | Who owns the resource. | [optional] 
**username** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.annotation_reference_return import AnnotationReferenceReturn

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationReferenceReturn from a JSON string
annotation_reference_return_instance = AnnotationReferenceReturn.from_json(json)
# print the JSON string representation of the object
print(AnnotationReferenceReturn.to_json())

# convert the object into a dict
annotation_reference_return_dict = annotation_reference_return_instance.to_dict()
# create an instance of AnnotationReferenceReturn from a dict
annotation_reference_return_from_dict = AnnotationReferenceReturn.from_dict(annotation_reference_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


