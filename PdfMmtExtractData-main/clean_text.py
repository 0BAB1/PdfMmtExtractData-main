def cleanId(text):
    to_cut = ["'","\\"]
    text = text.replace(to_cut[0], "")
    text = text.split(to_cut[1])[0]
    return text
    
def cleanTxt(text):
    text = text.replace("'", "")
    return text