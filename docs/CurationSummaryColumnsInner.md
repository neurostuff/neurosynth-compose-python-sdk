# CurationSummaryColumnsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**stub_count** | **int** |  | [optional] 
**exclusions** | **Dict[str, int]** | stub count per exclusion tag id | [optional] 
**tags** | **Dict[str, int]** | stub count per tag id | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.curation_summary_columns_inner import CurationSummaryColumnsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CurationSummaryColumnsInner from a JSON string
curation_summary_columns_inner_instance = CurationSummaryColumnsInner.from_json(json)
# print the JSON string representation of the object
print(CurationSummaryColumnsInner.to_json())

# convert the object into a dict
curation_summary_columns_inner_dict = curation_summary_columns_inner_instance.to_dict()
# create an instance of CurationSummaryColumnsInner from a dict
curation_summary_columns_inner_from_dict = CurationSummaryColumnsInner.from_dict(curation_summary_columns_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


