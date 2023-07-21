import json
import requests

res = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(res.text)

# print(res)
# print("\n\n\n#############################################################\n\n\n\n")
# print(todos)
try:
    with open ("todos.json", "w") as file:
        json.dump(todos, file, indent=4)
        print("Data has been added successuflly!")     
except Exception as e:
        print("Error occured!\nthe error is: "+str(e))
        
        
        
# Map of userId to number of complete TODOs for that user
todos_by_user = {}

for todo in todos: # Increment complete TODOs count for each user.
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1  # Increment the existing user's count.
        except KeyError:
            todos_by_user[todo["userId"]] = 1   # This user has not been seen. Set their count to 1.
            
# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)

# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]

# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))
print(users)
max_users = " and ".join(users)