student1 = Student(
    name="Alice",
    student_class="10th Grade",
    school_name="Sunrise High School"
)

# Add it to the session
db.session.add(student1)

# Commit to save in the database
db.session.commit()

print("Student added successfully!")