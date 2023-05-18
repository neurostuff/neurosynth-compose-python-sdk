# NeurostoreAnalysis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neurostore_id** | **str** |  | [optional] [readonly] 
**exception** | **str** |  | [optional] 
**traceback** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.neurostore_analysis import NeurostoreAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of NeurostoreAnalysis from a JSON string
neurostore_analysis_instance = NeurostoreAnalysis.from_json(json)
# print the JSON string representation of the object
print NeurostoreAnalysis.to_json()

# convert the object into a dict
neurostore_analysis_dict = neurostore_analysis_instance.to_dict()
# create an instance of NeurostoreAnalysis from a dict
neurostore_analysis_form_dict = neurostore_analysis.from_dict(neurostore_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


