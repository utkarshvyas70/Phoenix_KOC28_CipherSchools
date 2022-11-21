emailId =(input("Enter your email id: "))
username=emailId[:emailId.index("@")]
domain_=emailId[emailId.index("@")+1:]
domain__=domain_.upper()
print(f"Your desired username is {username} and your desired domain is {domain__}")