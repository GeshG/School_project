import teacher_payment

teacher_salary_monthly = teacher_payment.MonthlySalaryTeacher(1, 'Jane', 'Smith', 24, 92, 1000)
teacher_salary_honored = teacher_payment.HonoredTeacher(2, 'Peter','Pan', 30, 87, 10, 10)
payroll_system = teacher_payment.PayRoll()
payroll_system.calculate_payroll([
    teacher_salary_monthly,
    teacher_salary_honored,
])
