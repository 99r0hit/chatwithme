import openai

# Set up your OpenAI API key
openai.api_key = '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'

def gpt_chatbot(prompt):
    try:
        # Call the GPT-4 API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Welcome to the GPT Chatbot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Get the response from GPT
        response = gpt_chatbot(user_input)
        print(f"ChatGPT: {response}")

if __name__ == '__main__':
    main()
