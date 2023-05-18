# Estimator

the specification for the function/class running the meta-analysis

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | the meta-analytic algorithm applied to the data. Currently this should be directly tied to the function/class running the meta-analysis. For example, ALE, or MKDADensity are valid NiMARE classes to put here. | [optional] 
**args** | **object** | arbitrary keyword arguments to be passed into the function/class to modify default functionality, this could modify the kernel, resampling methods, or any other behavior defined in the function/class (like MKDADensity). | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.estimator import Estimator

# TODO update the JSON string below
json = "{}"
# create an instance of Estimator from a JSON string
estimator_instance = Estimator.from_json(json)
# print the JSON string representation of the object
print Estimator.to_json()

# convert the object into a dict
estimator_dict = estimator_instance.to_dict()
# create an instance of Estimator from a dict
estimator_form_dict = estimator.from_dict(estimator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


