import streamlit as st
import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll TEXT,
    department TEXT,
    semester TEXT
)
""")
conn.commit()

st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓"
)

st.title("🎓 Student Management System")
st.caption("Simple Student CRUD Project")

menu = st.sidebar.selectbox("📌 Menu",["🏠 Dashboard", "➕ Add Student", "📋 Students", "✏️ Update Student","🗑️ Delete Student", "👤 My Info"])

if menu == "🏠 Dashboard":

    st.header("🏠 Dashboard")
    st.write("Welcome to Student Management System")

    cur.execute("SELECT COUNT(*) FROM students")
    total = cur.fetchone()[0]

    col1, col2, col3 = st.columns(3)

    col1.metric("👨‍🎓 Total Students", total)
    col2.metric("💾 Database", "SQLite")
    col3.metric("🐍 Language", "Python")

    st.divider()

    st.subheader("📌 CRUD Operations")

    col1, col2 = st.columns(2)

    with col1:
        st.info("➕ Create - Add Student")
        st.info("📋 Read - View Students")

    with col2:
        st.warning("✏️ Update - Edit Student")
        st.error("🗑️ Delete - Remove Student")

elif menu == "➕ Add Student":
    st.header("➕ Add Student")

    name = st.text_input("Name")
    roll = st.text_input("Roll")
    department = st.text_input("Department")
    semester = st.text_input("Semester")

    if st.button("Add Student", type="primary"):
        if name and roll:
            cur.execute(
                "INSERT INTO students (name, roll, department, semester) VALUES (?, ?, ?, ?)",
                (name, roll, department, semester)
            )
            conn.commit()
            st.success("✅ Student added successfully!")
        else:
            st.warning("⚠️ Name and Roll are required.")


elif menu == "📋 Students":
    st.header("📋 All Students")

    cur.execute("SELECT * FROM students")
    students = cur.fetchall()

    if students:
        for student in students:
            with st.container(border=True):
                st.write(
                    f"ID: {student[0]}  |  "
                    f"Name: {student[1]}  |  "
                    f"Roll: {student[2]}  |  "
                    f"Department: {student[3]}  |  "
                    f"Semester: {student[4]}"
                )
    else:
        st.info("No students added yet.")


elif menu == "✏️ Update Student":
    st.header("✏️ Update Student")

    id = st.number_input("Student ID", min_value=1, step=1)

    name = st.text_input("New Name")
    roll = st.text_input("New Roll")
    department = st.text_input("New Department")
    semester = st.text_input("New Semester")

    if st.button("Update Student", type="primary"):
        cur.execute(
            "UPDATE students SET name=?, roll=?, department=?, semester=? WHERE id=?",
            (name, roll, department, semester, id)
        )
        conn.commit()
        st.success("✅ Student updated successfully!")


elif menu == "🗑️ Delete Student":
    st.header("🗑️ Delete Student")

    id = st.number_input("Student ID", min_value=1, step=1)

    if st.button("Delete Student", type="primary"):
        cur.execute("DELETE FROM students WHERE id=?", (id,))
        conn.commit()
        st.success("🗑️ Student deleted successfully!")


elif menu == "👤 My Info":
    st.header("👤 My Info")

    st.subheader("Tarek Amin Arik")

    st.write("🎓 Computer Science and Technology")
    st.write("🏫 Brahmanbaria Polytechnic Institute")

    st.divider()

    st.write("""
    Highly interested in Python, Web applications and AI/ML.
    This Student Management System is my CRUD operation project.
    """)

    st.subheader("🛠️ Skills")

    st.write(
        "Python | NumPy | Pandas | Streamlit | "
        "Matplotlib | Seaborn | Scikit-learn"
    )

conn.close()
