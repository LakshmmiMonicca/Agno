from my_gemma import Gemma

from agno.models.google import Gemini



from agno.agent import Agent

from dotenv import load_dotenv

import agno.tools



from youtube_tool import youtube_tool

from google_tool import google_search

import os

os.environ["GEMINI_API_KEY"] = "AIzaSyCAXNjm86lwT2OdYTg1BOdFGgx0w7m0lNE"



load_dotenv()



print("Loaded Gemini Key:", os.getenv("GEMINI_API_KEY"))



agent = Agent(model=Gemma())   # ✅ Instance, not class

model = Gemma()

print("Type of model being passed to Agent:", type(model))



agent = Agent(model=model)





agent = Agent(

    model=Gemini(id="gemini-2.0-flash", grounding=True),

    show_tool_calls=True,

    markdown=True,

)





agent.print_response("How are you?")



Youtube_agent = Agent(

    

    model=Gemini(id="gemini-2.0-flash", grounding=True),  # or Gemini()

    tools=[youtube_tool],

    show_tool_calls=True,

    description="You are a YouTube agent. Summarize YouTube videos and provide channel info."

)





Youtube_agent.print_response("Summarize this video https://youtu.be/ONMftqeKZRE?si=7KcALk8QFqlajizh and provide recently posted video from the channel", markdown=True)



web_agent = Agent(

    model=Gemini(id="gemini-2.0-flash", grounding=True),

    tools=[google_search],

    description="You are a news agent that helps users find the latest news.",

    instructions=[

        "Given the channel name by the user, provide latest information about the channel.",

        "Search for 10 news items and select the top 4 unique items.",

        "Search in English and in Tamil.",

    ],

    show_tool_calls=True,

    #debug_mode=True,

)

agent.print_response("Karthik's Show", markdown=True)



team_Agents = Agent(

    model=Gemini(id="gemini-2.0-flash", grounding=True),

    team=[Youtube_agent, web_agent],

    instructions=["Summarise the video based on the URL provided by the user and gather latest information about the channel"],

    show_tool_calls=True,

)



team_Agents.print_response("Summarize this video https://youtu.be/ONMftqeKZRE?si=7KcALk8QFqlajizh and provide latest information about Karthik's Show channel")

