import json

data = {
  "users": [
    {
      "id": 0,
      "name": "Adam Carter",
      "work": "Unilogic",
      "email": "adam.carter@unilogic.com",
      "dob": "1978",
      "address": "83 Warner Street",
      "city": "Boston",
      "optedin": True
    },
    {
      "id": 1,
      "name": "Leanne Brier",
      "work": "Connic",
      "email": "leanne.brier@connic.org",
      "dob": "1987",
      "address": "9 Coleman Avenue",
      "city": "Toronto",
      "optedin": False
    }
  ],
  "images": [
    "img0.png",
    "img1.png",
    "img2.png"
  ],
  "coordinates": {
    "x": 35.12,
    "y": -21.49
  },
  "price": "$59,395"
}

# try:  
#     with open("data1.json", "w") as write_file:
#      json.dump(data, write_file, )
#      print("Data has been added successuflly!")     
# except:
#     print("Error occured!")
    
# try:  
#     with open("data.json", "w") as write_file:
#      json.dump(data, write_file, indent=4)
#      print("Data has been added successuflly!")     
# except:
#     print("Error occured!")
    
    
json_string = json.dumps(data)
print(type(json_string))
# json_string = json.dumps(data, indent =  4 )
# json_string = json.dumps(data, indent =  2 )

# print(json_string)
# print("####################################")
# print(data)
with open("data.json", "r") as read_file:
    data = json.load(read_file)

# print(json.dumps(data, indent= 4))


