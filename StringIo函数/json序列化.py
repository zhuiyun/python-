import json

data={"name":"yun","age":19}
jsData=json.dumps(data)
print(data)
print(jsData)

data2=json.loads(jsData)
print(data2["name"])
print(data["name"])