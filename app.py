from flask import Flask, render_template, request, jsonify
import pandas as pd
from pathlib import Path

app = Flask(__name__)
DATA_FILE = Path("data/college_admission_data.xlsx")
REQUIRED_COLUMNS = [
    "Student ID","Student Name","Gender","Category","Course","City",
    "12th Marks (%)","Entrance Score","Admission Status","Annual Fee (INR)"
]

def load_data():
    df = pd.read_excel(DATA_FILE)
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError("Missing columns: " + ", ".join(missing))
    df = df[REQUIRED_COLUMNS].copy()
    df["12th Marks (%)"] = pd.to_numeric(df["12th Marks (%)"], errors="coerce")
    df["Entrance Score"] = pd.to_numeric(df["Entrance Score"], errors="coerce")
    df["Annual Fee (INR)"] = pd.to_numeric(df["Annual Fee (INR)"], errors="coerce")
    return df.dropna(subset=["Student ID"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/data")
def api_data():
    try:
        df = load_data()
        records = df.fillna("").to_dict(orient="records")
        return jsonify({"success": True, "data": records})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"success": False, "error": "No file selected."}), 400
    file = request.files["file"]
    if not file.filename.lower().endswith((".xlsx", ".xls")):
        return jsonify({"success": False, "error": "Please upload an Excel file."}), 400
    try:
        temp = pd.read_excel(file)
        missing = [c for c in REQUIRED_COLUMNS if c not in temp.columns]
        if missing:
            return jsonify({"success": False, "error": "Missing columns: " + ", ".join(missing)}), 400
        if len(temp) > 100:
            return jsonify({"success": False, "error": "Maximum 100 students are allowed."}), 400
        temp[REQUIRED_COLUMNS].to_excel(DATA_FILE, index=False)
        return jsonify({"success": True, "message": f"{len(temp)} student records uploaded successfully."})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
