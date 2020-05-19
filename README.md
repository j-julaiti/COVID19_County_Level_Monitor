# COVID19 County Level Monitoring

## Requirements
Python: >= 3.0

Python Library:
- pandas
- numpy
- matplotlib

You can install the required libraries via pip install

## Install 

### Only for Linux or MacOS users

`git clone https://github.com/JJ5196/COVID19_County_Level_Monitor.git`

`cd COVID19_County_Level_Monitor`

`./init.sh`

`source ~/.bashrc`

### Windows Users (or if you want to skip the installation)

`git clone https://github.com/JJ5196/COVID19_County_Level_Monitor.git`

`cd COVID19_County_Level_Monitor`

`python scan.py`

## Usage (After the Installation, and only for Linux/MacOS users)
`scan`

Note that you don't have to be inside the git folder to call the function scan

## Example
`$ git clone https://github.com/JJ5196/COVID19_County_Level_Monitor.git`

`$ cd COVID19_County_Level_Monitor`

`$ ./init.sh`

`$ source ~/.bashrc`

`$ scan`

`no config is file found, please input the 5-digit ZIP code: 17011`

`2 records have been found, which county are you looking for?`

`    1 Cumberland County, PA`

`    2 York County, PA`

`1`

![](https://github.com/JJ5196/COVID19_County_Level_Monitor/blob/master/output_example.png)

## Data
Data from The New York Times, based on reports from state and local health agencies.
