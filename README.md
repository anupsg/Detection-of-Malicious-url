# Detection-of-Malicious-url
Using Shallow and deep networks
=> install all the softwares required

sudo apt-get install libatlas-base-dev gfortran python-dev
sudo apt-get install python-pip
sudo pip install --upgrade pip
sudo pip install numpy
sudo pip install scipy
sudo pip install matplotlib
Sudo pip install seaborn
sudo pip install scikit-learn
sudo pip install tensorflow
sudo pip install theano
sudo pip install keras
sudo pip install pandas
sudo pip install h5py
sudo pip install jupyter
sudo pip install ipython


=> set virtual environment 

follow the steps in the below link

https://sourabhbajaj.com/mac-setup/Python/virtualenv.html


Test is the folder that contains all the models and the supportive files and folders

The folders inside Test :

-> CSS
-> Fonts
-> JS
-> Prathi-URL-project-edited
-> Prathi-URL-project-updated
-> epoch-test-results

The files inside Test : 
-> index.html
-> process.php



Prathi-URL-project-edited : 

folder :

-> logs - has the checkpoints for each model
-> data - train.txt, test.txt, trainlabel.csv, testlabel.csv


This folder has the training and testing models in .py format and the csv files 

when you run the testing programs (for pre-trained models) in this folder (cnntest_1.py, cnnlstmtest_1.py, rnntest_1.py, lstmtest_1.py), you get the accuracy, recall, precision amd F1 score for each check points that is run for 60 epochs during training.

running the testing program in unix/linux/osx :

cd to the folder where these files are. in this case, to test/Prathi-URL-project-edited

cd test/Prathi-URL-project-edited
python model.py (Ex: python cnntest_1.py )

if you get an error for crossmodel slection, 
change it to model_selection.

in the line - from sklearn.model_selection import train_test_split


Prathi-URL-project-updated : 

folder :

-> logs - has the checkpoints for each model
-> data - train.txt, test.txt, trainlabel.csv, testlabel.csv

This folder has the training and testing models in .py format and the csv files 

when you run the testing programs (for pre-trained models) in this folder (cnntest_1.py, cnnlstmtest_1.py, rnntest_1.py, lstmtest_1.py), you get the validation of the url. you pass the url as the parameter and check if it is benign or malacious

cd to the folder where these files are. in this case, to test/Prathi-URL-project-updated

cd test/Prathi-URL-project-updated
python model.py url (Ex: python cnntest_1.py google.com)

=> To vew the training loss and accuracy : 

in terminal => jupyter notebook
open the PrAtHi-URL-graph.ipynb file and load every model's .csv file which is in logs folder to the "traindata = pd.read_csv('logs/CSV files/training_set_lstmanalysis.csv') " line in PrAtHi-URL-graph.ipynb file (edit the model names). Remember to give the proper path and name. 

To Run :

Remember to start from first line in the file till the last everytime you load the new model. 

shift+enter

=> Run in the browser (hosting - local host)

follow the steps in the following link

http://duspviz.mit.edu/tutorials/localhost-servers/

