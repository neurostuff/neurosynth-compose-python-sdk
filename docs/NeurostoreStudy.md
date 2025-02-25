# NeurostoreStudy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neurostore_id** | **str** |  | [optional] [readonly] 
**analyses** | [**List[NeurostoreAnalysis]**](NeurostoreAnalysis.md) |  | [optional] 
**exception** | **str** |  | [optional] 
**traceback** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.neurostore_study import NeurostoreStudy

# TODO update the JSON string below
json = "{}"
# create an instance of NeurostoreStudy from a JSON string
neurostore_study_instance = NeurostoreStudy.from_json(json)
# print the JSON string representation of the object
print(NeurostoreStudy.to_json())

# convert the object into a dict
neurostore_study_dict = neurostore_study_instance.to_dict()
# create an instance of NeurostoreStudy from a dict
neurostore_study_from_dict = NeurostoreStudy.from_dict(neurostore_study_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


