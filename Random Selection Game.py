import random

def Random():
    articles = []
    while True:
        art = (input("To continue 'Enter Next' else, Enter articles: "))
        if art == "Next":
            break;
        articles.append(art)
    print(articles)
    verbs = []
    while True:
        vb = (input("To continue 'Enter Next' else, Enter Verbs: "))   
        if vb == "Next":   
            break;
        verbs.append(vb)
    print(verbs)
    nouns = []
    while True:
        nn = (input("To continue 'Enter Next' else, Enter Nouns: "))
        if nn == "Next":   
            break;
        nouns.append(nn)
    print(nouns)
    adverbs = []
    while True:
       ad = (input("To continue 'Enter End' else, Enter Adverbs: "))   
       if ad == "End":   
           break;
       adverbs.append(ad)
    print(adverbs)
#part 2: 
    def Sentence():
        article = random.choice(articles)    
        noun = random.choice(nouns)
        verb = random.choice(verbs)
        adverb = random.choice(adverbs)
       
        our_sentence = article + " " + noun + " " + verb + " " + adverb + "."
        our_sentence = our_sentence.capitalize()
         
        print(our_sentence)  
        
    Sentence()
    Sentence()
    Sentence()   
    Sentence()
    Sentence() 
Random()
        
  
            

