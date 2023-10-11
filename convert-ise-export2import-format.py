#!/opt/homebrew/bin/python3.11

#########
# Purpoose: Convert endpoint export file from ISE to be used for migration
# and import into other ISE servers.  Preserves the MAB related attributes of
# (MACAddress,EndPointPolicy,IdentityGroup,Description,StaticAssignment,StaticGroupAssignment)
#
# Author: Zeb Whitehead - Auburn University
# Lastupdated: 20231010
#
#########

#Require to install the pandas module
import pandas as pd

#Prompt user for ISE export filename
Exportfname = input('Enter the ISE Export file name: ')
#Create ISE Import filename base on the export filename
Importfname = Exportfname.split('.')[0]+'-import.csv'

#Read the export file from ISE and convert into a Dataframe object
df = pd.read_csv(Exportfname)

#Add column to Dataframe object
df.insert(1, "EndPointPolicy", '', allow_duplicates = True)

#Tell user what is happening
print("Creating ISE import file: " + Importfname)

# Output only the select columns of the Dataframe object to a 
# resulting csv file used for import into ISE
df.to_csv(Importfname, index=False, columns=['MACAddress', 'EndPointPolicy', 'IdentityGroup', 'Description', 'StaticAssignment', 'StaticGroupAssignment'])


print("Done!!! \nLogin to the new ISE server and import this file into the Endpoint Identities")


#DEBUG
#print(df)

