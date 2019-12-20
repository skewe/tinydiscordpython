@client.event
async def on_message(message):
    if message.content == "generate a sentence": 
        word1 = ["hello","No","Yes","Maybe","kk","yas","hmm"]
        word2 = ["I'll","I","...","I guess","okay","I dont know"]
        word3 = ["nevermind","lmao","my","your"]
        word4 = [", but nah","...","I'll try"]
        word5 = ["..hehe","hhh","ill stop",":(","...","im just sad"]
        nouns = ["dog","cat","rabbit","game","phone","nintendo","house","pencil"]
        goonnouns = ["sofa","computer","chair","comfortable chair","nes","gameboy","iphone","android","apple phone","ds","ds lite","3ds xl","nintendo switch"]
        doing = ["do it", "go on my", "run around","touch my","just stop","stop talking","stop caring","talk now","do something","just jump off a cliff","just die","just give up on this right now"]
        word7 = ["am alive","wanna kill myself","am here","don't know","am bored","am tired of this","am gonna kill myself","am gonna cry","am gonna explain it to you"]
        word8 = ["then","*sigh*","fine", "okaay","alright","thats alright", "its okay"]
        yes3 = ""
        yes4 = ""
        yes4allow = "no"
        yes3allow = "no"
        yes5allow = "no"
        yes6allow = "no"
        yes7allow = "no"
        yes5 = ""
        yes7 = ""
     

        yes1 = (random.choice(word1))
        
        yes2 = (random.choice(word2))
       
    
        if yes1 == "No":
          
            yes2 = (random.choice(word3))
        if yes1 == "Maybe":
            yes2 = (random.choice(word3))
        if yes2 == "nevermind":
            yes3 = (random.choice(word5))
            yes3allow = "yes"
        if yes2 == "I guess":
            yes3 = (random.choice(word5))
            yes3allow = "yes"
        if yes2 == "my":
            yes4allow = "yes"
            yes4 = (random.choice(nouns))
        if yes2 == "your":
            yes4allow = "yes"
            yes4 = (random.choice(nouns))
        if yes2 == "I'll":
            yes5allow = "yes"
            yes5 = (random.choice(doing))
        if yes5 == "go on my":
            yes6allow = "yes"
            yes6 = (random.choice(goonnouns))
        if yes3 == "go on my":
            yes4allow = "yes"
            yes4 = (random.choice(nouns))        
   
        if yes5 == "touch my":
            yes6allow = "yes"
            yes6 = (random.choice(nouns))
        if yes1 == "Yes":
            yes2 = (random.choice(word8))
        if yes2 == "I":
            yes3 = (random.choice(doing))
            yes3allow = "yes"
        if yes3 == "touch my":
            yes4allow = "yes"
            yes4 = (random.choice(nouns))    
       
       
     
 
        
        await message.channel.send(yes1)
        await message.channel.send(yes2)

        if yes3allow == "yes":
            await message.channel.send(yes3)

        if yes4allow == "yes":
            await message.channel.send(yes4)
    
        if yes5allow == "yes":
            await message.channel.send(yes5)
              
        if yes6allow == "yes":
            await message.channel.send(yes6)
            
        if yes7allow == "yes":
            await message.channel.send(yes7)
