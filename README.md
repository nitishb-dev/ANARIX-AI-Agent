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

## 📦 Project Structure

📂ANARIX-AI-AGENT  
  ├── 📂__pycache__  
  ├── 📂datasets  
  │   └── 📄(Excel files or raw datasets)  
  ├── 📂db  
  │   └── 📄(MySQL config or helpers)  
  ├── 📂env *(excluded by .gitignore)*  
  ├── 📂llm  
  │   └── 📄agent.py *(Gemini + SQL + chart logic)*  
  ├── 📄.env *(holds GEMINI_API_KEY)*  
  ├── 📄.gitignore *(ignores env/, __pycache__/, .env etc.)*  
  ├── 📄api_check.py *(api testing script)*  
  ├── 📄cmds.txt *(CLI commands or experiment log)*  
  ├── 📄init_db.py *(script to populate MySQL from Excel)*  
  ├── 📄main.py *(FastAPI entry point with `/ask` endpoint)*  
  ├── 📄requirements.txt *(all required pip packages)*  
  ├── 📄TASK DESCRIPTION.md *(provided use-case or brief)*  
  └── 📄README.md *(project documentation you're reading)*

---

## 1. Create a Virtual Environment

python -m venv env
source env/bin/activate # Linux/macOS
.\env\Scripts\activate # Windows

## 2. Install Dependencies

pip install -r requirements.txt

## 3. Add Your Gemini API Key
Create a .env file:

GEMINI_API_KEY=your_gemini_api_key_here

Get your key from: https://makersuite.google.com/app/apikey

## 4. Configure MySQL DB
Ensure MySQL is running, and update the DB connection in init_db.py if needed.

## 5. Load Data into MySQL

python init_db.py

This loads your Excel files into MySQL tables.

## ▶️ Run the API Server

uvicorn main:app --reload

Access Swagger UI at:
http://127.0.0.1:8000/docs

## 💬 Example Questions
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

---

## 📦 Requirements

Python 3.8+

FastAPI

SQLAlchemy

pandas

matplotlib

python-dotenv

sse-starlette

MySQL (local or hosted)

Google Generative AI client (google-generativeai)

---

## 🧠 How It Works

User Input — Ask a question at the /ask API endpoint.

Gemini Processing — Generates a SQL query or chart instruction.

SQL Execution — FastAPI runs the SQL on the connected MySQL database.

Chart (Optional) — If requested, Matplotlib opens a popup with a chart.

---

## 📌 Notes

.env is excluded by .gitignore for security

Matplotlib is used to pop up chart windows (no frontend)

Error-handling and Gemini fallback are supported

---

## 📷 Screenshots

<div align="center">

  <img src="https://github.com/user-attachments/assets/e60e9244-4c1e-4ccb-b8a9-ebf07ef6f48f" alt="SQL Output Screenshot" width="1000" style="margin: 10px 0;" />

  <img src="https://github.com/user-attachments/assets/6f09ef1c-be57-4499-9613-85dfd6d6b420" alt="Chart Screenshot" width="986" style="margin: 10px 0;" />

  <img src="https://github.com/user-attachments/assets/d4ec6398-87d2-4194-b4c6-1f2d28666494" alt="Postman Screenshot" width="970" style="margin: 10px 0;" />

</div>


---

## 🙌 Credits
FastAPI

Google Gemini

SQLAlchemy

Matplotlib

Pandas


---

