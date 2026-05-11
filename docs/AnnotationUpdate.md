# AnnotationUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neurostore_id** | **str** | the id of the annotation on neurostore | [optional] 
**snapshot** | **object** | the snapshot taken of the annotation pending a successful run of the meta-analytic algorithm | [optional] 
**studyset** | **str** | The related cached studyset to this annotation. | [optional] [readonly] 
**neurostore_url** | **str** |  | [optional] [readonly] 
**cached_studyset_id** | **str** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.annotation_update import AnnotationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationUpdate from a JSON string
annotation_update_instance = AnnotationUpdate.from_json(json)
# print the JSON string representation of the object
print(AnnotationUpdate.to_json())

# convert the object into a dict
annotation_update_dict = annotation_update_instance.to_dict()
# create an instance of AnnotationUpdate from a dict
annotation_update_from_dict = AnnotationUpdate.from_dict(annotation_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


