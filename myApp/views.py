from django.shortcuts import render
from .models import Word
import random
from django.http import JsonResponse
import language_tool_python
import spacy

def home(request):
    return render(request, 'home.html')

def cours(request):
    themes = [
        'colours', 
        'town', 
        'kitchen', 
        'pencase', 
        'fruits', 
        'objects', 
        'pets', 
        'school', 
        'summer'
    ]
    return render(request, 'cours.html', {'themes': themes})

def theme_words(request, theme_name):
    words = Word.objects.filter(theme=theme_name)
    return render(request, 'theme_words.html', {'words': words, 'theme': theme_name})

def exercise(request):
    themes = [
        'colours', 
        'town', 
        'kitchen', 
        'pencase', 
        'fruits', 
        'objects', 
        'pets', 
        'school', 
        'summer'
    ]
    return render(request, 'exercise.html', {'themes': themes})


def exercise_theme(request, theme):
    words = Word.objects.filter(theme=theme)
    nouns = words.filter(category='noun')
    verbs = words.filter(category='verb')

    selected_words = random.choices(list(nouns), k=5)  
    selected_verbs = random.choices(list(verbs), k=5) 

    context = {
        'selected_words': selected_words,
        'selected_verbs': selected_verbs,
        'theme': theme,  
    }

    return render(request, 'theme_exer.html', context)

nlp = spacy.load("en_core_web_sm")
def lemmatize_sentence(sentence):
    doc = nlp(sentence)
    return [token.lemma_ for token in doc]

def contains_required_words(sentence, words):
    lemmatized_sentence_words = set(lemmatize_sentence(sentence.lower()))
    words = set(word.lower() for word in words)
    return all(word in lemmatized_sentence_words for word in words)


def check_sentence(request):

    if request.method == "POST":
        sentence = request.POST.get("sentence", "")  
        selected_nouns = request.POST.getlist("nouns[]")  
        selected_verbs = request.POST.getlist("verbs[]")  
        print("Sentence:", sentence)
        print("Nouns:", selected_nouns)
        print("Verbs:", selected_verbs)


        all_selected_words = selected_nouns + selected_verbs

        if not contains_required_words(sentence, all_selected_words):
            return JsonResponse({"error": "Your sentence does not contain all the required words."})

        tool = language_tool_python.LanguageTool('en-US')
        matches = tool.check(sentence)

        if not matches:
            return JsonResponse({"message": "The sentence is correct!!!!!!"})

        errors = [f"{match.ruleIssueType}: {match.message}" for match in matches]
        return JsonResponse({"suggestions": errors})
    else:
        return JsonResponse({"error": "Only POST method allowed."})
