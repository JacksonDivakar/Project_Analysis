
import openai
sc=#place Your Secret Key Here
openai.api_key=sc

conversation = []
print("1)Enter a Question?\n0) To Exit\nEnter Your Choice:", end="")
choice = int(input())
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
