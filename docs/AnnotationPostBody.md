# AnnotationPostBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cached_studyset_id** | **str** |  | 
**neurostore_id** | **str** | the id of the annotation on neurostore | [optional] 
**snapshot** | **object** | the snapshot taken of the annotation pending a successful run of the meta-analytic algorithm | [optional] 
**studyset** | **str** | The related cached studyset to this annotation. | [optional] [readonly] 
**neurostore_url** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.annotation_post_body import AnnotationPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationPostBody from a JSON string
annotation_post_body_instance = AnnotationPostBody.from_json(json)
# print the JSON string representation of the object
print AnnotationPostBody.to_json()

# convert the object into a dict
annotation_post_body_dict = annotation_post_body_instance.to_dict()
# create an instance of AnnotationPostBody from a dict
annotation_post_body_form_dict = annotation_post_body.from_dict(annotation_post_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


