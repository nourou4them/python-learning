import os
import xlwt
import xlrd3
from datetime import datetime
from progressbar import ProgressBar, Percentage, Bar, ETA

# Créer des variables pour stocker le chemin du dossier des fichiers de modifs,
# le nom du fichier des stats et sa destination
chemin = '//chemin/complet'
dossier = os.listdir(chemin)
nom_fichier = input("Nom du fichier : ")
sauvegarde = input("Où sauvegarder le fichier ? : ")
date = datetime.now().strftime('%Y%m%d')
fichier_final = str(date) + "_" + nom_fichier
# Compter le nombre de fichiers inclus dans le dossier spécifié
cpt = len(dossier)
print("Il y'a", cpt, "fichiers dans le dossier", chemin)

pbar = ProgressBar(widgets=[Bar('>', '[', ']'), ' ',
                                            Percentage(), ' ',
                                            ETA()],maxval=cpt)

# Création d'un classeur excel et d'une feuille "Datas"
fichier = xlwt.Workbook()
sheet1 = fichier.add_sheet("Datas")

index = 0
nonvide = 0
row = input("Quelle ligne ? ")
row = int(row)
col = input("Quelle colonne ? ")
col = int(col)

for root, dirs, files, in pbar(os.walk(chemin)):
    xlsfiles = [_ for _ in files if _.endswith('.xlsx')]
    for xlsfile in xlsfiles:
            wb = xlrd3.open_workbook(os.path.join(root, xlsfile))
            sheet = wb.sheet_by_name('sheet_name')
            empty_cell = False
            num_cols = sheet.ncols
            num_rows = sheet.nrows
            for row_index in range(row, num_rows):
                # set count empty cells
                count_empty = 0
                #print('Ligne: {}'.format(row_index))
                for col_index in range(col):
                    # get cell value
                    data = sheet.cell_value(row_index, col)
                    # check if cell is empty
                    if data == '':
                        # set empty cell is True
                        empty_cell = True
                        # increment counter
                        count_empty += 1
                    else:
                        # set empty cell is false
                        empty_cell = False

                    # check if cell is not empty
                    if not empty_cell:
                        # print value of cell
                        #print('Ligne #: {} | Value: {}'.format(row_index, data))
                        sheet1.write(index, 0, data)
                        index += 1
                        nonvide += 1

                # check the counter if is = num_cols means the whole row is empty
                if count_empty == num_cols:
                    print('Row is empty')
                    # stop looping to next rows
                    break

print(nonvide)

# Sauvegarde du fichier xls des stats
fichier.save(os.path.join(sauvegarde, fichier_final))
