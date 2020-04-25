customers = 'customers.txt'
contacts = 'allContacts.txt'

print("---Reading in the entire file")
with open(customers) as file_object:
    customers_lines = file_object.readlines()

with open(contacts) as contacts_object:
    contacts_lines = contacts_object.readlines()

print(customers_lines)
print(contacts_lines)

for customer_names in contacts_lines:
    if customers_lines in contacts_lines:
        print(contacts_lines.replace(customer_names, 'customer'))

