# SpecificationPostBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | the type of meta-analysis being run, typically either cbma or ibma, but others may become available in the future. | [optional] 
**estimator** | [**Estimator**](Estimator.md) |  | [optional] 
**mask** | **str** | a string representing a binary nifti file to select which voxels a user wants to include in the analysis. | [optional] 
**contrast** | **str** | selection of categories in the filter column to differentiate groups, or \&quot;neurosynth\&quot;, \&quot;neuroquery\&quot;, or \&quot;neurostore\&quot; to compare to a database reference group | [optional] 
**transformer** | **str** | A transformation applied to column(s) (e.g., binarize based on a threshold). This is likely to become deprecated. | [optional] 
**corrector** | [**Corrector**](Corrector.md) |  | [optional] 
**filter** | **str** | a column from annotations selecting which analyses to include in the meta-analysis | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.specification_post_body import SpecificationPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificationPostBody from a JSON string
specification_post_body_instance = SpecificationPostBody.from_json(json)
# print the JSON string representation of the object
print SpecificationPostBody.to_json()

# convert the object into a dict
specification_post_body_dict = specification_post_body_instance.to_dict()
# create an instance of SpecificationPostBody from a dict
specification_post_body_form_dict = specification_post_body.from_dict(specification_post_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


