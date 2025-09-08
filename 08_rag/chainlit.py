import chainlit as cl
from query import rag_chain

@cl.on_chat_start
async def on_chat_start():
    logo = cl.Image(name="logo", display="inline", url="https://codelabs.cs.pdx.edu/images/pdx-cs-logo.png")
    await cl.Message(content="", elements=[logo]).send()

    welcome_text = (
        "**Welcome to the Portland State CS Chatbot!**\n\n"
        "Ask me anything about the CS program, courses, or resources at PSU.\n\n"
    )
    await cl.Message(content=welcome_text).send()

@cl.on_message
async def on_message(message: cl.Message):
    user_query = message.content
    answer = rag_chain.invoke(user_query)
    await cl.Message(content=answer).send()

if __name__ == "__main__":
    cl.run()

