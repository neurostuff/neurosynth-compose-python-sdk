# MetaAnalysisStudyset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neurostore_id** | **str** | The id of the studyset on neurostore. | [optional] 
**snapshot** | **object** | The snapshot of the studyset pending a successful run of the meta-analysis. | [optional] 
**neurostore_url** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis_studyset import MetaAnalysisStudyset

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysisStudyset from a JSON string
meta_analysis_studyset_instance = MetaAnalysisStudyset.from_json(json)
# print the JSON string representation of the object
print MetaAnalysisStudyset.to_json()

# convert the object into a dict
meta_analysis_studyset_dict = meta_analysis_studyset_instance.to_dict()
# create an instance of MetaAnalysisStudyset from a dict
meta_analysis_studyset_form_dict = meta_analysis_studyset.from_dict(meta_analysis_studyset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


