# MetaAnalysisList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[MetaAnalysisReturn]**](MetaAnalysisReturn.md) |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis_list import MetaAnalysisList

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysisList from a JSON string
meta_analysis_list_instance = MetaAnalysisList.from_json(json)
# print the JSON string representation of the object
print MetaAnalysisList.to_json()

# convert the object into a dict
meta_analysis_list_dict = meta_analysis_list_instance.to_dict()
# create an instance of MetaAnalysisList from a dict
meta_analysis_list_form_dict = meta_analysis_list.from_dict(meta_analysis_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


