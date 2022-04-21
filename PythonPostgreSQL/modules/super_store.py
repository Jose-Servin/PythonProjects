import psycopg2
from openpyxl import Workbook
from super_store_functions import create_connection
from constants import (
    REPORT_ONE_QUERY, REPORT_TWO_QUERY, REPORT_THREE_SHEET_ONE_QUERY, REPORT_THREE_SHEET_TWO_QUERY,
    REPORT_FOUR_SHEET_ONE_QUERY, REPORT_FOUR_SHEET_TWO_QUERY, REPORT_FOUR_SHEET_THREE_QUERY)
import pandas as pd


def script_function():
    conn = create_connection()

    # query database and save results to dataframe object
    report_one = pd.read_sql(REPORT_ONE_QUERY, con=conn, index_col=None)
    report_two = pd.read_sql(REPORT_TWO_QUERY, con=conn, index_col=None)
    report_three_one = pd.read_sql(REPORT_THREE_SHEET_ONE_QUERY, con=conn, index_col=None)
    report_three_two = pd.read_sql(REPORT_THREE_SHEET_TWO_QUERY, con=conn, index_col=None)
    report_four_one = pd.read_sql(REPORT_FOUR_SHEET_ONE_QUERY, con=conn, index_col=None)
    report_four_two = pd.read_sql(REPORT_FOUR_SHEET_TWO_QUERY, con=conn, index_col=None)
    report_four_three = pd.read_sql(REPORT_FOUR_SHEET_THREE_QUERY, con=conn, index_col=None)

    # create xlsx file for reports and write query results to them
    with pd.ExcelWriter('../Reports/Master_Report.xlsx') as writer:
        report_one.to_excel(writer, sheet_name='Profitable_Region')
        report_two.to_excel(writer, sheet_name="State vs Volume")
        report_three_one.to_excel(writer, sheet_name="Profitable State")
        report_three_two.to_excel(writer, sheet_name="Top 10 pct City States")
        report_four_one.to_excel(writer, sheet_name="Profitable Product per State")
        report_four_two.to_excel(writer, sheet_name="Sum of profit")
        report_four_three.to_excel(writer, sheet_name="Running sum of profit")


if __name__ == "__main__":
    script_function()
