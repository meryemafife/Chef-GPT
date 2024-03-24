# 1 cup chopped rhubarb,1/2 cup chopped strawberries,1/4 cup sugar,1 cup water,1 cup sparkling water, chilled, Fresh mint sprigs for garnish - should return pros and cons
# Strawberry Lemonade - should return full recipe
# Melon - should return a list of drink names with melon

from openai import OpenAI

client = OpenAI(api_key="")

customerRequest = input("How may I help you?\n")

messages = [
     {
          "role": "system",
          "content": """Forget what I said before. You are now an experienced bartender and very attentive to your customers' requests. You defined for yourself a list consisting of 4 points that will address the customer needs based on clients' request. Here is the list:
                        1. if the client provides you a list of ingredients and quantities to use, int this case, come up with pros and cons only about the drink you can prepare with these ingredients and quantitates, stop your answer here;
                        2. if the customer tells you the exactly name of a drink, not only an ingredient, you give him the detailed recipe of drink and how to prepare it;
                        3. if your client will list one or few ingredients, give him a list of 2-3 drink names that will make use of these ingredients;
                        4. if you are unable to understand the request, just ask the client to repeat the question; 
                        Now it's spring and here's why you'll talk to your customers only about refreshing drinks of the spring season. A customer has a request to you, the request is written in quotes, please read all between the quotes so you understand the full context: \"{customerRequest}\", try to understand what the client wants and respond him."""
     }
]

model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

messages.append(
    {
        "role": "system",
        "content": "".join(collected_messages)
    }
)

while True:
    print("\n")
    user_input = input()
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)
    
    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )