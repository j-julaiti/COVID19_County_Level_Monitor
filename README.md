COVID19 County Level Monitoring

# Requirements

OS: Linux or OSX

Python: >= 3.0

Python Library:
	1. pandas
	2. numpy
	3. matplotlib

You can install the library via pip install

# Install
git clone https://github.com/JJ5196/COVID19_County_Level_Monitor.git
cd COVID19_County_Level_Monitor
./init.sh
source ~/.bashrc

# Usage
`scan`

Note that you don't have to be inside the git folder to call the function scan

# Example
$ git clone https://github.com/JJ5196/COVID19_County_Level_Monitor.git
$ cd COVID19_County_Level_Monitor
$ ./init.sh
$ source ~/.bashrc
$ scan
$ no config is file found, please input the 5-digit ZIP code: 17011
2 records have been found, which county are you looking for?
    1 Cumberland County, PA
    2 York County, PA
1

# Data 
Data from The New York Times, based on reports from state and local health agencies.
