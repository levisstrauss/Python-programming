# it reflect of LIFO Last In first out
# Its a combination of compiling the data iside of the stack
browsing_session = []

browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
lsst = browsing_session.pop()
print(browsing_session)
if not browsing_session: # To verify if the stack is empty
    browsing_session[-1] #to get the value of the stacks on top the stacks