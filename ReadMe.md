# 🧾 Employee Payslip Generator & Email Sender

This Python project automates the process of generating professional payslip PDFs for employees and sending them directly to their email addresses. The script reads employee data from an Excel file, calculates the net salary, creates a printable payslip using the `fpdf` library, and sends the payslip via Gmail using `yagmail`.

---

## 📁 Project Structure

The project directory contains the following files and folders:
- `employeepayslips2.xlsx`: Excel file with employee details.
- `logo.png`: Optional company logo to appear on payslips.
- `generate_payslips.py`: Main Python script for generating and sending payslips.
- `README.md`: Documentation for the project.
- `/Payslips`: Folder where generated PDF payslips are saved.

---

## ✅ Features

- Generate customized PDF payslips for each employee.
- Automatically calculate net salary.
- Send payslips to employee emails via Gmail.
- Organize all PDF files in a designated folder.
- Optional company branding with logo and address.

---

## 🔧 Requirements & Installation

### 1. **Python 3.7+**

### 2. Required Libraries

To install the required Python libraries, run:

```bash
pip install pandas fpdf yagmail openpyxl
```

### 3. 📂 Excel File Format

Ensure your Excel file (`employeepayslips2.xlsx`) has the following columns:
- Employee Id
- Name
- Email
- Basic Salary
- Allowance
- Deductions

Example:

| Employee Id | Name        | Email               | Basic Salary | Allowance | Deductions |
|-------------|-------------|---------------------|--------------|-----------|------------|
| 1001        | John Doe    | john@example.com     | 1000         | 200       | 150        |

**Note:** Ensure column headers are correct and there are no extra spaces. The values for Basic Salary, Allowance, and Deductions should be numerical.

### 4. 📤 Gmail Setup

To send emails using Gmail:
- Enable 2-Step Verification on your Google account.
- Generate an App Password by going to your Google Account > Security > App Passwords > Generate one for "Mail."
- Replace the credentials in the script:

```python
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_generated_app_password"
```

---

## 🧾 Output

All PDF payslips will be saved in the `/Payslips` folder, with each file named in the format `EmployeeID_payslip.pdf`.

---

## 🚀 How to Run the Project

1. Place your Excel file and logo (optional) in the same directory as the script.
2. Open the terminal or command prompt.
3. Navigate to the project folder and run:

```bash
python generate_payslips.py
```

Logs will appear in the console for each email processed and sent.

---

## 🛠️ How It Works

1. **Data Loading**: The script reads employee data from the Excel file, removing unnecessary whitespace from column headers.
2. **Validation**: The script checks that all expected columns are present.
3. **Calculation**: It calculates the net salary as:  
   **Net Salary = Basic Salary + Allowance - Deductions**
4. **Payslip Generation**: The script uses `fpdf` to generate personalized PDF payslips.
5. **Storage**: The generated PDFs are saved in the specified target directory, which is created if it doesn't exist.
6. **Email Sending**: The payslip is sent as an attachment using `yagmail` with Gmail’s SMTP server.

---

## 🧪 Example Console Output

```
✅ Connected to Gmail SMTP server.
📤 Sending to john.doe@example.com...
✅ Sent to john.doe@example.com
📤 Sending to jane.smith@example.com...
✅ Sent to jane.smith@example.com
🏁 All payslips sent!
```

---

## ⚠️ Troubleshooting

| Problem                   | Solution                                            |
|---------------------------|-----------------------------------------------------|
| SMTP authentication error | Ensure App Password is correct and 2FA is enabled. |
| Missing columns           | Check Excel headers for typos or extra spaces.     |
| Email not received        | Check the spam folder or verify the email address. |
| File not found            | Confirm `employeepayslips2.xlsx` is in the same folder. |

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🤝 Contributions

Feel free to fork the project and submit pull requests. Feedback and improvements are always welcome!

---

## 👨‍💼 Developed By

Your Name / Company  
📧 kudziet221@gmail.com

