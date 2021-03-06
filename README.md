# newsevents

Damian Trilling & Marieke van Hoof


This repo accompanies the following article:

Damian Trilling & Marieke van Hoof (2020) Between Article and Topic: News Events as Level of Analysis and Their Computational Identification, Digital Journalism, DOI: [10.1080/21670811.2020.1839352](htttps://dx.doi.org/10.1080/21670811.2020.1839352)


## Unpacking the data and creating working files
`unzip raw-private-encrypted.zip` will create the folder `raw-private`, which contains all necessary data to run the jupyter notebooks.
It is a password-protected file.

Then, run `src/data-processing/030-pkl2net.py` in order to create the folder `data/intermediate` with the necessaty `.net` files.




## Steps to fully run the analysis

On a dedicated VM (inca.interact-uva.surf-hosted.nl), we calculate the softcosine similarity using the following script:
`src/data-processing/softcosine_newsevents.py`

This produces the data in
`data/raw-private`   




## Folder structure and files

All files/folders in bold are archived publicly. 

- **src**
   + **draft** - contains work-in-progress to be moved to other folders (or deleted)
   + **data-processing** - contains data cleaning / processing scripts that generate any intermediate or temporary data files needed by the analyses
   + **lib** - contains functions used by other scripts in src/data-processing or src/analysis
   + **analysis** - scripts or notebooks that contain the actual analyses; should produce the files in /report
- **data**
   + **raw** - contains raw ‘public’ data. Files should never be manually edited or cleaned. 
   + raw-private - contains raw data that cannot be shared for any reason (copyright, privacy, etc.). 
   + **raw-private-encrypted** - contains an encrypted version of the data in raw-private. 
   + **intermediate** - contains ‘public’ data derived from raw data or downloaded from an external source automatically. Any files here can be recreated using the scripts in src/data-processing provided any needed external sources and private data are available. Files are archived publicly. 
   + tmp - contains temporarily generated data to help speed up or simplify processing, but that does not need to be stored. All files in this folder can be recreated using the scripts in scripts/data that do not depend on external sources or private data. Files are not archived. 
   + *Files directly in data/ are seen as final / published data sets.*
- **report**
   + **figures** - optional folder for embedded figures
   + *Files directly in report/ are final / published reports*


Required top-level files:
- Readme.Rmd / md
- LICENSE


Optional/recommended top-level files:

- Makefile or other executable script to run data processing and analyses
- .travis or other CI-file
- Dockerfile or other Container install script
- Requirements.txt or R-equivalent
