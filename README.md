 
"employee_count": {
    "description": (
        "The number of people employed by the company, "
        "or the employee-size range explicitly declared "
        "by the company."
    ),
    "extract": (
        "Extract only an explicitly stated company employee "
        "count or company-size range. Prefer labelled values "
        "such as 'Company size: 11-50 employees'. "
        "Do not extract LinkedIn followers, page followers, "
        "profile views, employees visible in a profile list, "
        "or counts of people who follow the company. "
        "A number is valid only when the surrounding context "
        "clearly identifies it as the company's employee "
        "count or company-size range. Preserve ranges exactly."
    ),
    "example": "11-50 employees"
},
