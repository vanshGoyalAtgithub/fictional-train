from uagents import Agent
 
alice = Agent(name="alice", seed="alice recovery phrase")
 
print("Fetch network address: ", alice.wallet.address())
#Fetch network address:  fetch1454hu0n9eszzg8p7mvan3ep7484jxl5mkf9phg