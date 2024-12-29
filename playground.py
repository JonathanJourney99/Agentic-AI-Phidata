from phi.agent import Agent
from dotenv import load_dotenv
import phi.api
from phi.model.groq import Groq
import os
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi
from phi.playground import Playground, serve_playground_app 
load_dotenv(override=True)

from financial_agent import *

phi.api = os.getenv("API_KEY")


app = Playground(agents=[finance_agent, web_agent]).get_app()
    
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True) 
