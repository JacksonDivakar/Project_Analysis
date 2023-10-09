step100="""Step,Title,Content
1,Introduction to V.S.B. Engineering College,"V.S.B. Engineering College is a premier educational institution located in Karur, Tamil Nadu, India. Established in 2002, the college is committed to providing quality education in the field of engineering and technology. With a strong focus on academic excellence, V.S.B. Engineering College has earned a reputation for producing skilled engineers who contribute to the nation's development."
2,Academic Programs at V.S.B. Engineering College,"V.S.B. Engineering College offers a wide range of academic programs to cater to the diverse interests and career goals of its students. The college provides undergraduate and postgraduate courses in various engineering disciplines. These programs are designed to provide students with a strong foundation in engineering and technology."
3,Departments at V.S.B. Engineering College,"V.S.B. Engineering College has several departments, each specializing in a specific area of engineering and technology. The key departments include:
- Computer Science and Engineering (CSE)
- Electronics and Communication Engineering (ECE)
- Electrical and Electronics Engineering (EEE)
- Mechanical Engineering (ME)
- Information Technology (IT)
- Civil Engineering (CE)
- Master of Business Administration (MBA)
- Master of Computer Applications (MCA)"
4,Library Services at V.S.B. Engineering College,"The college library is a valuable resource for students and faculty. It houses a vast collection of books, journals, and digital resources to support academic and research needs. The library offers services such as book lending, reference assistance, and access to online databases and e-journals."
5,Alumni Association at V.S.B. Engineering College,"The Alumni Association at V.S.B. Engineering College plays a crucial role in maintaining strong connections with former students and involving them in the growth and development of the institution. It serves as a bridge between the college, its current students, and alumni, fostering a sense of community and support."
6,Campus Facilities at V.S.B. Engineering College,"V.S.B. Engineering College offers a range of campus facilities to ensure a conducive environment for learning, growth, and overall well-being of students and staff. These facilities contribute to the college's commitment to providing a holistic educational experience."
7,Transportation Services at V.S.B. Engineering College,"V.S.B. Engineering College provides transportation services to ensure that students and staff have convenient and reliable commuting options. These services help in facilitating easy access to the college from various locations."
8,Canteen Facilities at V.S.B. Engineering College,"V.S.B. Engineering College offers well-maintained canteen facilities to cater to the nutritional needs of students and staff. The college canteen is an essential part of campus life, providing a variety of food options to suit different tastes and preferences."
9,Medical, ATM & Insurance Facilities at V.S.B. Engineering College,"V.S.B. Engineering College prioritizes the well-being and convenience of its students and staff by offering various essential facilities related to health, banking, and insurance. Here's a detailed overview of these facilities:"
10,Alumni Association Structure at V.S.B. Engineering College (2018-2019),"The Alumni Association operates with a structured framework that includes the following roles and responsibilities:"
11,College Canteen at V.S.B. Engineering College,"At V.S.B. Engineering College, the college canteen is a vital component of campus life, offering students and staff a variety of delicious food options. In this section, we explore the features and facilities of the college canteen, highlighting its role in nourishing the college community:"
12,Medical Facilities, ATM, and Insurance at V.S.B. Engineering College,"In this section, we will delve into the medical facilities, ATM services, and insurance provisions available at V.S.B. Engineering College, emphasizing the importance of health and financial services for the college community:"
13,Alumni Association Overview at V.S.B. Engineering College,"In this section, we'll explore the Alumni Association at V.S.B. Engineering College and its significant role in connecting alumni, students, faculty, and the institution itself:"
14,Library Resources at V.S.B. Engineering College,"The college library is a valuable resource for students and faculty. It houses a vast collection of books, journals, and digital resources to support academic and research needs. The library offers services such as book lending, reference assistance, and access to online databases and e-journals."""



list1=[step100]
import openai


sc="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"
openai.api_key=sc


print("1)Enter a Question?\n0) To Exit\nEnter Your Choice:", end="")

choice = int(input())
conversation=[]
for i in list1:
    conversation.append({"role": "user", "content": i})
prompt="Now onwards consider the given data as your knowledge and only answer with the given data only+\n"
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
