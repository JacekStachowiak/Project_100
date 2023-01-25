import json

# write --> json.dump()
# read --> json.load()
# update --> json.update()

new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

# write
with open('data.json', 'w') as data_file:
    json.dump(new_data, data_file, indent=4)

# load i update
with open('data.json', 'r') as data_file:
    data = json.load(data_file)
    data.update(new_data)
# znowu zapis
with open('data.json', 'w') as data_file:
    json.dump(new_data, data_file, indent=4)

