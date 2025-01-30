from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Excel file path
FILE_PATH = r"D:\KN Study\github study\s-khandelwal.github.io\contact_data.xlsx"

@app.route("/save", methods=["POST"])
def save_data():
    data = request.json
    new_entry = pd.DataFrame([data])

    # Check if the file exists
    if os.path.exists(FILE_PATH):
        df = pd.read_excel(FILE_PATH)
        df = pd.concat([df, new_entry], ignore_index=True)
    else:
        df = new_entry

    df.to_excel(FILE_PATH, index=False)

    return jsonify({"message": "Data saved successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
