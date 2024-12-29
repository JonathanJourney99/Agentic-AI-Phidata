from phi.agent import Agent
from dotenv import load_dotenv
from phi.model.groq import Groq
import os
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo


load_dotenv(override=True)


web_agent = Agent(
    name="Web Agent",
    role="Search the web",  
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview", api_key=os.getenv("GROQ_API_KEY")),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview", api_key=os.getenv("GROQ_API_KEY")),
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

dum_agent = Agent(
    name="Statistical Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview", api_key=os.getenv("GROQ_API_KEY")),
    description="Your are a dummy agent.",
    show_tool_calls=True,
    markdown=True,
)      


agent_team = Agent(
    team=[web_agent, finance_agent, dum_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response(f""" 
    Think step by step and evaluate the stock using different pricing models and compare the outcomes, to provide a good recommendation about buy, sell, hold. Also provide outcome values and other useful metrics, ratios.
    
    1. **Discounted Cash Flow (DCF) Analysis**: This involves estimating the present value of a company's future cash flows.
    
    2. **Price-to-Earnings (P/E) Ratio**: A comparison of the company's current share price to its per-share earnings.
    
    3. **Dividend Discount Model (DDM)**: Used for companies that pay dividends, estimating the present value of all future dividend payments.
    
    4. **Relative Valuation (Comparables)**: Comparing the stock's multiples to its industry peers.
    
    Perform the calculations and show whether to buy for a particular company IDFCFIRSTB.NS and show the calculations.
    """, stream=True)
