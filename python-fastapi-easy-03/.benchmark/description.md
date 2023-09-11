Create a resource `/items` that allows for basic CRUD operations (Create, Read, Update, Delete).
Items can be stored in memory, no need to use a database.

## Requirements
- A POST request to `/items` should create a new Item.
- A GET request to `/items` should return a list of all Item objects.
- A GET request to `/items/:id` should return the Item with the specified ID.
- A PUT request to `/items/:id` should update the Item with the specified ID.
- A DELETE request to `/items/:id` should delete the Item with the specified ID.

An Item object should have the following properties:
- id: string (defined by the server)
- name: string (defined by the client)
- created_at: datetime (defined by the server)
- updated_at: datetime (defined by the server)

Endpoints should return appropriate status codes:
- 201 for POST
- 200 for GET/PUT/DELETE
- 404 for not found

## Reminders
- Don't modify existing endpoints unless instructed to do so.
- Don't forget to update the `requirements.txt` file with any new dependencies.