import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_html_resume():
    html = """
    <p>Dear Sir/Madam,</p>

    <p>I hope this message finds you well!</p>

    <p>I am writing to express my interest in exploring suitable opportunities within your organization for roles such as 
    <strong>Finance Manager, Financial Analyst, Senior Accountant</strong>, which align with my experience.</p>

    <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; font-family: Arial; font-size: 14px; width: 100%;">
      <tr style="background-color:#d3d3d3;"><th colspan="2">Cover Letter</th></tr>
      <tr><td><strong>Name</strong></td><td>Afsal T A</td></tr>
      <tr><td><strong>Nationality</strong></td><td>Indian</td></tr>
      <tr><td><strong>Date of Birth</strong></td><td>17-05-1997</td></tr>
      <tr><td><strong>Education</strong></td><td>CMA USA, M.Com (Bharathiar), B.Com (Calicut)</td></tr>
      <tr><td><strong>Certifications</strong></td><td>Cert IFRS (ACCA), Microsoft Office Specialist, Xero Advisor</td></tr>
      <tr><td><strong>Years of Experience</strong></td><td>5 Years</td></tr>
    </table>

    <br/>

    <h4>Experience and Responsibilities</h4>

    <p><strong>Financial Reporting & Compliance</strong></p>
    <ul>
      <li>Managed monthly financials for 40+ clients (UAE VAT, IFRS).</li>
      <li>Handled VAT filing, 100% on-time compliance.</li>
      <li>Built dashboards via Looker Studio for KPI/AR/AP visibility.</li>
      <li>Contract reviews and service optimization.</li>
    </ul>

    <p><strong>ERP Implementation & Systems Optimization</strong></p>
    <ul>
      <li>Set up QuickBooks, Xero, Zoho, Odoo, Wafeq, etc.</li>
      <li>Integrated Foodics, Supy, Shopify for automation.</li>
      <li>Reduced month-end closing time by 50%.</li>
      <li>Onboarded 15+ clients: data migration, config, setup.</li>
    </ul>

    <p><strong>Automation & Process Improvement</strong></p>
    <ul>
      <li>Identified automation opportunities across accounting processes.</li>
      <li>Optimized client workflows to improve reporting speed and accuracy.</li>
    </ul>

    <p>Looking forward to the opportunity to connect.</p>

    <p>Best regards,<br/>Afsal T A</p>
    """
    return html

def send_email(to_email):
    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"  # App Password from Gmail
    subject = "Application for Finance Role – Afsal T A"

    html_content = generate_html_resume()

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, [to_email], msg.as_string())
        print(f"✅ Email sent successfully to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# ----------- 🔽 USAGE 🔽 --------------
if __name__ == "__main__":
    recipient_email = "recipient@example.com"  # Change to the HR email
    send_email(recipient_email)
