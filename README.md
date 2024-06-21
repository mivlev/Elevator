# OA / SMX Elevator project

## Usage instructions
* Install dependencies

```
pip install -r requirements.txt
```

* Run using the following command. starting floor should be an integer and floors to visit 
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


```mermaid
sequenceDiagram
    participant dotcom
    participant iframe
    participant viewscreen
    dotcom->>iframe: loads html w/ iframe url
    iframe->>viewscreen: request template
    viewscreen->>iframe: html & javascript
    iframe->>dotcom: iframe ready
    dotcom->>iframe: set mermaid data on iframe
    iframe->>iframe: render mermaid
```