def check(sentence, words): 
    splt_txt=sentence.split('.')
    translator = Translator()
    translations = translator.translate(splt_txt, 'en')
    all_sentence=[]


    for translation in translations:
        
        all_sentence.append(translation.text)
    res = [any([k in s for k in words]) for s in all_sentence] 
    return ['It seems Docor Suggest some medicine or Test. You can visit our site for online medicine or in any clinic for appointment' for i in range(0, len(res)) if res[i]] 
      
 




sentence = 'I would request you to go for a mammogram or Test. Once you get the report. Please visit to my clinic for details check.'
words = ['medicine', 'test','mri','mammogram']
print(check(sentence, words))

    
OutPut:



['It seems Docor Suggest some medicine or Test. You can visit our site for online medicine or in any clinic for appointment']











