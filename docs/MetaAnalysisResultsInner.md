# MetaAnalysisResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | **object** |  | [optional] 
**meta_analysis_id** | **str** |  | [optional] 
**cli_version** | **str** |  | [optional] 
**estimator** | [**Estimator**](Estimator.md) |  | [optional] 
**neurostore_id** | **str** |  | [optional] 
**neurovault_collection** | [**NeurovaultCollection**](NeurovaultCollection.md) |  | [optional] 
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str** | Who owns the resource. | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis_results_inner import MetaAnalysisResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysisResultsInner from a JSON string
meta_analysis_results_inner_instance = MetaAnalysisResultsInner.from_json(json)
# print the JSON string representation of the object
print MetaAnalysisResultsInner.to_json()

# convert the object into a dict
meta_analysis_results_inner_dict = meta_analysis_results_inner_instance.to_dict()
# create an instance of MetaAnalysisResultsInner from a dict
meta_analysis_results_inner_form_dict = meta_analysis_results_inner.from_dict(meta_analysis_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


