def questions():
    questions = ["How important is money to you?",
                     "How do you feel about spending money?",
                     "Spending makes me feel",
                     "How do you feel about saving money?",
                     "What best describes you?",
                     "I am comfortable taking risks with my money.",
                     "How do you feel about your financial future?",
                     "Are you often satisfied with your financial decisions?",
                     "What is your money motto?",
                     "Which best describes you?",
                     "If you had $1m today, what would you do with it?",
                     "How do you feel about retirement planning?",
                     "How do you feel about debt?"]

    options = [("A. Not important at all", "B. Somewhat important", "C. Important", "D. Very important"),
               ("A. I enjoy spending money and don't worry about it too much.", "B. I'm comfortable spending money, but I'm also careful not to overspend", "C. I'm so careful and don't like to spend money unless I have to", "D. I'm very frugal and try to save as much money as possible."),
               ("A. Guilty", "B. Empowered", "C. Neither"),
               ("A. I don't think about saving money.", "B. I save money when I can, but it's not my priority.", "C. I'm a good saver and try to put away some money each month.", "D. I'm obsessed with saving money. I can save for Africa."),
               ("A. Student", "B. Career professional", "C. Homemaker", "D. Self-employed", "E. Unemployed", "F. On a career break", "G. Retired"),
               ("A. Yes", "B. Not really", "C. No", "D. A big no"),
               ("A. I'm not too worried about my financial future.", "B. I'm a bit concerned about my financial future, but I'm confident that I'll be okay.", "C. I'm very concerned about my financial future, and I'm not sure how I will make ends meet.", "D. I'm not concerned about my financial future because I believe that everything will work out in the end."),
               ("A. Yes", "B. Somewhat", "C. No"),
               ("A. Money makes the world go round", "B. Money doesn't grow on trees", "C. It’s better to give than to receive", "D. I never look at the price tag"),
               ("A. I borrow to spend on luxuries to impress other people", "B. I am an impulsive spender and feel guilty about my unplanned expenses", "C. I keep track of my spending. I am satisfied with my financial actions", "D. I am a bit tight with money"),
               ("A. Pamper myself to some shopping", "B. Save and invest 90% of the money", "C. Take care of my necessities and share with loved ones", "D. Buy something and flaunt it on Instagram"),
               ("A. Thumbs up", "B. Thumbs down"),
               ("A. I pay back my debt", "B. I don’t borrow if I can’t afford it", "C. I have issues paying back my debt")]

    responses = []

    index = 0

    for question in questions:
        print("\n")
        print(question)

        for option in options[index]:
            print(option)
        response = input("Enter A, B, C or D: ").upper()
        responses.append(response)
        index += 1

    return responses

def money_personality(responses):
    nurturers = 0
    savers = 0
    spenders = 0
    hoarders = 0


    if responses[0] == "C" or responses[0] == "D":
        hoarders +=1
        savers += 1
        nurturers += 1
    elif responses[0] == "B":
        spenders += 1


    if responses[1] == "B":
        savers += 1
        nurturers += 1
    elif responses[1] == "A":
        spenders += 1
    else:
        hoarders += 1


    if responses[2] == "B":
        savers += 1
        nurturers += 1
        hoarders += 1
    elif responses[2] == "A":
        spenders += 1


    if responses[3] == "C":
        savers += 1
        nurturers += 1
    elif responses[3] == "B":
        spenders += 1
    else:
        hoarders +=1


    if responses[5] == "B":
        spenders += 1
        nurturers += 1
    elif responses[5] == "A":
        spenders += 1
        savers += 1
    elif responses[5] == "D":
        hoarders +=1


    if responses[6] == "B":
        nurturers += 1
        hoarders += 1
    elif responses[6] == "C":
        spenders += 1
        hoarders += 1
    elif responses[6] == "A":
        spenders += 1
    else :
        savers += 1


    if responses[7] == "A":
        nurturers += 1
        hoarders += 1
        savers += 1
    elif responses[7] == "C":
        spenders += 1


    if responses[8] == "B":
        hoarders += 1
        savers += 1
    elif responses[8] == "C":
        nurturers += 1
    elif responses[8] == "D":
        spenders += 1


    if responses[9] == "C":
        nurturers += 1
        savers += 1
    elif responses[9] == "A" or  responses[9] == "B":
        spenders += 1
    else:
        hoarders += 1


    if responses[10] == "B":
        hoarders += 1
        savers += 1
    elif responses[10] == "C":
        nurturers += 1
    else:
        spenders += 1


    if responses[11] == "A":
        hoarders += 1
        savers += 1
        nurturers += 1
    elif responses[11] == "B":
        spenders += 1


    if responses[12] == "B":
        nurturers += 1
        savers += 1
        hoarders += 1
    elif responses[12] == "A":
        nurturers += 1
        savers += 1
    elif responses[12] == "C":
        spenders += 1

    return {
        "saver" : savers,
        "hoarder" : hoarders,
        "spender" : spenders,
        "nurturer" : nurturers
    }

# answers = questions()
#
# print("\n")
# print(money_personality(answers))
