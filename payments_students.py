import student_payment


print('\n')

student_monthly_scholarship = student_payment.Monthly_Scholarship('Jon Doe', 3, 90)
student_scholarships = student_payment.StudentScholarship()
student_scholarships.student_scholarship([
    student_monthly_scholarship
])

print('\n')

student_fees = student_payment.Student_Fee('Karen Smith', 4 , 'US')
fee_students = student_payment.StudentFeeSemester()
fee_students.student_fee_semester([
    student_fees
])
