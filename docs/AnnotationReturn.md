# AnnotationReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neurostore_id** | **str** | the id of the annotation on neurostore | [optional] 
**snapshot** | **object** | the snapshot taken of the annotation pending a successful run of the meta-analytic algorithm | [optional] 
**studyset** | **str** | The related cached studyset to this annotation. | [optional] [readonly] 
**neurostore_url** | **str** |  | [optional] [readonly] 
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str** | Who owns the resource. | [optional] 
**username** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.annotation_return import AnnotationReturn

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationReturn from a JSON string
annotation_return_instance = AnnotationReturn.from_json(json)
# print the JSON string representation of the object
print AnnotationReturn.to_json()

# convert the object into a dict
annotation_return_dict = annotation_return_instance.to_dict()
# create an instance of AnnotationReturn from a dict
annotation_return_form_dict = annotation_return.from_dict(annotation_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


