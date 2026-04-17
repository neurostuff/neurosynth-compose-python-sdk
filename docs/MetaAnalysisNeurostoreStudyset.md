# MetaAnalysisNeurostoreStudyset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neurostore_id** | **str** | The id of the studyset on neurostore. | [optional] 
**snapshot** | **object** | The snapshot of the studyset pending a successful run of the meta-analysis. | [optional] 
**annotations** | [**List[AnnotationSnapshotSummary]**](AnnotationSnapshotSummary.md) | Compact summaries of cached annotations paired with this studyset snapshot. | [optional] 
**neurostore_url** | **str** |  | [optional] [readonly] 
**version** | **str** | A string representing a labeled version of this particular studyset. | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis_neurostore_studyset import MetaAnalysisNeurostoreStudyset

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysisNeurostoreStudyset from a JSON string
meta_analysis_neurostore_studyset_instance = MetaAnalysisNeurostoreStudyset.from_json(json)
# print the JSON string representation of the object
print(MetaAnalysisNeurostoreStudyset.to_json())

# convert the object into a dict
meta_analysis_neurostore_studyset_dict = meta_analysis_neurostore_studyset_instance.to_dict()
# create an instance of MetaAnalysisNeurostoreStudyset from a dict
meta_analysis_neurostore_studyset_from_dict = MetaAnalysisNeurostoreStudyset.from_dict(meta_analysis_neurostore_studyset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


