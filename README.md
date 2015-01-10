# MyPugliaSOS - Italiano

MyPugliaSOS è un server web per i soci di PugliaSOS.
Permette loro di contattare altri soci, iscriversi a eventi e corsi e avere
informazioni riguardanti quelli già frequentati.

## Installazione

Per installare il web server, assicurarsi di avere installati sul proprio pc:

- git
- Python 2.7
- pip

Aprire il terminale. Solo per questo passo potreste aver bisogno di
privilegi da amministratore.
Scrivere:

    pip install Django==1.7.1
    pip install whitenoise==1.0.6

Adesso clonare il repository:

    git clone https://github.com/PugliaSOS/my-puglia-sos.git

Il codice sorgente sarà adesso nella cartella *my-puglia-sos*.

    cd my-puglia-sos

Creare il database:

    python manage.py syncdb

Verrà chiesto di creare un superuser. Si può farlo subito, inserendo username
(che dovrebbe essere un indirizzo email) e password, o farlo in seguito.

Avviare il server:

    python manage.py runserver

Se tutto va bene, dovrebbe comparire una scritta come la seguente:

    Django version 1.7.x, using settings 'my_puglia_sos.settings.deveolpment'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Aprire il browser ed inserire nella barra degli indirizzi:

    localhost:8000

Fatto!

# Contributi

Questo software è correlato al progetto Coding Lab promosso da PugliaSOS.
Per contribuire al progetto, contattare PugliaSOS a segreteria@pugliasos.it.

# MyPugliaSOS - English

MyPugliaSOS is a web server for PugliaSOS's associates.
It allows them to contact other associates, enroll to events or courses
and get info about attending ones.

## Setup

To setup the web server, be sure you have installed on your pc:

- git
- Python 2.7
- pip

Open the terminal. You might need admin permissions only for this step.
Type:

    pip install Django==1.7.1
    pip install whitenoise==1.0.6

Now clone the repo.

    git clone https://github.com/PugliaSOS/my-puglia-sos.git

You will find the source code in the folder *my-puglia-sos*.

    cd my-puglia-sos

Create the database:

    python manage.py syncdb

You will asked to create a superuser. You can either create it, typing
username (which should be an email address) and password, or do it later on.

Start the server:

    python manage.py runserver

If everything goes fine, you should see something like:

    Django version 1.7.x, using settings 'my_puglia_sos.settings.deveolpment'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Now just open the browser and type into the address bar:

    localhost:8000

Done!

# Contribution

This software is related to the Coding Lab by PugliaSOS.
To contribute to this project, please contact PugliaSOS at
segreteria@pugliasos.it.
