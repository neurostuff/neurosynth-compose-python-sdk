# Corrector

The function/class applying statistical adjustments to the output of the meta-analysis (optional).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | the name of the function/class performing the correction. For example FWECorrector from NiMARE would be valid. | [optional] 
**args** | **object** | key word arguments passed to the corrector to modidy default functionality, such as number of iterations, or the particular method of correction being applied. | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.corrector import Corrector

# TODO update the JSON string below
json = "{}"
# create an instance of Corrector from a JSON string
corrector_instance = Corrector.from_json(json)
# print the JSON string representation of the object
print Corrector.to_json()

# convert the object into a dict
corrector_dict = corrector_instance.to_dict()
# create an instance of Corrector from a dict
corrector_form_dict = corrector.from_dict(corrector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


