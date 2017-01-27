## Raw Data Backup

Dear Colleages,

Backup of ___raw and anonymized data___ is important for legal reasons, it is proper scientific conduct and allows to maintain the  replicability of your analysis.

It is therefore mandatory that you ***proactively*** engage in the backup of your analog and digital raw data ***before*** you start analysis.


## Our laboratory supports your backup as follows:

#### Terminology
*Analog raw* data is data collected with a questionnaire or by clinical examination, e.g. age, sex, handedness, fugl-meyer, etc. *Overhead* is everything which is not data, but necessary for the experiment, e.g. signed consent forms, payment notes, lab notebook, etc. *Digitized analog* data is analog data which has been put in some digital format (e.g. csv or txt). *Primarily digital* data is data collected directly with a pc, e.g. EEG, EMG, protocol code artifacts etc.

#### Primarily Digital and Digitized Analog Data

1. Digitize all analog raw data into e.g. a txt, excel or csv file
    - organized by pseudonyms within the file
    - or directly into each subjects folder
2. The raw analog data can then be put into the overhead binder.
2. Latest 6 months after data collection is finished:
    - check for consistency of the data
    - anonymize the data (i.e. PP_01 -> sub_001; KJ_24 --> sub_002)
2. Store anonymized digitized analog and primarily  data you acquired during a experiment on your local analysis PC.
2. Compress the data folder / archive into a zip-file.
3. Provide a copy of the zip-file on an external hard-drive or USB-stick to Robert
4. Robert will push the data on our backup NAS server.

Everyone from the lab can afterwards retrieve the raw data by <a href="#howto"> connecting to the backup server from an analysis PC.</a>

#### Overhead / Analog Raw Data
1. Store your overhead in a binder
2. Store your analog raw data in a binder
2. Hand the binder to Doris Wildner
3. Doris puts it into a lockable cabinet in her office
4. You can access the binder during Doris office hours (or by asking Robert)

## Data organization
Working software over comprehensive documentation!

##### before
But we suggest a clear organization of raw data for a project, e.g.:

    - project_name
        - readme.txt (%describe project, name and contact details of team members)
        - data
            - sub_001 (%provide only anonymized data)
                - conditionA
                - conditionB
            - sub_002
            - ...
        - protocol
            - code (%code to run your experiment)
            - docs (%folder with handouts, forms, protocol description, etc.)


##### during

We advise to use some version control tool (ideally [git](https://git-scm.com/)) for working on your scripts and drafts. Our lab has an [academic account on GitHub](https://github.com/translationalneurosurgery), with private repositories. Consider to collaborate on GitHub for easy version control, and getting feedback on your code and drafts from colleagues. If you have any questions on version control with git, ask Robert or Valerio.

##### after
Once your data is analyzed and published, you might additionally want to backup stuff like:

    - code (%folder containing your data analysis code)
        - dependencies.txt (%state toolboxes used)
        - utils (%folder with helper functions)
    - results (%folder containing your analysis results)
        - img (%folder containing e.g. images)
        - proc (%folder containing intermediate / cached data)
    - pub (%folder containing your drafts)

<h2 id = "howto"> Connecting to the Backup NAS server</h2>

The purpose of the backup-server is maintaining a backup copy of the data. Please do not put unnecessary load on the drives by running scripts on the data directly. Download a local copy!

<!--- ![bup_uname](./bup_passwd.png) --->

#### Access is restricted.
- Get username, password and ip-adress from Robert or Lukas.
- The account gives you read-only rights.
- You can access the data only from any analysis PC in the upper floor.


#####  For connecting to the backup NAS server using ftp-client (e.g. File Zilla)

1. Start FileZilla.

2. Go to the tap menu to File, Site Manager.

3. Create a new Site by clicking on the button on the left site.

4. On the right site you need to enter  host ip address, user name and password.

5. Connect by clicking on the connect button.

6. On the left you can see the your folders and on the right side the server folders.
7. You can copy data on your pc by going to your desired folder
8. Drag and drop the desired files to your local folder.


#### For connecting to the backup NAS server using an internet browser


1. Open your browser.
2. Enter the IP address of the processing server

3. Click on the figure with the folder to get to the web file manager.

4. Click again to enter the user name and password

4. Data is stored in the public directory.

5. Go to the folder of interest.

5. Click on the blue icon with the green arrow pointing down to download the desired files.

6. Logout if you are finished.
