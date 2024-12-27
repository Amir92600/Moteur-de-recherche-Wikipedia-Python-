import wikipediaapi

# Initialisation de l'objet Wikipedia en français avec un User-Agent
wiki_wiki = wikipediaapi.Wikipedia(
    language='fr',
    user_agent='MoteurRechercheWikipedia/1.0 (https://github.com/monutilisateur/moteur-recherche-wikipedia)'
)

# Demande de l'entrée utilisateur
search_term = input("Entrez un terme de recherche : ")

# Recherche de la page
page = wiki_wiki.page(search_term)

# Vérification de l'existence de la page
if page.exists():
    print("Titre :", page.title)
    print("Contenu :", page.text[:200])  # Affiche les 200 premiers caractères du contenu
else:
    print("Aucun résultat trouvé.")
