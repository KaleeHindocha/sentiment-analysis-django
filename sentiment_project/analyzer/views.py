from django.shortcuts import render
from textblob import TextBlob


def index(request):
    result = None  

    if request.method == "POST":
        text = request.POST.get("text", "")

        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity        
        subjectivity = analysis.sentiment.subjectivity  

       
        polarity_percent = int((polarity + 1) * 50)

    
        if polarity > 0:
            sentiment_label = "Positive"
        elif polarity < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

   
        if subjectivity >= 0.5:
            subjectivity_label = "Subjective"
        else:
            subjectivity_label = "Objective"

        result = {
            "text": text,
            "polarity_percent": polarity_percent,
            "sentiment_label": sentiment_label,
            "subjectivity_label": subjectivity_label,
            "polarity": polarity,
            "subjectivity": subjectivity,
        }

    return render(request, "index.html", {"result": result})

    
     
      
       
