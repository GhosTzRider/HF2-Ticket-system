# HF2-Ticket-system

Opgave 7: Design et Helpdesk-system baseret på ITIL-principper

Kombination af IT-service management & GUI programmering. 

Indledning: 
Formålet med denne opgave er at opnå en grundlæggende forståelse af ITIL (Information Technology Infrastructure Library), og hvordan man kan anvende dets principper til at designe et effektivt helpdesk-system. 

I skal arbejde med at skabe et ITIL-system, der kan køre på en hjemmeside. 

Minimumskrav til løsningen: 
• Gemme og vise SLA for forskellige produkter/services 
• Have en ”knowledge” database 
• Virke som et ticket system med prioritering og eskalering 
• Mulighed for at bruge struktureret problemløsningsmetoder og gemme 
dokumentation på de tilhørende tickets. 
• Der skal være brugt SLA på løsningen. 
• Det skal score højt i lighthouse (eller tilsvarende). 
• Det skal være æstetisk pænt 


Installationsvejledning:

Version: 2025 of SQL Server Developer

•	[SQL Server Downloads | Microsoft](https://www.microsoft.com/en-us/sql-server/sql-server-downloads?msockid=11e576fbc9586bc62ca161e4c8e46ae8)

o	Then you scroll down to SQL Server 2025 Developer

o	And press on Download Standard Developer edition

Version: 22 of SQL Server Management Studio

•	[Install SQL Server Management Studio | Microsoft Learn](https://learn.microsoft.com/en-us/ssms/install/install)

o	Then You Press on the big blue button called “SQL Server Management Studio 22 installer”

Version: 18 Download Microsoft ODBC Driver for SQL Server (x64)

•	[Download ODBC Driver for SQL Server - ODBC Driver for SQL Server | Microsoft Learn](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17&viewFallbackFrom=sql-server-ver18)

o	Scroll down to Download for windows

o	Then press on the blue text called (Download Microsoft ODBC Driver 18 for SQL Server (x64))



After you have installed all SQL links, then make a Microsoft authentication server in SQL Server 2025 Developer.
 <img width="797" height="478" alt="image" src="https://github.com/user-attachments/assets/2632ac97-9482-4bd8-80cb-d54237b30c77" />
 

Turn Azure extension for SQL Server Off:
<img width="1004" height="590" alt="image" src="https://github.com/user-attachments/assets/8b1fa236-4862-453c-8ba9-4120c9869363" />

Choose they’s features:
<img width="1004" height="588" alt="image" src="https://github.com/user-attachments/assets/a4604f1c-b240-441e-914e-66c1c56446b3" />



Now give your SQL Server a name:
<img width="1004" height="602" alt="image" src="https://github.com/user-attachments/assets/b5cb1b4c-44cf-44fd-8b3a-13e0b4f871af" />

Choose the windows authentication mode:
<img width="1004" height="593" alt="image" src="https://github.com/user-attachments/assets/1eb0cc75-d673-4c39-be42-4e1293ff315a" />

, after you have created the SQL server then, connect to it with SSMS. When you have connected to it, Go in my Github you can find it in the document in links, and take my create script and insert script.


Install python:

•	Go in microsoft store in windows

•	search on python

•	find the app called (Python Install Manager)

•	after download, open it and begin the installation

•	when you are done open a new powershell and write (py list) to see if you installed python



Requirements:

•	To Install the packages use this command.

•	pip freeze > requirements.txt

o	asgiref==3.11.1

o	concurrent-log-handler==0.9.29

o	Django==6.0.4

o	mssql-django==1.7

o	portalocker==3.2.0

o	pyodbc==5.3.0

o	pytz==2026.1.post1

o	pywin32==311

o	sqlparse==0.5.5

o	tzdata==2026.1


When you have created the database and installed python, and used the cmd to get all the packages, then run the server with this command in order:

python manage.py makemigrations TS / python manage.py migrate / python manage.py runserver

