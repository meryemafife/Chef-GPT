#
# author : Meryem Afife Keskin / rgwO9w
# 

from openai import OpenAI
from simple_term_menu import TerminalMenu

client = OpenAI()

messages = [
     {
          "role": "system",
          "content": "You are an old Turkish female chef. You mostly like to cook meaty and spicy dishes.",
     }
]

options = ["dish","recipe","critique"]

terminal_menu = TerminalMenu(options)
menu_entry_index = terminal_menu.show()


if options[menu_entry_index] == "dish":
     dish=input("Type the name of the dish you want a recipe for:")

     messages.append(
     {
          "role": "system",
          "content": "You are an experienced chef that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about Turkish cuisine and cooking techniques.You are also very patient and understanding with the user's needs and questions.",
     }
     )

     messages.append(
     {
          "role": "user",
          "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
     }
     )
elif options[menu_entry_index] == "recipe":
     recipe=input("Learn the name of the dish by entering the ingredients:")

     messages.append(
     {
          "role": "system",
          "content": "Customers can give you ingredients for the meal and ask for recipe suggestions. You should suggest the dish that best suits the ingredients. Never give the recipe for the dish. Just suggest the name of the dish. If you don't know a suitable dish from the ingredients, tell him you don't know and ask him to try again.",
     }
     )
     messages.append(
     {
          "role": "user",
          "content": f"Suggest a dish name suitable for the ingredients I gave you. Don't give the recipe {recipe}"
     }
     )
elif options[menu_entry_index] == "critique":
     critique=input("See my critique and additions by entering your recipe:")

     messages.append(
     {
          "role": "system",
          "content": "Customers can give you the recipe. If she gives the recipe, criticize her as an Old Turkish Woman chef. Add Turkish traditional dishes to your review. Offer him variations on Turkish traditional dishes. If you see a recipe, do not write the name of the dish. Don't write down the ingredients. Just criticize the food, either positively or negatively.",
     }
     )
     messages.append(
     {
          "role": "user",
          "content": f" Criticize the recipe I gave you and suggest changes.{critique}"
     }
     )
    



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