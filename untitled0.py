import json
data = [
        {
          "username": "Mike",
          "code": "12345",
          "city": "NYC"
        },
        {
          "username": "kor",
          "code": "12345",
          "city": "NYC"
        },
      ]


with open('config.txt') as json_file:
   rew = json.load(json_file)

rew.append({
          "username": "kotey",
          "code": "12345",
          "city": "NYC"
        })


print(rew)
with open('config.txt', 'w') as outfile:
  json.dump(rew, outfile) 

# print(data)