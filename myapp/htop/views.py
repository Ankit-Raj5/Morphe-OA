from django.shortcuts import HttpResponse
import os
import getpass
from datetime import datetime
import pytz
import subprocess

def htop_view(request):
    name = "Ankit Rajpoot"  
    username = getpass.getuser() 

   
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')

    try:
        top_output = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True).stdout
    except Exception as e:
        top_output = f"Error fetching 'top' output: {str(e)}"

    html_content = f"""
    <h1>System Info</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {ist_time}</p>
    <pre>{top_output}</pre>
    """
    return HttpResponse(html_content)