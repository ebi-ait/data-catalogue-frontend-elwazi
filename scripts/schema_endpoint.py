import requests as rq
import json

data = {
    'token': '-',
    'content': 'metadata',
    'format': 'json',
    'returnFormat': 'json',
}

r = rq.post('https://redcap.h3abionet.org/redcap/api/',data=data)
print('HTTP Status: ' + str(r.status_code))
# print(r.json())
redcap_data = r.json()


# Convert REDCap data to HAL format
hal_data = {
    "_links": {
        "self": {"href": "/redcap"}
    },
    "_embedded": {
        "properties": []
    }
}


for record in redcap_data:
    record_data = {record["field_name"]:
    {
        "form_name": record["form_name"],
        "field_type": record["field_type"],
        "select_choices_or_calculations": record["select_choices_or_calculations"],
        "required_field": record["required_field"],
        "text_validation_type_or_show_slider_number": record["text_validation_type_or_show_slider_number"],
        "text_validation_min": record["text_validation_min"],
        "text_validation_max": record["text_validation_max"]

    }}
    hal_data["_embedded"]["properties"].append(record_data)


# Print the HAL data
with open('../k8s/overlays/elwazi/schema_endpoint.json', 'w', ) as f:
    json.dump(hal_data, f, ensure_ascii=False, indent=4, separators=(',', ': '))



