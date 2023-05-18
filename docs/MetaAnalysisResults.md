# MetaAnalysisResults

array of neurostore ids representing the results of this meta-analysis (nominally all results should be the same, but machine architecture differences/algorithm stochastic-ness may lead to slightly different outcomes for each result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis_results import MetaAnalysisResults

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysisResults from a JSON string
meta_analysis_results_instance = MetaAnalysisResults.from_json(json)
# print the JSON string representation of the object
print MetaAnalysisResults.to_json()

# convert the object into a dict
meta_analysis_results_dict = meta_analysis_results_instance.to_dict()
# create an instance of MetaAnalysisResults from a dict
meta_analysis_results_form_dict = meta_analysis_results.from_dict(meta_analysis_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


