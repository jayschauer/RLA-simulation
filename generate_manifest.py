from rla.pres_senate_rla import *

import csv

combined_elections = get_combined_elections()
print(len(combined_elections))
elections2016 = combined_elections[18]
print(elections2016)
with open('manifest.csv', 'w') as manifest_file:
    writer = csv.DictWriter(manifest_file, fieldnames=['Batch ID', '# of Sheets', 'First Imprinted ID', 'Last Imprinted ID', 'Municipality', 'Precinct Number', 'Box Letter', 'Folder Number'])
    writer.writeheader()
    election = elections2016['Michigan'].pres
    row = {
        'Batch ID': 0,
        '# of Sheets': election.total_votes,
        'First Imprinted ID': 0,
        'Last Imprinted ID': election.total_votes - 1,
        'Municipality': 'MI_pres_2016',
        'Precinct Number': 0,
        'Box Letter': 'A',
        'Folder Number': 0,
    }
    writer.writerow(row)