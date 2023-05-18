# NeurovaultFileList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[NeurovaultFileReturn]**](NeurovaultFileReturn.md) |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.neurovault_file_list import NeurovaultFileList

# TODO update the JSON string below
json = "{}"
# create an instance of NeurovaultFileList from a JSON string
neurovault_file_list_instance = NeurovaultFileList.from_json(json)
# print the JSON string representation of the object
print NeurovaultFileList.to_json()

# convert the object into a dict
neurovault_file_list_dict = neurovault_file_list_instance.to_dict()
# create an instance of NeurovaultFileList from a dict
neurovault_file_list_form_dict = neurovault_file_list.from_dict(neurovault_file_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


