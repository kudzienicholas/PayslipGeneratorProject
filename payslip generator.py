
import pandas as pd
from fpdf import FPDF
import yagmail
import os

# Load Excel File
df = pd.read_excel("employeepayslips.xlsx")

# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Validate Required Columns
expected_columns = ["Employees Id", "Name", "Email", "Basic Salary", "Allowance", "Deductions"]
for col in expected_columns:
    if col not in df.columns:
        raise KeyError(f"Column '{col}' is missing from the Excel file!")

# Calculate Net Salary
df["Net Salary"] = df["Basic Salary"] + df["Allowance"] - df["Deductions"]

# Email Credentials
SENDER_EMAIL = "kudziet221@gmail.com"
SENDER_PASSWORD = "yurevcdkvwzzeulj"  # Use a valid Gmail App Password

# Try connecting to Gmail SMTP using yagmail
try:
    yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)
    print("✅ Connected to Gmail SMTP server.")
except Exception as e:
    print(f"❌ Failed to connect to Gmail SMTP: {e}")
    exit()

# Define PDF class for payslips
class PayslipPDF(FPDF):
    def header(self):
        try:
            self.image("logo.png", 10, 8, 30)
        except:
            pass

        self.set_xy(45, 10)
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(30, 30, 30)
        self.cell(0, 8, "Manchester Cafe", ln=True)
        self.set_x(45)
        self.set_font("Helvetica", "", 11)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, "54 Babra Tredgold Circle, Mbare, Harare", ln=True)

        self.ln(10)
        self.set_draw_color(180, 180, 180)
        self.set_line_width(0.6)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(8)

    def footer(self):
        self.set_y(-20)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, "This is a system-generated payslip. For inquiries, contact HR.", 0, 0, "C")

    def generate_payslip(self, employee):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(50, 50, 50)
        self.cell(0, 10, f"Payslip for {employee['Name']}", ln=True)
        self.ln(4)

        self.set_font("Helvetica", "", 12)
        self.set_text_color(80, 80, 80)
        self.cell(40, 8, "Employee ID:", 0, 0)
        self.cell(60, 8, str(employee["Employees Id"]), 0, 1)
        self.cell(40, 8, "Email:", 0, 0)
        self.cell(60, 8, employee["Email"], 0, 1)
        self.ln(6)

        self.set_fill_color(220, 235, 250)
        self.set_draw_color(180, 180, 180)
        self.set_text_color(0, 0, 0)
        self.set_font("Helvetica", "B", 12)
        self.cell(95, 10, "Earnings", 1, 0, "C", True)
        self.cell(95, 10, "Deductions", 1, 1, "C", True)

        self.set_font("Helvetica", "", 12)
        self.set_fill_color(245, 245, 245)
        self.cell(95, 10, f"Basic Salary: ${employee['Basic Salary']:.2f}", 1, 0, "L", True)
        self.cell(95, 10, f"Deductions: ${employee['Deductions']:.2f}", 1, 1, "L", True)
        self.cell(95, 10, f"Allowance: ${employee['Allowance']:.2f}", 1, 0, "L", True)
        self.cell(95, 10, "", 1, 1, "L", True)

        self.set_font("Helvetica", "B", 12)
        self.set_text_color(255, 255, 255)
        self.set_fill_color(50, 150, 90)
        self.cell(190, 12, f"Net Salary: ${employee['Net Salary']:.2f}", 0, 1, "C", True)
        self.ln(10)

        self.set_font("Helvetica", "I", 11)
        self.set_text_color(70, 70, 70)
        self.multi_cell(0, 8, "Thank you for your contribution. We appreciate your continued efforts as part of the Manchester Cafe team.")

# Target folder path for PDFs
save_path = r"C:\Users\uncommonStudent\OneDrive\Desktop\PYTHON\Payslips"

# Create the folder if it doesn't exist
os.makedirs(save_path, exist_ok=True)

# Generate and send payslips
for _, row in df.iterrows():
    try:
        pdf = PayslipPDF()
        pdf.add_page()
        pdf.generate_payslip(row)
        filename = f"{row['Employees Id']}_payslip.pdf"
        full_path = os.path.join(save_path, filename)
        pdf.output(full_path)

        print(f"📤 Sending to {row['Email']}...")

        yag.send(
            to=row["Email"],
            subject="Your Monthly Payslip",
            contents=f"Dear {row['Name']},\n\nPlease find your payslip attached.\n\nBest regards,\nYour Company",
            attachments=full_path
        )
        print(f"✅ Sent to {row['Email']}")

    except Exception as e:
        print(f"❌ Failed to send to {row['Email']}: {e}")

print("🏁 All payslips sent!")