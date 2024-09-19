student = {
    "name" : "Brayan",
    "academic_year" : 2024,
    "units" : [{
        "name" : "Web Development",
        "credits" : 2000,
        "grade" : "B"
    },{
        "name" : "Network and System Administration",
        "credits" : 1500,
        "grade" : "C"
    },{
        "name" : "Java",
        "credits" : 1000,
        "grade" : "D"
    }],
    "total_credits" : sum(student["units"["credits"]]),
    #"GPA" : 
}
print(student)

grade_weight_mapping = {
    "A" : 4,
    "B" : 3,
    "C" : 2,
    "D" : 1,
    "E" : 0
}