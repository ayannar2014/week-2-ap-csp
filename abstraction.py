#abstraction is when i hide the complex details for something a lot more simple. 
#function allows us to wrap data or information into a special box or enclosure for reuse
#define a function
# def personalInformation():
#     question1= input("how old are you?")
#     question2= input("where do you live?")
#     question3= input("what school do you go to?")
# print(question1 + question2 + question3)
# #if you dont space them over its outside of your function
# personalInformation()
# personalInformation()

def Age():
    q1 = int(input("when year is it now?"))
    q2 = int(input("what year were you born?"))
    answer = q1 - q2
    result = print(f'you are {answer} years old')
Age()
Age()

#how to push to github
#git add .
#git push origin
#if that doesnt work do git push orgin--force