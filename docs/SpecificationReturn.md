# SpecificationReturn

The view of the specification through an endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | the type of meta-analysis being run, typically either cbma or ibma, but others may become available in the future. | [optional] 
**estimator** | [**Estimator**](Estimator.md) |  | [optional] 
**mask** | **str** | a string representing a binary nifti file to select which voxels a user wants to include in the analysis. | [optional] 
**conditions** | [**SpecificationConditions**](SpecificationConditions.md) |  | [optional] 
**weights** | **List[float]** |  | [optional] 
**transformer** | **str** | A transformation applied to column(s) (e.g., binarize based on a threshold). This is likely to become deprecated. | [optional] 
**corrector** | [**Corrector**](Corrector.md) |  | [optional] 
**filter** | **str** | a column from annotations selecting which analyses to include in the meta-analysis | [optional] 
**database_studyset** | **str** |  | [optional] 
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str** | Who owns the resource. | [optional] 
**username** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.specification_return import SpecificationReturn

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificationReturn from a JSON string
specification_return_instance = SpecificationReturn.from_json(json)
# print the JSON string representation of the object
print(SpecificationReturn.to_json())

# convert the object into a dict
specification_return_dict = specification_return_instance.to_dict()
# create an instance of SpecificationReturn from a dict
specification_return_from_dict = SpecificationReturn.from_dict(specification_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


