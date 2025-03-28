import os
import openai
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Web Search Agent
web_search_agent = Agent(name= 'web search agent',
                         role= 'Search the web for latest information',
                         model= Groq(id="deepseek-r1-distill-llama-70b"),
                         tools= [DuckDuckGo()],
                         instructions= ["Always include sources"],
                         show_tool_calls=True,
                         markdown= True,   # Answer should be in Markdown format
                         ) 

# Finance Agent
finance_agent = Agent(name= 'Financial Agent',
                      role= "Gather financial data about the company",
                      model= Groq(id="deepseek-r1-distill-llama-70b"),
                      tools= [YFinanceTools(stock_price=True, analyst_recommendations=True,
                                            stock_fundamentals=True, company_news=True)],
                      instructions= ["Use tables to display the data"],
                      show_tool_calls= True,
                      markdown= True, 
                    )                  
        
multi_ai_agents = Agent(team =[web_search_agent, finance_agent],
                        instructions= ["Always include sources", "Use tables to display the data"],
                        show_tool_calls= True,
                        markdown= True,
                        )

multi_ai_agents.print_response("Summarize the analyst recommandation and share latest news about NVDE", stream=True)


