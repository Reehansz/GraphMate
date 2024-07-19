

def nlp(text) :
    import openai
    chatstr= ""
    openai.api_key = "YOUR API KEY"
    chatstr = f"Kill previous History and just give me mathematical expression from the sentence, don't explain or try to solve '{text}' it should be parsable by python in lowercase and should have all symbols (+,-,*,/)"
    # print(chatstr)

    try :
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        res = response['choices'][0]['text']
        return res.replace('^','**')
    except :
        return "please repeat again"

def nlpdes(text):
    import openai
    chatstr= ""
    openai.api_key = "YOUR API KEY"
    chatstr = f"{text} mention just it's domain and range in words in one line"

    try:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        res = response['choices'][0]['text']
        return res
    except:
        return "please repeat again"

# print(nlp("3 x square plus 5 into x plus 8"))
# print(nlpdes(nlp("3 x square plus 5 into x plus 8")))


    
