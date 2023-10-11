# ise-mab-export-import-tool
Tool to take export file from ISE and prepare it for re-import on new/restored ISE server

## Requirements
- Python 3 and pandas module
- Cisco ISE Server version 2.x or 3.x


## Usage
From the Cisco ISE web admin interface:
- Goto "Work Centers" -> "Network Access" -> "Identities"
- Select "Export" -> "Export All"
- With the downloaded file rename the "profiler_endpoints.csv" to a name of your choice
- Copy the export file into the folder with this tool
- Run the tool "python3 convert-ise-export2import-format.py"
  - The tool will prompt you to enter the filename of the export file
  - Then it will process the file and create an import file
  - The resulting filename will be displayed in the console output (based on the filename entered by the user and -import.csv) 
