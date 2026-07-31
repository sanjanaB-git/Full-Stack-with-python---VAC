from config import tickets_collection


# Insert a new ticket
def create_ticket(ticket):
    tickets_collection.insert_one(ticket)


# Get all tickets
def get_all_tickets():
    return list(tickets_collection.find())


# Assign ticket to a staff member
def assign_ticket(title, assigned_to):
    tickets_collection.update_one(
        {"title": title},
        {
            "$set": {
                "assigned_to": assigned_to
            }
        }
    )


# Update ticket priority
def update_priority(title, priority):
    tickets_collection.update_one(
        {"title": title},
        {
            "$set": {
                "priority": priority
            }
        }
    )


# Update ticket status
def update_status(title, status):
    tickets_collection.update_one(
        {"title": title},
        {
            "$set": {
                "status": status
            }
        }
    )


# Find one ticket
def get_ticket(title):
    return tickets_collection.find_one({"title": title})


# Delete a ticket (optional)
def delete_ticket(title):
    tickets_collection.delete_one({"title": title})