# Annotation

a holder/reference to the annotation on neurostore

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neurostore_id** | **str** | the id of the annotation on neurostore | [optional] 
**snapshot** | **object** | the snapshot taken of the annotation pending a successful run of the meta-analytic algorithm | [optional] 
**studyset** | **str** | The related cached studyset to this annotation. | [optional] [readonly] 
**neurostore_url** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.annotation import Annotation

# TODO update the JSON string below
json = "{}"
# create an instance of Annotation from a JSON string
annotation_instance = Annotation.from_json(json)
# print the JSON string representation of the object
print Annotation.to_json()

# convert the object into a dict
annotation_dict = annotation_instance.to_dict()
# create an instance of Annotation from a dict
annotation_form_dict = annotation.from_dict(annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


