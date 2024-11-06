# ICS-exporter

## 1 Use
### 1.1 Install
Install the necessary libraries
```python
pip install -r requirements.txt
```

### 1.1 Events
Put the events in a .json file called `events.json` in the same directory as `main.py`.
#### Example
```json
[
    {
        "title": "MyEvent",
        "start": "2030-01-01 00:00",
        "end": "2030-12-31 23:59",
        "location": "Lausanne, suisse"
    }
]
```

### 1.2 Run the script
Simply run the script. it will create a file `events.ics` in the directory
