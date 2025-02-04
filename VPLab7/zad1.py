import json

python_object = {
    "name": "Радко",
    "age": 19,
    "grades": [5.5, 6.0, 4.8],
    "address": {
        "city": "Враца",
        "postal_code": 3000
    }
}

json_data = json.dumps(python_object, indent=4, ensure_ascii=False)

print("Python към JSON данни:")
print(json_data)

