#coding excercise of "100 days of python" course in Udemy
#love score calculator

 
def calculate_love_score(name1, name2):
    
    name1 = name1.lower()
    name2 = name2.lower()
    
    word_true = "true"
    word_love = "love"
    
    conc_names = name1 + name2
    
    total_for_word_true_names = 0
    total_for_word_love_names = 0
    
    for each_letter_true in word_true :
        for each_letter_name in conc_names :
            if each_letter_true == each_letter_name:
               total_for_word_true_names += 1
    #print(total_for_word_true_names)
    
    for each_letter_love in word_love :
        for each_letter_name in conc_names :
            if each_letter_love == each_letter_name:
               total_for_word_true_names += 1 
    #print(total_for_word_love_names)
    
    print(str(total_for_word_true_names) + str(total_for_word_love_names))  
        
