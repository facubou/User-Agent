from user_agents import parse
export = ""

f = open("your_txt_File", "r")
f2 = open("UAexport.txt", "w")
for line in f:
    ua_string = str(line)
    user_agent = parse(ua_string)
    concat = str(user_agent) + ":" + line 
    #print (user_agent) 
    export = concat + "\n" + str(export)

f2.write (export)

