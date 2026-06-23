Homework Tracker

A beginner-friendly Python project that helps students manage pending homework using JSON files and a menu-driven interface.

📌 Description

This project allows users to:

Add pending homework
View all homework
Search homework by subject
Delete homework records
Save data permanently
Load data automatically

All homework data is stored in homeworktracker.json, so assignments remain saved even after closing the program.

🧠 Concepts Used

Python Functions
Dictionaries
Nested Dictionaries
JSON Storage
File Handling
json.load()
json.dump()
Loops
User Input
Conditional Statements
Data Persistence

✨ Features

✅ Add Homework

✅ View Homework

✅ Search Homework

✅ Delete Homework

✅ Automatic JSON Saving

✅ Automatic JSON Loading

✅ Homework Due Date Tracking

✅ Total Homework Counter

📂 Files

homework_tracker.py
homeworktracker.json

💻 Stored Information

Each homework record contains:

Subject Name
Pending Homework
Due Date

Example:

{
    "Maths": {
        "homework": "Exercise 5.1",
        "due_date": "25-06-2026"
    }
}

▶️ Example Output

=== Homework Tracker ===

1. Add Pending Homework
2. View Homework
3. Search Homework
4. Delete Homework
5. Exit

Total homework: 1
Enter the number: 1

Enter the subject name: Maths
Enter the pending h.w: Exercise 5.1
Enter the due date: 25-06-2026

Saved
Subject = Maths
Homework Pending = Exercise 5.1
Due Date = 25-06-2026
