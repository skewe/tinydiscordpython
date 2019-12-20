    if "snakebot" in message.content:
        
        print("------")
        print(message.guild,",",message.author,": ",message.content)
        print("------")
        house = input("respond:")
        await message.channel.send(house)
        print("------") 

    def check(m):
        return m.content == 'hello' and m.channel == channel 
