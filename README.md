# 🧠 ANARIX AI Agent (FastAPI + Gemini + MySQL)

An intelligent AI-powered agent designed to interpret natural language questions, automatically generate SQL queries, execute them on a MySQL database, and optionally display visualizations — all through a user-friendly FastAPI interface.

It leverages **Google Gemini** (via Generative AI API) for robust natural language understanding and **Matplotlib** for insightful data visualizations on your e-commerce sales, ads, and eligibility metrics.

---

## 🚀 Features

This ANARIX AI Agent provides a powerful and intuitive way to interact with your e-commerce data:

✅ **Natural Language Interaction**  
Ask questions in plain English, such as:

- "What is the total ad spend?"
- "Which item had the highest CPC?"
- "Generate a pie chart of sales by item"
- "Insert a new entry into sales_metrics table"

✅ **Automated SQL Generation & Execution**  
Automatically understands your natural language queries, generates the correct SQL, and executes it against your MySQL database.

✅ **Direct Answers & Visualizations**  
Displays query results directly or provides clear answers. It can also plot bar or pie charts using Matplotlib for visual data analysis.

✅ **Data Manipulation**  
Supports `SELECT`, `INSERT`, `UPDATE`, and `DELETE` operations via natural language.

---

## 🗂️ Project Structure

ANARIX-AI-AGENT/
├── pycache/ # Python bytecode
├── datasets/ # Excel files or raw data
├── db/ # MySQL configuration/helpers
├── env/ # Virtual environment (excluded by .gitignore)
├── llm/ # LLM/Gemini-related logic
├── .env # Contains Gemini API Key
├── .gitignore # Ignore env, pycache, .env, etc.
├── chech.py # Misc/utility script
├── cmds.txt # Notes or command history
├── init_db.py # Populates MySQL DB from Excel
├── main.py # FastAPI entry point
├── requirements.txt # Python dependencies
├── TASK DESCRIPTION.md # Original assignment or scope
└── README.md # 📄 This file

✅ 2. Create a Virtual Environment
bash
Copy
Edit
python -m venv env
source env/bin/activate # Linux/macOS
.\env\Scripts\activate # Windows
✅ 3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
✅ 4. Add Your Gemini API Key
Create a .env file:

env
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key_here
Get your key from: https://makersuite.google.com/app/apikey

✅ 5. Configure MySQL DB
Ensure MySQL is running, and update the DB connection in init_db.py if needed.

✅ 6. Load Data into MySQL
bash
Copy
Edit
python init_db.py
This loads your Excel files into MySQL tables.

▶️ Run the API Server
bash
Copy
Edit
uvicorn main:app --reload
Access Swagger UI at:
http://127.0.0.1:8000/docs

💬 Example Questions
📊 Data Queries
"What is the total ad spend?"

"How many clicks did item 101 get?"

"Show me all metrics for item 21"

📈 Business Metrics
"What is the Return on Ad Spend (RoAS)?"

"Which item had the highest CPC?"

📊 Chart Requests
"Generate a pie chart of sales by item"

"Show a bar chart of revenue per product"

🛠️ Data Updates
"Insert a new item into sales_metrics"

"Update ad spend for item 32"

"Delete entry where item_id is 99"

📦 Requirements
Python 3.8+

FastAPI

SQLAlchemy

pandas

matplotlib

python-dotenv

sse-starlette

MySQL (local or hosted)

Google Generative AI client (google-generativeai)

🧠 How It Works
User Input — Ask a question at the /ask API endpoint.

Gemini Processing — Generates a SQL query or chart instruction.

SQL Execution — FastAPI runs the SQL on the connected MySQL database.

Chart (Optional) — If requested, Matplotlib opens a popup with a chart.

📌 Notes
.env is excluded by .gitignore for security

Matplotlib is used to pop up chart windows (no frontend)

Error-handling and Gemini fallback are supported

📷 Screenshots
(Optional — Add these)

SQL Query Chart Example

🙌 Credits
FastAPI

Google Gemini

SQLAlchemy

Matplotlib

Pandas

📬 License
This project is licensed under the MIT License.

markdown
Copy
Edit

---

### ✅ Notes:

- Place this in `README.md`
- You can optionally update:
  - `screenshots/` folder with real images
  - `.gitignore` to ignore `.env`, `/env`, etc.
  - The GitHub URL if you’ve already pushed this

Let me know if you want help with:

- Creating a `LICENSE`
- Adding a badge for Gemini or FastAPI
- Deploying on Render/Vercel/EC2

All set for GitHub now! ✅

Ask ChatGPT
