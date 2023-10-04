# SpecificationConditions

selection of categories in the filter column to differentiate groups, or \"neurosynth\", \"neuroquery\", or \"neurostore\" to compare to a database reference group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from neurosynth_compose_sdk.models.specification_conditions import SpecificationConditions

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificationConditions from a JSON string
specification_conditions_instance = SpecificationConditions.from_json(json)
# print the JSON string representation of the object
print SpecificationConditions.to_json()

# convert the object into a dict
specification_conditions_dict = specification_conditions_instance.to_dict()
# create an instance of SpecificationConditions from a dict
specification_conditions_form_dict = specification_conditions.from_dict(specification_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


