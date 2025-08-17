a= {
    "key":"value",
    "exam":"boards",
    "devansh":99,
    "gopalji":97,
    "tulsi":100,
    "list":[2,4,6,7],
    0:"harry"
}

print(a.items())
# output coming dict_items([('key', 'value'), ('exam', 'boards'), ('devansh', 99), ('gopalji', 97), ('tulsi', 100), ('list', [2, 4, 6, 7]), (0, 'harry')])  this is returning output in the tuple form 

print(a.keys())
#dict_keys(['key', 'exam', 'devansh', 'gopalji', 'tulsi', 'list', 0])

print(a.values())


print(a.update({"exam":"test"}))
print(a)


print(a.update({"exam":"Graduation", "new":"palak"}))
print(a)



print(a.get("harry","shiv")) #dictionary.get(key, default_value)
#If key exists ➝ return its value.If key doesn't exist ➝ return default_value (or None if not given).

print(a.get("harry"))