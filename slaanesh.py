from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
 
class Message(Model):
    message: str
 
slaanesh = Agent(
    name="slaanesh",
    port=8001,
    seed="slaanesh secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)
 
fund_agent_if_low(slaanesh.wallet.address())