import mysql.connector
# Connect to MySQL
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abhi123",
    database="school"
)

# Create a cursor object using the cursor() method
cursor = db_connection.cursor()

try:
    # Task 2: Insert a new student record
    insert_query = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
    student_data = ("Alice", "Smith", 18, 95.5)
    cursor.execute(insert_query, student_data)
    db_connection.commit()
    print("Student record inserted successfully.")

    # Task 3: Update the grade of the student named Alice
    update_query = "UPDATE students SET grade = %s WHERE first_name = %s"
    new_grade = 97.0
    cursor.execute(update_query, (new_grade, "Alice"))
    db_connection.commit()
    print("Grade updated successfully.")

    # Task 4: Delete the student with last name Smith
    delete_query = "DELETE FROM students WHERE last_name = %s"
    cursor.execute(delete_query, ("Smith",))
    db_connection.commit()
    print("Student record deleted successfully.")

    # Task 5: Fetch and display all student records
    select_query = "SELECT * FROM students"
    cursor.execute(select_query)
    students = cursor.fetchall()

    print("\nAll Students:")
    for student in students:
        print(student)

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    # Close the cursor and database connection
    if db_connection.is_connected():
        cursor.close()
        db_connection.close()
        print("\nMySQL connection closed.")