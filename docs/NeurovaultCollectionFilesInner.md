# NeurovaultCollectionFilesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | [optional] 
**exception** | **str** |  | [optional] 
**traceback** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**file** | **bytearray** |  | [optional] 
**image_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**map_type** | **str** |  | [optional] 
**cognitive_contrast_cogatlas** | **str** |  | [optional] 
**cognitive_contrast_cogatlas_id** | **str** |  | [optional] 
**cognitive_paradigm_cogatlas** | **str** |  | [optional] 
**cognitive_paradigm_cogatlas_id** | **str** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.neurovault_collection_files_inner import NeurovaultCollectionFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of NeurovaultCollectionFilesInner from a JSON string
neurovault_collection_files_inner_instance = NeurovaultCollectionFilesInner.from_json(json)
# print the JSON string representation of the object
print NeurovaultCollectionFilesInner.to_json()

# convert the object into a dict
neurovault_collection_files_inner_dict = neurovault_collection_files_inner_instance.to_dict()
# create an instance of NeurovaultCollectionFilesInner from a dict
neurovault_collection_files_inner_form_dict = neurovault_collection_files_inner.from_dict(neurovault_collection_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


