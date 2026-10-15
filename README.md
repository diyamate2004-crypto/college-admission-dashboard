
# College Admission Data Analysis Dashboard

A professional Python Flask web application for analyzing college admission data stored in Excel.

## Features
- Professional responsive dashboard UI
- Excel-based data source
- Maximum 100 student records
- Essential KPI cards:
  - Total Students
  - Admitted Students
  - Admission Rate
  - Average 12th Marks
  - Average Entrance Score
  - Average Annual Fee
- Interactive charts:
  - Admissions by Course
  - Admission Status Distribution
  - Students by Category
  - 12th Marks vs Entrance Score
- Course, Gender, Category and Status filters
- Student record table with search
- Excel upload and dashboard refresh
- Data validation for required columns and 100-student limit

## Required Excel Columns
1. Student ID
2. Student Name
3. Gender
4. Category
5. Course
6. City
7. 12th Marks (%)
8. Entrance Score
9. Admission Status
10. Annual Fee (INR)

## Project Structure
college_admission_dashboard/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── college_admission_data.xlsx
├── static/
│   ├── app.js
│   └── style.css
└── templates/
    └── index.html

## How to Run

### 1. Open the project
Extract the ZIP and open the folder in VS Code or PyCharm.

### 2. Create a virtual environment (recommended)
Windows:
python -m venv venv
venv\Scripts\activate

### 3. Install packages
pip install -r requirements.txt

### 4. Start the web application
python app.py

### 5. Open in browser
http://127.0.0.1:5000

## Excel Upload
Go to "Excel Upload" in the dashboard and upload an Excel file containing the exact required columns. The dashboard accepts a maximum of 100 students.

## Notes
The demo Excel file contains 100 generated student records for testing.
