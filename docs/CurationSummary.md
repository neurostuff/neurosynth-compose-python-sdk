# CurationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[CurationSummaryColumnsInner]**](CurationSummaryColumnsInner.md) |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.curation_summary import CurationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CurationSummary from a JSON string
curation_summary_instance = CurationSummary.from_json(json)
# print the JSON string representation of the object
print(CurationSummary.to_json())

# convert the object into a dict
curation_summary_dict = curation_summary_instance.to_dict()
# create an instance of CurationSummary from a dict
curation_summary_from_dict = CurationSummary.from_dict(curation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


