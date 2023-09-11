# NeurovaultFileReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | [optional] 
**exception** | **str** |  | [optional] 
**traceback** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**image_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str** | Who owns the resource. | [optional] 
**username** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.neurovault_file_return import NeurovaultFileReturn

# TODO update the JSON string below
json = "{}"
# create an instance of NeurovaultFileReturn from a JSON string
neurovault_file_return_instance = NeurovaultFileReturn.from_json(json)
# print the JSON string representation of the object
print NeurovaultFileReturn.to_json()

# convert the object into a dict
neurovault_file_return_dict = neurovault_file_return_instance.to_dict()
# create an instance of NeurovaultFileReturn from a dict
neurovault_file_return_form_dict = neurovault_file_return.from_dict(neurovault_file_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


