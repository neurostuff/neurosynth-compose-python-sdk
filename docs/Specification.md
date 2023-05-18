# Specification

a machine readable specification of how to run a meta-analysis (currently specifically tailored to NiMARE).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | the type of meta-analysis being run, typically either cbma or ibma, but others may become available in the future. | [optional] 
**estimator** | [**Estimator**](Estimator.md) |  | [optional] 
**mask** | **str** | a string representing a binary nifti file to select which voxels a user wants to include in the analysis. | [optional] 
**contrast** | **str** | underspecified selection of columns to contrast (TODO, make better). | [optional] 
**transformer** | **str** | A transformation applied to column(s) (e.g., binarize based on a threshold). This is likely to become deprecated. | [optional] 
**corrector** | [**Corrector**](Corrector.md) |  | [optional] 
**filter** | **str** | a boolean column from annotations selecting which analyses to include in the meta-analysis | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.specification import Specification

# TODO update the JSON string below
json = "{}"
# create an instance of Specification from a JSON string
specification_instance = Specification.from_json(json)
# print the JSON string representation of the object
print Specification.to_json()

# convert the object into a dict
specification_dict = specification_instance.to_dict()
# create an instance of Specification from a dict
specification_form_dict = specification.from_dict(specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


