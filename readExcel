import os
import xlwt
import xlrd3
import xlsxwriter
from datetime import datetime
from progressbar import ProgressBar, Percentage, Bar, ETA
import regex as re

# Variable creation to store folder path, filename et directory
chemin = input("Quelle est la source des fichiers à analyser (chemin complet) ? "
               "Exemple : C:\user\...  ==>")
dossier = os.listdir(chemin)
nom_fichier = input("Nom du fichier à créer : ")
sauvegarde = input("Où sauvegarder le nouveau fichier ? : ")
date = datetime.now().strftime('%Y%m%d')
fichier_final = str(date) + "_" + nom_fichier + ".xls"

# Count the number of files in the folder
cpt = len(dossier)
print("Il y'a", cpt, "fichiers dans le dossier", chemin)

#Progress Bar
pbar = ProgressBar(widgets=[Bar('>', '[', ']'), ' ', Percentage(), ' ', ETA()], maxval=cpt)

ligne = 2
nonvide = 0
row = 4
col = 1
col2 = 1

header = xlwt.easyxf('font: bold 1, color white; '
                     'alignment: horizontal left, vertical center; '
                     'pattern: pattern solid, fore_colour green;')

# Creation of workbook and sheet "DATAS"
fichier = xlwt.Workbook()
sheet1 = fichier.add_sheet("DATAS")
sheet1.write(1, col2, "Date", header)


# Loop to fill the file
for root, dirs, files, in pbar(os.walk(chemin)):
    xlsfiles = [_ for _ in files if _.endswith('.xlsx')]
    for xlsfile in xlsfiles:
            wb = xlrd3.open_workbook(os.path.join(root, xlsfile))
            date = re.split("[._]", xlsfile)[0]
            objet = re.split("[_.]", xlsfile)[1]
            auteur = re.split("[_.]", xlsfile)[-2]
            sheet = wb.sheet_by_index(0)
            empty_cell = False
            num_cols = sheet.ncols
            num_rows = sheet.nrows
            for row_index in range(row, num_rows):
                # set count empty cells
                count_empty = 0
                # print('Ligne: {}'.format(row_index))
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
                        # print('Ligne #: {} | Value: {}'.format(row_index, data))
                        sheet1.write(ligne, col2, date)
                        sheet1.write(ligne, col2+1, objet)
                        ligne += 1
                        nonvide += 1

                # check the counter if is = num_cols means the whole row is empty
                if count_empty == num_cols:
                    print('Row is empty')
                    # stop looping to next rows
                    break

print("This is the result")

# Save the stats file
fichier.save(os.path.join(sauvegarde, fichier_final))
