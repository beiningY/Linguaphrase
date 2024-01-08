# Importation des modules nécessaires
from django.shortcuts import render
from .models import Word
import random
from django.http import JsonResponse
import language_tool_python
import spacy

def home(request):
    return render(request, 'home.html')

def cours(request):
    # Liste des thèmes disponibles
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
    # Récupération des mots associés à un thème spécifique
    words = Word.objects.filter(theme=theme_name)
    return render(request, 'theme_words.html', {'words': words, 'theme': theme_name})

def exercise(request):
    # Liste des thèmes disponibles pour les exercices
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
    # Récupération des mots et verbes associés à un thème spécifique
    words = Word.objects.filter(theme=theme)
    nouns = words.filter(category='noun')
    verbs = words.filter(category='verb')

    # Sélection aléatoire de 5 mots et 5 verbes pour l'exercice
    selected_words = random.choices(list(nouns), k=5)  
    selected_verbs = random.choices(list(verbs), k=5) 

    context = {
        'selected_words': selected_words,
        'selected_verbs': selected_verbs,
        'theme': theme,  
    }

    return render(request, 'theme_exer.html', context)

# Chargement du modèle Spacy pour le traitement du langage naturel
nlp = spacy.load("en_core_web_sm")

def lemmatize_sentence(sentence):
    # Lemmatisation d'une phrase en utilisant le modèle Spacy
    doc = nlp(sentence)
    return [token.lemma_ for token in doc]

def contains_required_words(sentence, words):
    # Vérifie si une phrase contient tous les mots requis après lemmatisation
    lemmatized_sentence_words = set(lemmatize_sentence(sentence.lower()))
    words = set(word.lower() for word in words)
    return all(word in lemmatized_sentence_words for word in words)


def check_sentence(request):

    if request.method == "POST":
        sentence = request.POST.get("sentence", "")  
        selected_nouns = request.POST.getlist("nouns[]")  
        selected_verbs = request.POST.getlist("verbs[]")  
        print("Phrase:", sentence)
        print("Noms:", selected_nouns)
        print("Verbes:", selected_verbs)

        all_selected_words = selected_nouns + selected_verbs

        # Vérification de la présence de tous les mots requis dans la phrase
        if not contains_required_words(sentence, all_selected_words):
            return JsonResponse({"error": "Votre phrase ne contient pas tous les mots requis."})

        # Utilisation de l'outil de vérification de la grammaire pour suggestions
        tool = language_tool_python.LanguageTool('fr-FR')
        matches = tool.check(sentence)

        if not matches:
            return JsonResponse({"message": "La phrase est correcte !!!"})

        errors = [f"{match.ruleIssueType}: {match.message}" for match in matches]
        return JsonResponse({"suggestions": errors})
    else:
        return JsonResponse({"error": "Seule la méthode POST est autorisée."})
