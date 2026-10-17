
def test_mark_attendance():
    student_id = "STU101"
    attendance_status = "Present"

    if student_id and attendance_status in ["Present", "Absent"]:
        print("PASS: Attendance data is valid")
    else:
        print("FAIL: Attendance data is invalid")


def test_missing_student_id():
    student_id = ""
    attendance_status = "Present"

    if not student_id:
        print("PASS: Missing student ID detected")
    else:
        print("FAIL: Missing student ID not detected")


test_mark_attendance()
test_missing_student_id()