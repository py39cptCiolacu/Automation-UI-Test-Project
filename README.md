# 🧪 API Testing Project using `pytest`, `requests`, and `Playwright`

This repository contains a suite of automated tests built with `pytest`, using the `requests` library for REST API interactions and `Playwright` for optional frontend validations. The tests cover key HTTP operations such as `GET`, `POST`, `PATCH`, as well as validations, sorting, and filtering using query parameters.

---

## ✅ Features Implemented

### 1. 📥 Fetching All Endpoint Data
Performed `GET` requests for each of the following endpoints:
- `/users`
- `/posts`
- `/comments`
- `/todos`

The results were parsed and formatted into a more human-readable output.

---

### 2. 🧑‍💻 Creating a New User
Sent a `POST` request to create a new user with custom information. The response data for the newly created user was printed and validated.

---

### 3. 🔍 Verifying User Count Increments
Implemented a test to check that after adding a new user, the total number of users has increased by exactly one.

---

### 4. 🧾 Searching User by Name
Built a method that retrieves a user by using a query parameter (e.g., `?username=...`). The user's ID is extracted from the response and reused in subsequent tests.

---

### 5. ✅ Displaying First 20 Active Users
Filtered and displayed the first 20 users that are considered "active" based on available data (e.g., having posts, todos, or other activity).

---

### 6. 📛 Users with Middle Names
Displayed the first 5 users who have a middle name, assumed by detecting names with three parts (e.g., "John Michael Doe").

---

### 7. 📝 Creating Related Resources for a User
For the previously created user, the following resources were added:
- A post
- A comment
- A todo item

The methods are reusable and support creation for any user by ID.

---

### 8. ✉️ Updating Email Address
Created a method to update a user's email address via a `PATCH` request and verified the update through a follow-up API call.

---

### 9. 📆 Sorting Todos by Due Date
Fetched the first 20 todos and displayed them in ascending order based on their `dueDate` field (if available).

---

## 🧰 Tech Stack

- Python 3
- [pytest](https://docs.pytest.org/)
- [requests](https://docs.python-requests.org/)
- [Playwright](https://playwright.dev/python/)

---

## 🏁 How to Run the Tests

1. Install dependencies:

```bash
pip install -r requirements.txt
