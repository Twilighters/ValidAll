import jsonschema
import json

with open("myJson.schema.json", "r", encoding="UTF-8") as file_json_schema:
    data_schema = json.load(file_json_schema)
with open("myJson.json", "r", encoding="UTF-8") as file_json:
    data = json.load(file_json)

validate = jsonschema.validate(data, schema=data_schema)
