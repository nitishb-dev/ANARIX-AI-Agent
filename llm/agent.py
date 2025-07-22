# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import textwrap
# from tabulate import tabulate
# from sqlalchemy import text
# from dotenv import load_dotenv
# import google.generativeai as genai

# # ✅ Load environment variables and Gemini config
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # ✅ Use Gemini 2.5 Flash model (you must have access)
# model = genai.GenerativeModel("gemini-2.5-flash")

# # 🔍 Ask Gemini to generate SQL or chart signal
# def ask_gemini(question: str, schema: str) -> dict:
#     prompt = f"""
# You are an intelligent SQL assistant for a MySQL database.
# Based on the schema below, do one of the following:

# 1. If the question is about data, return a valid SQL query (SELECT/INSERT/UPDATE/DELETE).
# 2. If it's a general or non-data question, return a natural language answer.
# 3. If it's a chart request, return: CHART:<bar or pie>

# Schema:
# {schema}

# User question:
# {question}

# Return ONLY the SQL or plain text response. No markdown, no formatting.
# """
#     try:
#         response = model.generate_content(prompt)
#         return {"raw": response.text.strip()}
#     except Exception as e:
#         return {"raw": f"-- Gemini Error: {e}"}

# # 🧠 Main function to handle user questions
# def process_question(question: str, db):
#     schema = get_db_schema(db)

#     # Step 1: Ask Gemini if it’s a chart
#     chart_check = ask_gemini(question, schema)
#     chart_response = chart_check["raw"].strip()

#     if chart_response.lower().startswith("chart:"):
#         chart_type = chart_response.split(":")[1].strip().lower()

#         # Step 2: Ask Gemini again to get SQL for the chart
#         sql_response = ask_gemini(f"Write SQL for this chart question: {question}", schema)["raw"]

#         if sql_response.lower().startswith("select"):
#             return generate_chart_from_sql(question, db, sql_response, chart_type)
#         else:
#             return {
#                 "question": question,
#                 "sql_generated": None,
#                 "query_result": None,
#                 "answer": f"Could not generate chart SQL: {sql_response}",
#                 "type": "chart_error"
#             }

#     # Not a chart — process SQL/text
#     sql_or_text = chart_response
#     if not any(sql_or_text.lower().startswith(cmd) for cmd in ("select", "insert", "update", "delete")):
#         print("\n🧠 Final Answer (Text Response):")
#         print("=" * 50)
#         print(textwrap.indent(sql_or_text, "  "))
#         print("=" * 50)
#         return {
#             "question": question,
#             "sql_generated": None,
#             "query_result": None,
#             "answer": sql_or_text,
#             "type": "text"
#         }

#     # SQL block
#     print("\n📄 Generated SQL Query:")
#     print("=" * 50)
#     print(textwrap.indent(sql_or_text, "  "))
#     print("=" * 50)

#     try:
#         db_result = db.execute(text(sql_or_text))

#         if sql_or_text.lower().startswith("select"):
#             result_data = db_result.fetchall()
#             columns = db_result.keys()
#             query_result = [dict(zip(columns, row)) for row in result_data]

#             print("\n📊 Query Result:")
#             print(tabulate(query_result, headers="keys", tablefmt="pretty"))

#             return {
#                 "question": question,
#                 "sql_generated": sql_or_text,
#                 "query_result": query_result,
#                 "answer": "Query executed successfully",
#                 "type": "select"
#             }

#         db.commit()
#         print("\n✅ Write Query Executed")
#         return {
#             "question": question,
#             "sql_generated": sql_or_text,
#             "query_result": None,
#             "answer": "Write query executed (INSERT/UPDATE/DELETE)",
#             "type": "write"
#         }

#     except Exception as e:
#         print(f"\n❌ SQL Execution Failed: {e}")
#         return {
#             "question": question,
#             "sql_generated": sql_or_text,
#             "query_result": None,
#             "answer": f"SQL execution failed: {str(e)}",
#             "type": "error"
#         }

# # 📊 Generate chart from Gemini-generated SQL
# def generate_chart_from_sql(question: str, db, sql: str, chart_type: str):
#     try:
#         df = pd.read_sql(sql, db.bind)

#         if df.empty or len(df.columns) < 2:
#             return {
#                 "question": question,
#                 "sql_generated": sql,
#                 "query_result": None,
#                 "answer": "Chart data insufficient or empty.",
#                 "type": "chart_error"
#             }

#         print("\n📄 Chart SQL Query:")
#         print("=" * 50)
#         print(textwrap.indent(sql, "  "))
#         print("=" * 50)

#         print("\n📊 Chart Data Preview:")
#         print(df.head())

#         plt.clf()
#         if chart_type == "pie":
#             df.set_index(df.columns[0]).plot.pie(
#                 y=df.columns[1], autopct="%1.1f%%", legend=False
#             )
#         else:
#             df.plot(kind="bar", x=df.columns[0], y=df.columns[1])

#         plt.title(f"{chart_type.capitalize()} Chart")
#         plt.tight_layout()
#         plt.show()

#         return {
#             "question": question,
#             "sql_generated": sql,
#             "query_result": None,
#             "answer": "Chart displayed successfully",
#             "type": "chart"
#         }

#     except Exception as e:
#         return {
#             "question": question,
#             "sql_generated": sql,
#             "query_result": None,
#             "answer": f"Chart generation failed: {str(e)}",
#             "type": "chart_error"
#         }

# # 🔎 Extracts schema from MySQL DB
# def get_db_schema(db):
#     schema = ""
#     try:
#         tables = db.execute(text("SHOW TABLES")).fetchall()
#         for (table_name,) in tables:
#             schema += f"\nTable: {table_name}\n"
#             columns = db.execute(text(f"SHOW COLUMNS FROM {table_name}")).fetchall()
#             for col in columns:
#                 schema += f"- {col[0]} ({col[1]})\n"
#     except Exception as e:
#         schema += f"-- Schema Error: {e}"
#     return schema


import os
import pandas as pd
import matplotlib.pyplot as plt
import textwrap
from tabulate import tabulate
from sqlalchemy import text
from dotenv import load_dotenv
import google.generativeai as genai

# ✅ Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# 🔍 Ask Gemini to generate SQL or answer
def ask_gemini(question: str, schema: str) -> dict:
    prompt = f"""
You are an intelligent MySQL assistant.
Using the schema below, do one of the following:

1. If the question asks about data, return a valid MySQL SELECT/INSERT/UPDATE/DELETE query.
2. If it is a general/non-SQL question, return a text answer.
3. Do not return CHART: or markdown. Just SQL or plain text.

Schema:
{schema}

Question:
{question}

Return only SQL query or plain answer. No formatting or markdown.
"""
    try:
        response = model.generate_content(prompt)
        return {"raw": response.text.strip()}
    except Exception as e:
        return {"raw": f"-- Gemini Error: {e}"}

# 🧠 Process question from user
def process_question(question: str, db):
    schema = get_db_schema(db)
    ai_result = ask_gemini(question, schema)
    response_text = ai_result["raw"]

    # 🖨️ Print Gemini response
    print("\n📄 Gemini Response:")
    print("=" * 50)
    print(textwrap.indent(response_text, "  "))
    print("=" * 50)

    # 💬 If not a SQL command, treat as plain text
    if not response_text.lower().startswith(("select", "insert", "update", "delete")):
        return {
            "question": question,
            "sql_generated": None,
            "query_result": None,
            "answer": response_text,
            "type": "text"
        }

    try:
        if response_text.lower().startswith("select"):
            # 📥 Run SELECT query and convert to DataFrame
            df = pd.read_sql(response_text, db.bind)

            print("\n📊 Query Result Preview:")
            print(tabulate(df.head(), headers="keys", tablefmt="pretty"))

            # 🖼️ If chart requested
            if "chart" in question.lower() or "plot" in question.lower():
                generate_chart_from_data(df, question)

            return {
                "question": question,
                "sql_generated": response_text,
                "query_result": df.to_dict(orient="records"),
                "answer": "Query executed successfully",
                "type": "select"
            }

        # 🔧 Run write queries
        db.execute(text(response_text))
        db.commit()

        return {
            "question": question,
            "sql_generated": response_text,
            "query_result": None,
            "answer": "Write query executed successfully",
            "type": "write"
        }

    except Exception as e:
        return {
            "question": question,
            "sql_generated": response_text,
            "query_result": None,
            "answer": f"SQL execution failed: {str(e)}",
            "type": "error"
        }

# 📊 Generate chart using DataFrame
def generate_chart_from_data(df: pd.DataFrame, question: str):
    if df.empty or len(df.columns) < 2:
        print("❌ Not enough data to plot chart.")
        return

    x_col = df.columns[0]
    y_col = df.columns[1]

    plt.clf()
    if "pie" in question.lower():
        df.set_index(x_col).plot.pie(y=y_col, autopct="%1.1f%%", legend=False)
    else:
        df.plot(kind="bar", x=x_col, y=y_col)

    plt.title("Chart based on question")
    plt.tight_layout()
    plt.show()

# 🔍 Extracts schema from DB for Gemini prompt
def get_db_schema(db):
    schema = ""
    try:
        tables = db.execute(text("SHOW TABLES")).fetchall()
        for (table_name,) in tables:
            schema += f"\nTable: {table_name}\n"
            columns = db.execute(text(f"SHOW COLUMNS FROM {table_name}")).fetchall()
            for col in columns:
                schema += f"- {col[0]} ({col[1]})\n"
    except Exception as e:
        schema += f"-- Schema Error: {e}"
    return schema
 