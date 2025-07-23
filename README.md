# 🧠 ANARIX AI Agent (FastAPI + Gemini + MySQL)

---

## 📘 Project Overview

This project focuses on building an AI agent designed to answer e-commerce data questions. The agent is capable of interpreting natural language questions, generating and executing SQL queries on provided datasets, and responding with accurate answers.

---

## 🚀 Features

This ANARIX AI Agent provides a powerful and intuitive way to interact with your e-commerce data:

- Natural Language Querying: The AI agent can understand and answer any question related to the provided e-commerce data.

- API-Driven Interaction: Questions are received via API endpoints, and the agent processes them to return accurate responses.

- SQL Conversion & Execution: The agent includes logic to convert natural language questions into SQL queries, fetch answers from the database, and return them in a human-readable format.

---

## 🧠 How It Works

1. **User Input** — Ask a question at the `/ask` API endpoint.
2. **Gemini Processing** — Generates a SQL query or chart instruction.
3. **SQL Execution** — FastAPI runs the SQL on the connected MySQL database.
4. **Chart Generation** — If requested, Matplotlib generates a chart and saves it as an image file in `assets/screenshots/`.  
   The API response includes the path to the chart image (e.g., `"chart_path": "assets/screenshots/chart.png"`), which can be viewed or served via your web server.
5. **Response** — The agent returns the answer, SQL query, query result, and chart path (if applicable).

---

## 📦 Project Structure

📂ANARIX-AI-AGENT  
 ├── 📂pycache   
 ├── 📂assets  
 │ └── 📂screenshots (has imgs)   
 ├── 📂datasets  
 │ └── 📄(Excel files or raw datasets)  
 ├── 📂db  
 │ └── 📄(MySQL config or helpers)  
 ├── 📂env _(excluded by .gitignore)_  
 ├── 📂llm  
 │ └── 📄agent.py _(Gemini + SQL + chart logic)_  
 ├── 📄.env _(holds GEMINI_API_KEY)_  
 ├── 📄.gitignore _(ignores env(virtual environment)/, pycache/, .env, api_check.py, cmds.txt.)_    
 ├── 📄init_db.py _(script to populate MySQL from Excel)_  
 ├── 📄main.py _(FastAPI entry point with `/ask` endpoint)_  
 ├── 📄requirements.txt _(all required pip packages)_  
 ├── 📄TASK DESCRIPTION.md _(provided use-case or brief)_  
 └── 📄README.md _(project documentation you're reading)\_

---

## 1. Create a Virtual Environment

python -m venv env

source env/Scripts/activate #bash

## 2. Install Dependencies

pip install -r requirements.txt

## 3. Add Your Gemini API Key

Create a .env file:

GEMINI_API_KEY=your_gemini_api_key_here

Get your key from: https://makersuite.google.com/app/apikey

## 4. Configure MySQL DB

Ensure MySQL is running, and update the DB connection in init_db.py if needed.

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

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


## 📊 Chart Output

- Chart images are saved automatically in `assets/screenshots/` whenever a chart is requested.
- The API response includes the chart image path for easy access and integration.
- Example response:
  ```json
  {
    "question": "Show me a bar chart of total sales by product",
    "sql_generated": "SELECT product, SUM(total_sales) FROM total_sales_metrics GROUP BY product",
    "query_result": [...],
    "answer": "Query executed successfully with chart",
    "chart_path": "assets/screenshots/chart.png",
    "type": "select"
  }
  ```
  
---

## 📷 Screenshots

<div align="center">

   <h2>DB & Tables in MySQL</h2>

   <img width="133" height="80" alt="Screenshot 2025-07-22 195118" src="https://github.com/user-attachments/assets/f492428c-e86b-448b-bf4d-131f10889185" />

  <h2>Swagger UI(/docs)<h2>

  <img src="https://github.com/user-attachments/assets/e60e9244-4c1e-4ccb-b8a9-ebf07ef6f48f" alt="SQL Output Screenshot" width="1000" style="margin: 10px 0;" />

  <img src="https://github.com/user-attachments/assets/6f09ef1c-be57-4499-9613-85dfd6d6b420" alt="Chart Screenshot" width="986" style="margin: 10px 0;" />

  <h2>Chart Output Example (Saved Image)</h2>
  <img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/ba70d7d1-b43f-428b-9ffc-a473d1f5cdea" />


  <h2>Terminal Output (Generated by Gemini API)<h2>

  <img src="https://github.com/user-attachments/assets/d4ec6398-87d2-4194-b4c6-1f2d28666494" alt="Postman Screenshot" width="970" style="margin: 10px 0;" />


  <h2>MySQL Output</h2>
  <img width="1533" height="645" alt="image" src="https://github.com/user-attachments/assets/ab5d4d1c-dba9-4876-b76c-26268e0ce5d2" />

</div>

---

## 🙌 Credits

FastAPI

Google Gemini

SQLAlchemy

Matplotlib

Pandas

---

## 🙋‍♂️ Author

**Nitish B**  
Final Year Student | Software Developer & AI Enthusiast  
📫 [GitHub](https://github.com/nitishb-dev) • [LinkedIn](https://www.linkedin.com/in/nitishb-dev)

---

### ⭐️ Star the Repository

If you found this project helpful, consider starring ⭐ it on GitHub to support future development!
