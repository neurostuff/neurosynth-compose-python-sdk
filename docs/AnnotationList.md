# AnnotationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AnnotationReturn]**](AnnotationReturn.md) |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.annotation_list import AnnotationList

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationList from a JSON string
annotation_list_instance = AnnotationList.from_json(json)
# print the JSON string representation of the object
print(AnnotationList.to_json())

# convert the object into a dict
annotation_list_dict = annotation_list_instance.to_dict()
# create an instance of AnnotationList from a dict
annotation_list_from_dict = AnnotationList.from_dict(annotation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


