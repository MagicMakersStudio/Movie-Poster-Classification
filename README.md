# Reconnaissance de films d'action d'après leurs affiches

Des adolescents ont créé un modèle qui reconnaît, d'après son affiche, si un film est un film d'action ou non.
Ils ont utilisé les modules Tensorflow et Keras en python pour créer leur réseau de neurones.

## Stage IA à Magic Makers

[Magic Makers](https://www.magicmakers.fr/) propose des ateliers de programmation créative pour des jeunes de 7 à 15 ans. Depuis 2018, des ateliers pour adolescents autour de l'intelligence artifielle sont donnés durant les vacances. Lors du stage, les makers découvrent ce qu'est un réseaux de neurones et les notions s'y attachant (perceptron multi-couches, convolutions, overfit, etc) en créant des projets comme celui-ci !

## Auteur du projet

Ce projet a été réalisé par **Léo et Tara** (en 5e et 3e) lors du stage de Juillet dans les bureaux de Blablacar, animé par **Romain et Jade**.


### Dataset

* [Dataset d'affiches de films](https://www.kaggle.com/nazimamzz/imdb-dataset-of-5000-movie-posters) - Les URLs des affiches de films avec leurs genres

Pour récupérer les photos des affiches, Léo et Tara ont créé un programme qui permet de récupérer une image d'après son URL. Pour faciliter la suite de leur projet, chaque nom d'image comprend le genre du film et toutes leurs images sont enregistrées dans un dossier 'poster'.

```
python3 recupimagesIMDB.py
```

### Entraînement

Léo et Tara on utilisé un réseau de neurones par convolutions pour leur projet.

```
python3 affiche-train.py
```
## Built With

* [Keras](https://keras.io/) - pour créer le modèle (avec TensorFlow)
* [Flask](http://flask.pocoo.org/) - pour créer une webapp
* [PIL](https://pillow.readthedocs.io/en/3.1.x/reference/Image.html) - pour manipuler des images
* [Numpy](https://www.numpy.org/) - pour manipuler des tableaux
* [H5py](https://www.h5py.org/) - pour sauvegarder le modèle
* [Sklearn](https://scikit-learn.org/stable/) - pour mélanger et séparer les données

## Résultats

< à venir >

### Application

Une fois leur modèle entraîné, Léo et Tara ont créé un programme pour prédire si un film est un film d'action ou non d'après la photo de son affiche ! Leur programme prend plusieurs images et n'ouvre que celles qui correspondent à un film d'action !

```
python3 affiche-predictor.py
```

### Remerciement

* Merci à [Blablacar](https://www.blablacar.fr/) de nous avoir acceuilli dans vos locaux
* Merci à [Magic Makers](https://www.magicmakers.fr/)
* Merci à [Keras](https://keras.io/) pour faciliter la création de réseaux de neurones !
* Merci à [Kaggle](https://www.kaggle.com/) pour le dataset
