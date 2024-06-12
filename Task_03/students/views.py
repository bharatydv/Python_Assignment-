from django.shortcuts import render, redirect
from django.db import connection, OperationalError
from .models import Student

def manage_students(request):
    error = None
    students = []

    try:
        # Insert a new student record
        if request.method == 'POST' and 'insert' in request.POST:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            age = request.POST.get('age')
            grade = request.POST.get('grade')
            if first_name and last_name and age and grade:
                Student.objects.create(first_name=first_name, last_name=last_name, age=age, grade=grade)
                return redirect('manage_students')
            else:
                error = "All fields are required for insertion."

        # Update the grade of the student with the first name "Alice"
        elif request.method == 'POST' and 'update' in request.POST:
            first_name = request.POST.get('first_name')
            new_grade = request.POST.get('new_grade')
            student = Student.objects.filter(first_name=first_name).first()
            if student:
                student.grade = new_grade
                student.save()
                return redirect('manage_students')
            else:
                error = f"Student with first name {first_name} not found."

        # Delete the student with the last name "Smith"
        elif request.method == 'POST' and 'delete' in request.POST:
            last_name = request.POST.get('last_name')
            student = Student.objects.filter(last_name=last_name).first()
            if student:
                student.delete()
                return redirect('manage_students')
            else:
                error = f"Student with last name {last_name} not found."

        # Fetch and display all student records
        students = Student.objects.all()

    except OperationalError as e:
        error = str(e)

    return render(request, 'students/manage_students.html', {'students': students, 'error': error})
