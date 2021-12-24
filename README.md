# Training Journal App


## Description
Training Journal it's my school project that track you trainings.


## Goal
Goal - help people track and organaize trainings.


## Installation
Project don't completed.


## Usage
Open 'scripts' folder; choose script to run; use following instructions.
#### Adding train
For add train into database you need to open 'add_train.py' script to begin with.
Type train information when ask:

    Avaliable train types for now:
    	Other
    	Run
    
    Enter Type:
    run
    Enter Date:
    01.01.2021
    Enter Time:
    10:00
    Enter Description:
    Github drive
    Enter Duration:
    42:00
    Enter Distance:
    6 km
    INSERT INTO run VALUES (?, ?, ?, ?, ?)
    ['01.01.2021', '10:00', 'Github drive', '42:00', '6 km']
	
Last two strings handle for better development. Please do not pay attention to this.
When you see they - save successful. Watch Show train for next step.

#### Show train
For show train from database you need to open 'show_trains.py' script to begin with.
Here will be the output of information about all workouts:

    01.01.2021 10:00:
    	Github drive
    	Duration: 42:00
    	Distance: 6 km

Thats all what you can do with this script as common user for now. Better functionality will be added in the future.


### State
Raw. In development.