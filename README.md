### Clonez le dépôt sur votre ordinateur local :

git clone https://github.com/beiningY/Linguaphrase.git

### Accéder au répertoire du projet :

cd Linguaphrase

### Créer et activer un environnement virtuel (facultatif mais fortement recommandé) :

python -m venv venv
source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`

### Installer les dépendances du projet :

pip install -r requirements.txt

### Effectuer les migrations de la base de données :

python manage.py migrate

### Démarrer le serveur de développement :

python manage.py runserver

### Accéder au site web : Ouvrez le lien suivant dans votre navigateur :

http://localhost:8000/
