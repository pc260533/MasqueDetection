# MaskDetection

## Information sur le dataset d'entrainement
Le dataset d’entrainement est composé de 3435 images annotées au format Pascal/VOC à l’aide de bounding boxes. 
3 classes d’objets sont présentes :
-	Classe without_mask : visage sans masque,
-	Classe with_mask : visage avec masque,
-	Classe with_incorrect_mask : visage avec masque mal porté.


## Information sur le dataset de validation
Le dataset de validation utilisé pour tester la fiabilité de l’algorithme est :  
https://www.kaggle.com/andrewmvd/face-mask-detection  
3 classes d’objets sont présentes :
-	Classe without_mask : visage sans masque,
-	Classe with_mask : visage avec masque,
-	Classe with_incorrect_mask : visage avec masque mal porté.  
Il est composé de 853 images annotées au format Pascal/VOC.


## Entrainement avec le dataset d'entrainement
-	Cloner le projet,
-   Créer un environnement virtuel,
-	Installer les dépendances contenues dans le requirements.txt :  
```pip install -r requirements.txt```  
Le dossier ```datasets/train``` contient le dataset d'entrainement au format yolov5.
Pour lancer l'entrainement, on utilise la commande suivante :  
```python yolov5/train.py --img 416 --batch 16 --epochs 50 --data ../datasets/data.yaml --weights yolov5.pt --cache --project=../result/train```  
Les données des entrainements sont dans :  
```result/train```  
Les paramètres utilisés pour obtenir nos meilleurs poids sont :
-   Nombre d'epochs = 50,
-   Taille de batch = 16,
-   Optimizer = SGD.


## Evaluation de la solution pour obtenir le cartucho/mAP avec le dataset de validation 
-	Cloner le projet,
-   Créer un environnement virtuel,
-	Installer les dépendances contenues dans le requirements.txt :  
```pip install -r requirements.txt```  
Le dossier ```datasets/valid``` contient le dataset d'entrainement au format yolov5.

Pour lancer la détection sur le dataset de validation, on utilise la commande suivante :  
```python yolov5/detect.py --weights ../best_50.pt --img 416 --conf 0.1 --source ../datasets/valid/images --project=../result/detect --exist-ok --save-txt --save-conf```

Les images du dataset de validation avec les bouding boxes de prédictions sont dans :  
```result/detect/exp```  
Les coordonnées et les lables associés sont dans :  
```result/detect/exp/labels```

Pour visualiser les 10 premières images du dataset de validation avec les boundings boxes, on utilise la commande suivante :  
```python affichageDetectionDatasetValidation.py```

Pour accéder aux mesures de mAP avec la fonction de YOLOv5, on doit d'abord convertir les annotations obtenues par la détection au format YOLO au format VOC :
Pour cela, on exécute la commande :  
```python yoloNewToYoloOld.py```  
Celle-ci réarrange les annotations YOLO en un format YOLO plus ancien de la façon suivante :  
```<class_id> <center_x> <center_y> <bb_width> <bb_height> <confidence>```  
=>  
```<class_id> <confidence> <center_x> <center_y> <bb_width> <bb_height>```

Puis, on exécute la commande :  
```python mAP/scripts/extra/convert_dr2_yolo.py```  
Celle-ci convertit les annotations YOLO anciens au format VOC :  
```<class_id> <center_x> <center_y> <bb_width> <bb_height> <confidence>```  
=>  
```<class_name> <confidence> <left> <top> <right> <bottom>```

Pour finir, on supprime le dossier ```mAP/input/detection-results/backup``` pour réutiliser la commande une nouvelle fois.

Les annotations du dataset de validation ont préalablement été converti de la même manière.  
Le contenu du dossier ```datasets/valid/labels``` a été copié dans le dossier ```mAP/input/ground-truth```.  
De plus, la commande suivante a déjà été exécutée :  
```python mAP/scripts/extra/convert_gt_yolo.py```

Après ces conversions, pour accéder aux mesures de mAP de cartucho on utilise la commande suivante :  
```python mAP/main.py```

YOLOv5 fournit également une commande pour calculer le mAP@0.5 :  
```python val.py --data ../datasets/data.yaml --weights ../best_50.pt --img 224 --project=../result/map --exist-ok```

Dans les deux cas, on retrouve des valeurs similaires de mAP.


## Faire des inférences et afficher les résultats de la détection en temps réel
-	Cloner le projet,
-   Créer un environnement virtuel,
-	Installer les dépendances contenues dans le requirements.txt :  
```pip install -r requirements.txt```

Pour lancer la détection sur le flux vidéo de la caméra du PC, on utilise la commande suivante :  
```python yolov5/detect.py --weights ../best_50.pt --img 416 --conf 0.1 --source 0```

Pour lancer la détection sur le flux vidéo d'une ou plusieurs sources vidéos externes, on utilise la commande suivante :  
```python yolov5/detect.py --weights ../best_50.pt --img 416 --conf 0.1 --source ../streams.txt```
Le fichier ```streams.txt``` contient la liste des sources.  
Par exemple, avec l'application IP Webcam sur Smartphone :  
```http://192.168.1.12:8080/video```


## Auteurs
-	__Pierre-Nicolas CHASSAGNE__ : Pierre-Nicolas_Chassagne@etu.u-bourgogne.fr,
-	__Nicolas FORGERON__ : Nicolas_Forgeron@etu.u-bourgogne.fr.