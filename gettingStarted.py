### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "065f16710de22f46ee97f7cb131ebf2c7e6b7685f1fcbae8da2b15a06d52bddc"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = int(7)
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = int(3)
    else: 
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
        answer = "Invalid question"
    return(answer)
# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))

#Questions:
#elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
# answer = "pcap"
#elif question == "Are encoding and encryption the same? - Yes/No":
# answer = "No"
#elif question == "Is it possible to decrypt a message without a key? - Yes/No":
# answer = "No"
#elif question == "Is it possible to decode a message without a key? - Yes/No":
# answer = "Yes"
#elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
# answer = "No"
#elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
# answer = "065f16710de22f46ee97f7cb131ebf2c7e6b7685f1fcbae8da2b15a06d52bddc"
#elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
# answer = "No"
#elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
# answer = int(7)
#elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
# answer = int(2)
