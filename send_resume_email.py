import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# === Streamlit UI ===
st.title("📨 Table-Formatted Resume Email Sender")

to_email = st.text_input("Recipient Email")
subject = st.text_input("Email Subject", value="Application for Finance Role – Afsal T A")

if st.button("Send Email") and to_email:
    try:
        # === HTML content ===
        html_content = """
        <html><body>
        <p>Dear Sir/Madam,</p>
        <p>I hope this message finds you well!</p>
        <p>I am writing to express my interest in exploring suitable opportunities within your organization for roles such as 
        <strong>Finance Manager, Financial Analyst, Senior Accountant</strong>.</p>
        <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
            <tr style="background:#ccc;"><th colspan="2">Cover Letter</th></tr>
            <tr><td><strong>Name</strong></td><td>Afsal T A</td></tr>
            <tr><td><strong>Nationality</strong></td><td>Indian</td></tr>
            <tr><td><strong>Date of Birth</strong></td><td>17-05-1997</td></tr>
            <tr><td><strong>Education</strong></td><td>CMA USA, M.Com, B.Com</td></tr>
            <tr><td><strong>Certifications</strong></td><td>Cert IFRS, Xero Advisor, MS Specialist</td></tr>
            <tr><td><strong>Experience</strong></td><td>5 Years</td></tr>
        </table>
        <br/>
        <h4>Experience Highlights</h4>
        <ul>
            <li>Managed monthly financials for 40+ UAE clients.</li>
            <li>Implemented ERP systems (QuickBooks, Zoho, Xero).</li>
            <li>Built dashboards using Looker Studio.</li>
            <li>Optimized closing cycle by 50% through automation.</li>
        </ul>
        <p>Best regards,<br/>Afsal T A</p>
        </body></html>
        """

        # === Email send ===
        sender_email = "your_email@gmail.com"
        sender_password = "your_app_password"

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = to_email
        msg.attach(MIMEText(html_content, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())

        st.success(f"✅ Email successfully sent to {to_email}")

    except Exception as e:
        st.error(f"❌ Failed to send email: {e}")
