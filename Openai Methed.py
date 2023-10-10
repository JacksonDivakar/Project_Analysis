import openai


sc="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"
openai.api_key=sc
data1="""(Computer Science Engineering(CSE)Department)NAME OF THE FACULTY-DESIGNATION 
DR. SANGEETHA M-Professor
DR. SUMITHIRADEVI C-Associate Prof
DR. BARANITHARAN K-Associate Prof
DR. KARTHI S-Assistant Professor
MR. ARIVARASAN S-Assistant Professor
MR. GUNASEKARAN S-Associate Prof
MRS. NANDHINI DEVI S-Assistant Professor
MS. SHOBANA M-Assistant Professor
MR. VASUDEVAN M-Assistant Professor
MR. ANBUMANI P-Assistant Professor
MRS. THARANI B-Assistant Professor
MRS. GEETHA S-Assistant Professor
MRS. LATHA P-Assistant Professor
MRS. ABIRAMI S-Assistant Professor
MR. SENTHIL KUMAR K-Assistant Professor
MRS. ABIRAMI M-Assistant Professor
MR. MANI P-Assistant Professor
MS. PRIYA M-Assistant Professor
MR. PRABAKARAN S-Assistant Professor
MR. RANJITH G-Assistant Professor
MR. MARIKUMAR B-Assistant Professor
MR. MOHAN S-Assistant Professor
MR. SRINATH YADAV K-Assistant Professor
MR. PALRAJ R-Assistant Professor
MR. MANIKANDAN T-Assistant Professor
MRS.NAGALAKSHMI-Assistant Professor
Mr.R.PALRAJ-Assistant Professor
MR. JAISHANKAR V-Assistant Professor"""
data2="""(Artificial Intellegence and data science(AIDS) Department)NAME OF THE FACULTY-DESIGNATION
MRS. KAVITHA V-Head of the Department(HOD)
M.KARTHIKEYAN-Assistant Professor
BHAVADHARANI K-Assistant Professor
"""
data3="""(Information Technology(IT) Department)NAME OF THE FACULTY-DESIGNATION
DR. AROCKIA MARRY P-Professor
DR. PARTHIBAN M-Associate Prof
MR. KUMARAN R-Associate Prof
MR. MANOJSAGAR K-Assistant Professor
MR. NELSON S-Assistant Professor
MR. VENGAIMARBHAN D-Assistant Professor
MR. MOHAN PERIYASAMY M-Assistant Professor
MR. MANIVANNAN K-Assistant Professor
MS. PREMA LATHA N-Assistant Professor
MRS. MAALINI D-Assistant Professor
MR. MOHAMED KEERAN V-Assistant Professor
MRS. NANDHINI I-Assistant Professor
MRS. SAHEBZATHI S-Assistant Professor
MS. NITHYA A-Assistant Professor
MR. ARIVOLI R-Assistant Professor
MR. FRANKLIN JINO R E-Assistant Professor
MRS. RAJESWARI S-Assistant Professor
MS. SARANYA R-Assistant Professor
MRS. MENAGA G-Assistant Professor
MR. PRAVEEN KUMAR G-Assistant Professor
MRS. REVATHI S-Assistant Professor
MRS. KAVYA PRIYA J-Assistant Professor
MR. SATHYANARAYANAN M-Assistant Professor
B.SRINIVAS-Assistant Professor
"""
data4="""Recruiters: ["Tata Consultancy Services","CAPGEMINI","Cognizant Technologies Solutions","WIPRO","GO SPEEDY GO","ARICENT","IBM","LTI","QUEST GLOBAL","NTT DATA","Mind tree","EXCELACOM","SONY INDIA","AMPHISOFT","VURAM","Sanmar","Tessolve","Mallow Technologies","MOBIVEIL","BYJUS","ZOHO","MBIT WIRELESS"]"""
data5="""Facilities:- Language Laboratory- Auditorium- Green Practices:- Green initiatives- Rainwater harvesting structure- Water Management- Sanitation- A Smart Classroom"""
data6="""
**Hostels:**- Separate hostels for boys and girls.- Tidy rooms and hygienic facilities.- Recreation hall, multi-gym, and indoor games.- Everyday conveniences: WI-FI, telephones, and weekly movies.- Hygienic mess facilities with steam cookers.- Mineral water plant and RO facility on campus.
**Bus:**- Various bus routes and timings for transportation.
**Canteen:**- Provides a variety of food at nominal rates.
**Medical, ATM & Insurance:**- 24X7 medical facilities, Dispensary, and ambulance.- Axis Bank ATM on campus.- Group insurance scheme for students and staff.
**Library Resources:**- Books: 41,909- E-Books: 8,325- Print Journals: 72- E-Journals: 1,997- Back Volumes: 3,005- Project Reports: 1,004- CD Collections: 2,798- NPTEL: 184- Question Bank: 91- Newspapers: 9- Established in 2002.- 20 Computer systems in Digital Library.- Collection of more than 40,000 volumes.- IP-based Video Surveillance.- Conducted a One Day National Conference in Digital Resource Initiatives in Libraries (DRIL).
**Library Vision and Mission:**- Vision: To be one of the best Engineering College Libraries globally.- Mission: Incorporate technology, offer comprehensive knowledge services."""
data7="""V.S.B. Educational Trust was founded in the year 2000 by Mr. V.S. Balsamy, the founder and correspondent of the V.S.B. Engineering College, with an interest in promoting, managing and administrating educational institutions with high academic standards, discipline and to take up and help other allied activities in the field of education. Under the Trust, V.S.B. Engineering College,Karur was established in the year 2002 and V.S.B College of Engineering Technical Campus,Coimbatore in the year 2012.The college principal name is Dr.Nimal Kannan.The Vice principal is Dr.kirubaSankar.College located in karudayampalayam,karur,Tamil Nadu,india""" 
data8="""there are 14 Departments and they are -Artificial Intelligence and Data Science-Bio-Technology-Biomedical Engineering-Chemical Engineering-Civil Engineering-Computer Science and Engineering-Computer Science and Business System-Artificial Intelligence and Machine Learning-Computer and Communication Engineering-Electrical and Electronics Engineering-Electronics and Communication Engineering-Information Technology-Mechanical Engineering-Science and Humanities"""
list1=[data1,data2,data3,data4,data5,data6,data7]
print("1)Enter a Question?\n0) To Exit\nEnter Your Choice:", end="")

choice = int(input())
conversation=[]
for i in list1:
    conversation.append({"role": "user", "content": i})
prompt="Now onwards consider the given data as your knowledge and only answer with the given data only and the another constraint is the details are about V.S.B Engineering College +\n"
conversation.append({"role": "user", "content": prompt})
while True:
    
    

    if choice == "exit" or choice==0:
        break
    else:
        user_input = input("Ask: ")
        conversation.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        assistant_reply = response["choices"][0]["message"]["content"]
        print("Assistant's reply: ", assistant_reply+"""\nEnter 'exit' to end or to continue 'Hit enter again'.""")

        conversation.append({"role": "assistant", "content": assistant_reply + "\n"})
        choice=input().lower()
print("Program Ended")