"""
Erasmus Specified Students Filter
MIT Licensed — Developed by Anıl AKSU

------------------------------------------------------------

This script pulls student data from a public Google Sheet,
filters specific students based on TCKN and name rules,
sorts them by score, and appends the engineering average
as the final row. Output is written to a local Excel file.

Input: Google Sheet (shared as "Anyone with the link can view")
Output: Erasmus Specified Students.xlsx

How to use:
- Make sure the Google Sheet is shared as public (view-only)
- Run the script with Python 3 and pandas installed
- The result Excel file will be created in the current directory
"""

import pandas as pd
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Google Sheet ID from the shared URL
sheet_id = "1-78sp_ioi6tLnXmx1CYrOuP2vb9cB3GX"
sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

df = pd.read_csv(sheet_url)
print("Google Sheet data loaded successfully.")

# List of (TCKN head, TCKN tail, Name start) filters
given_persons = [ ("21", "4", "Ah"), ("10", "2", "Al"), ("17", "8", "An"), ("16", "8", "Ay"),
    ("16", "2", "Em"), ("32", "0", "En"), ("65", "4", "Ez"), ("17", "2", "Fu"),
    ("10", "8", "Fu"), ("21", "8", "Ha"), ("23", "6", "Hi"), ("21", "6", "Hü"),
    ("26", "4", "Kü"), ("27", "6", "Me"), ("12", "6", "Me"), ("23", "0", "Me"),
    ("21", "4", "Nu"), ("10", "2", "Ok"), ("16", "8", "Öm"), ("31", "2", "Öm"),
    ("15", "4", "Öz"), ("20", "0", "Se"), ("38", "2", "Se"), ("11", "4", "Sı"),
    ("19", "2", "Su"), ("19", "8", "Sü"), ("26", "8", "Üm"), ("34", "0", "Ah"),
    ("27", "4", "Ay"), ("21", "6", "Bu"), ("10", "8", "Bü"), ("11", "2", "Ci"),
    ("10", "4", "Çı"), ("10", "6", "De"), ("41", "8", "Em"), ("40", "2", "Er"),
    ("10", "4", "Fa"), ("54", "4", "Fu"), ("10", "6", "Me"), ("19", "6", "Ca"),
    ("12", "4", "Hi"), ("34", "2", "İl"), ("10", "6", "Ke"), ("37", "4", "Me"),
    ("46", "0", "Me"), ("26", "4", "Si"), ("10", "2", "Su"), ("38", "2", "Su"),
    ("10", "6", "Ya"), ("99", "8", "Al"), ("10", "0", "Ay"), ("10", "6", "Ba"),
    ("24", "4", "De"), ("20", "8", "İp"), ("60", "0", "Ni"), ("10", "4", "Ze")]

# Check if a student matches the defined filters
def is_anyone_matched(tckn,ad_soyad):
        for head,tail,name_mask in given_persons:
                if(str(tckn).startswith(head) and 
                   str(tckn).endswith(tail) and
                   str(ad_soyad).startswith(name_mask)):
                        return True
        return False   


# Apply filter to the dataset
matches = df.apply(lambda row : is_anyone_matched(row["TCKN"] , row["Ad Soyad"]) , axis=1) #filtering
matches_df = df[matches]

matches_df = matches_df.sort_values(by="Puan" , ascending=False)

# Calculate overall engineering average
df["Puan"] = df["Puan"].astype(str).str.replace(",", ".").astype(float)
mean_grade = df["Puan"].mean()


mean_dict = ([{"TCKN" : "",
            "Ad Soyad" : "Engineering Average",
            "Öğrenci No" : "",
            "Puan" : round(mean_grade,3)}]) #Dictionary(Data SET)

mean_row = pd.DataFrame(mean_dict)


# Combine filtered students with the average row
last_state = pd.concat([matches_df,mean_row] , ignore_index=True)

# Save result to Excel
output_file = "Erasmus Specified Students.xlsx"
output_file = "Erasmus Specified Students.xlsx"
last_state.to_excel(output_file, index=False)


print(f"✅ Process completed. Output file: {output_file}")

def upload_to_drive(filepath , filename_on_drive=None):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth() #Opens Browser
        drive = GoogleDrive(gauth)

        filename_on_drive = filename_on_drive or filepath
        upload_file = drive.CreateFile({"Title" : filename_on_drive})
        upload_file.SetContentFile(filepath)
        upload_file.Upload()
        upload_file.InsertPermission({
                "type" : "anyone",
                "value" : "anyone",
                "role" : "reader"
        })

        print(f"Uploaded: {upload_file["title"]}")
        print("Link:" , upload_file["alternateLink"])

upload_to_drive(output_file)
