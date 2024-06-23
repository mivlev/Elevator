# OA / SMX Elevator Project

## Usage Instructions
* Install dependencies

```
pip install -r requirements.txt
```
1. Navigate to the 'src' directory

2. Run the following command in a terminal. starting floor should be an integer and floors to visit 
should be a comma separated list of integers.
```
python Elevator.py <starting floor> <floor1,floor2,...,floor_n>
```

Example usage:
```
python Elevator.py 15 2,6,12,18,22,1
```

## Assumptions
* Goal is to maximize elevator efficiency by minimizing travel time.
* Implementation for a single elevator.