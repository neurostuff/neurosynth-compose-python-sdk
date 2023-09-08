# UserReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** |  | [optional] 
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str** | Who owns the resource. | [optional] 
**username** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.user_return import UserReturn

# TODO update the JSON string below
json = "{}"
# create an instance of UserReturn from a JSON string
user_return_instance = UserReturn.from_json(json)
# print the JSON string representation of the object
print UserReturn.to_json()

# convert the object into a dict
user_return_dict = user_return_instance.to_dict()
# create an instance of UserReturn from a dict
user_return_form_dict = user_return.from_dict(user_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


