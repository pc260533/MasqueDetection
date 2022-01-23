import csv
import glob
import os

# On réarrange les colonnes des fichiers contenant les boudings boxes puis on les copie dans le dossier mAP/input/detection-results/ pour leur conversion au format de cartucho/mAP (dénormalisation).
for imageName in glob.glob('result/detect/exp/labels/*.txt'):
    with open(imageName, 'r') as infile, open('./mAP/input/detection-results/' + os.path.basename(imageName), 'w') as outfile:
        writer = csv.writer(outfile, delimiter=" ", lineterminator='\n')
        for row in csv.reader(infile, delimiter=" "):
            rowRearange = [row[0], row[5], row[1], row[2], row[3], row[4]];
            writer.writerow(rowRearange)