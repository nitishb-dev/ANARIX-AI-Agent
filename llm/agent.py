import os
import pandas as pd
import matplotlib.pyplot as plt
import textwrap
from tabulate import tabulate
from sqlalchemy import text
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_gemini(question: str, schema: str) -> dict:
    prompt = f"""
You are an intelligent MySQL assistant.
Using the schema below, do one of the following:

1. If the question asks for a chart, visualization, or plot, generate a valid MySQL SELECT query that returns the necessary data for plotting (e.g., categories and values).
2. If the question asks about data, return a valid MySQL SELECT/INSERT/UPDATE/DELETE query.
3. If it is a general/non-SQL question, return a text answer.
4. Do not return CHART: or markdown. Just SQL or plain text.

Schema:
{schema}

Question:
{question}

Return only SQL query or plain answer. No formatting or markdown.
If the question mentions chart, bar chart, pie chart, or plot, always return a SQL query for the relevant data.
"""
    try:
        response = model.generate_content(prompt)
        return {"raw": response.text.strip()}
    except Exception as e:
        return {"raw": f"-- Gemini Error: {e}"}

def infer_chart_type(df: pd.DataFrame) -> str or None:
    if df.empty or len(df.columns) < 2:
        return None
    if pd.api.types.is_numeric_dtype(df[df.columns[1]]):
        return "pie" if len(df) <= 10 else "bar"
    return None

def generate_chart_from_dataframe(df: pd.DataFrame, chart_type: str = "bar", chart_path="assets/screenshots/chart.png"):
    if df.empty:
        print("❌ Not enough data to plot chart.")
        return None

    plt.clf()
    # Two-column chart with many x values
    if len(df.columns) >= 2:
        x_col = df.columns[0]
        y_col = df.columns[1]
        df_sorted = df.sort_values(by=y_col, ascending=False)
        top_n = 20  # Show only top 20 items for clarity
        df_plot = df_sorted.head(top_n)
        plt.figure(figsize=(12, 6))
        bars = plt.bar(df_plot[x_col].astype(str), df_plot[y_col], color='#4A90E2', edgecolor='black')
        plt.title(f"Bar Chart of {y_col} by {x_col}", fontsize=14)
        plt.xlabel(x_col, fontsize=12)
        plt.ylabel(y_col, fontsize=12)
        plt.xticks(rotation=45, fontsize=10)
        # Add value labels above each bar
        for bar, value in zip(bars, df_plot[y_col]):
            plt.text(bar.get_x() + bar.get_width()/2, value, f"{value:,.0f}", ha='center', va='bottom', fontsize=9, color='black')
        plt.tight_layout()
        plt.savefig(chart_path)
        return chart_path
    # Single-value chart
    elif len(df.columns) == 1 and len(df) == 1:
        value = df.iloc[0, 0]
        label = df.columns[0]
        plt.bar([label], [value], width=0.4, color='#4A90E2', edgecolor='black')
        plt.title(f"{label} Value", fontsize=14)
        plt.xlabel(label, fontsize=12)
        plt.ylabel(label, fontsize=12)
        plt.ylim(0, value * 1.2)
        plt.text(label, value, f"{value:,.2f}", ha='center', va='bottom', fontsize=13, color='black', fontweight='bold')
        plt.tight_layout()
        plt.savefig(chart_path)
        return chart_path

def process_question(question: str, db):
    schema = get_db_schema(db)
    ai_result = ask_gemini(question, schema)
    response_text = ai_result["raw"]

    print("\n📄 Gemini Response:")
    print("=" * 50)
    print(textwrap.indent(response_text, "  "))
    print("=" * 50)

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
            df = pd.read_sql(response_text, db.bind)
            print("\n📊 Query Result Preview:")
            print(tabulate(df.head(), headers="keys", tablefmt="pretty"))

            if "chart" in question.lower() or "bar chart" in question.lower():
                chart_path = generate_chart_from_dataframe(df, "bar")
            else:
                chart_type = infer_chart_type(df)
                chart_path = generate_chart_from_dataframe(df, chart_type or "bar")

            return {
                "question": question,
                "sql_generated": response_text,
                "query_result": df.to_dict(orient="records"),
                "answer": "Query executed successfully with chart",
                "chart_path": chart_path,
                "type": "select"
            }

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