# NeurostoreStudyReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neurostore_id** | **str** |  | [optional] [readonly] 
**analyses** | [**List[NeurostoreAnalysis]**](NeurostoreAnalysis.md) |  | [optional] 
**exception** | **str** |  | [optional] 
**traceback** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str** | Who owns the resource. | [optional] 
**username** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.neurostore_study_return import NeurostoreStudyReturn

# TODO update the JSON string below
json = "{}"
# create an instance of NeurostoreStudyReturn from a JSON string
neurostore_study_return_instance = NeurostoreStudyReturn.from_json(json)
# print the JSON string representation of the object
print NeurostoreStudyReturn.to_json()

# convert the object into a dict
neurostore_study_return_dict = neurostore_study_return_instance.to_dict()
# create an instance of NeurostoreStudyReturn from a dict
neurostore_study_return_form_dict = neurostore_study_return.from_dict(neurostore_study_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


