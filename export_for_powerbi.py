import sqlite3
import pandas as pd
from datetime import datetime

# Connect to database
conn = sqlite3.connect('db.sqlite3')

# Query appointments with patient details
query = """
SELECT 
    a.id as appointment_id,
    a.appointment_date,
    a.appointment_time,
    a.department,
    a.status,
    a.risk_score,
    a.lead_time_days,
    a.booking_date,
    p.id as patient_id,
    p.prior_no_shows,
    p.previous_visits,
    p.sms_opt_in,
    u.username,
    u.first_name || ' ' || u.last_name as patient_name,
    d.specialization as doctor_specialization,
    du.first_name || ' ' || du.last_name as doctor_name
FROM appointments_appointment a
JOIN accounts_patientprofile p ON a.patient_id = p.id
JOIN auth_user u ON p.user_id = u.id
LEFT JOIN accounts_doctorprofile d ON a.doctor_id = d.id
LEFT JOIN auth_user du ON d.user_id = du.id
"""

df = pd.read_sql_query(query, conn)

# Add derived columns for Power BI
df['appointment_date'] = pd.to_datetime(df['appointment_date'])
df['month'] = df['appointment_date'].dt.month_name()
df['day_name'] = df['appointment_date'].dt.day_name()
df['week_number'] = df['appointment_date'].dt.isocalendar().week
df['risk_category'] = pd.cut(df['risk_score'], 
                               bins=[0, 30, 50, 70, 100], 
                               labels=['Low', 'Medium', 'High', 'Very High'])

# Save to CSV
df.to_csv('appointments_export.csv', index=False)
print(f"✅ Exported {len(df)} appointments to appointments_export.csv")
print("\n📊 Ready to import into Power BI!")