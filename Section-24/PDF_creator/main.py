import streamlit as st
from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")
pg = 0
for index, row in df.iterrows():
    #print (index, row, "\n")
    #print (f"Index is {index}\n")
    #print (f"Row is {row}\n")
    #mypage =index + 1
    for i in range(row["Pages"]):
        #print (i)
        #mypage = mypage + 1
        pg = pg + 1

        print(pg)
        pdf.add_page()
        pdf.set_font(family="Helvetica", style="B", size=12)
        #pdf.cell (w=0, h=12, txt="Helllo There!", align="L", ln=1, border=1)
        #pdf.set_font(family="Courier", style="B", size=12)
        pdf.set_text_color(255,255,255)
        pdf.set_fill_color(0, 0, 66)
        pdf.cell (w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0, fill=True)
        pdf.line(10,22,200,22)
        
        pdf.set_font(family="Times", style="I", size=12)
        pdf.ln(250)
        pdf.set_text_color(255,255,255)
        pdf.cell (w=0, h=7, txt=row["Topic"], align="L", ln=1, border=0, fill=True)        
        page_number = f"Page-{pg}"
        pdf.cell (w=0, h=8, txt=str(page_number), align="R", ln=1, border=0, fill=True)

pdf.output("Output.pdf")

'''
with open("topics.csv", "r") as file:
    content = file.read()
    print(content)
'''


print(type(pdf))

