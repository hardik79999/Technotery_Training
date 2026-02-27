"""
## Employee Attendance System

Create a command-line program that helps the HR department check daily employee attendance.

## Create a Master Employee List

* Make a fixed list of all company employees.
* This list should NOT change while the program runs.
* Example:

  ```
  ["John", "Sarah", "Michael", "Emma", "David"]
  ```

---

##  Create Daily Check-in Logs (Messy Data)

* Create a list that shows employee names with their check-in times.
* Some time entries should be correct.
* Some entries should be wrong or broken (invalid format).

Example:

```
[
  ("John", "08:50 AM"),
  ("Sarah", "09:15 AM"),
  ("Michael", "bad time"),
  ("Emma", "09:00 AM"),
  ("David", "25:61 PM")
]
```

---

##  Build an Interactive Menu

The program should keep running until the user chooses to exit.

Example menu:

```
1. Process Today’s Attendance Logs
2. View Attendance Report
3. Exit
```

* The program should repeat the menu after every action.
* It should only stop when the user selects "Exit".


## Process the Logs

When the user selects **Process Logs**, the program must:

1. Convert the time strings (like `"08:50 AM"`) into real time values.
2. Handle invalid or corrupted times without crashing.

   * If time is wrong, mark it as "Invalid Time".
3. Categorize valid check-ins:

   * Before 9:00 AM → **Early**
   * Exactly 9:00 AM → **On-Time**
   * After 9:00 AM → **Late**


## Find Absent Employees

* Compare the check-in list with the master employee list.
* If someone from the master list did NOT check in at all, mark them as **Absent**.



## Calculate Average Check-in Time

* Use only valid check-in times.
* Calculate the average time.
* Round it properly (normal math rounding).
* Display it in time format (example: 09:05 AM).


## Show Daily Attendance Report

The report should show:

* Each employee’s name
* Their check-in time
* Their status (Early / On-Time / Late / Invalid / Absent)
* The average check-in time

Example output:

```
Daily Attendance Report
-----------------------
John     - 08:50 AM - Early
Sarah    - 09:15 AM - Late
Michael  - Invalid Time
Emma     - 09:00 AM - On-Time
David    - Invalid Time

Absent: None

Average Check-in Time: 09:01 AM
```

---

## Important Rules

* The program must NOT crash because of bad time data.
* The menu must keep running until the user exits.
* Use proper time parsing (like datetime in Python).
* Keep the code clean and organized.


"""


from datetime import datetime
current_time = datetime.now().time()

office_time = 10.00
fix_time = []
Employee_Time = {}
status = True
while status:


    def Process_TodaysAttendance_Logs():
        Employee_List = ["John", "Sarah", "Michael", "Emma", "David"]
    
        for emp in Employee_List:
            e = input(f"{emp} Enter Your Time : " )
            mode = input(f"{emp} Enter like (AM) : (PM) : ").upper()
            e = e.replace(":",".")
            Employee_Time[emp] = e,mode
        print(Employee_Time)


    def View_Attendance_Report():
        for i in Employee_Time.items():
            fix_time.append(i)

        check = dict(fix_time)
        s = 0
        print("---------------------------------") 
        for k , v in check.items():
            
            if office_time > float(v[0]):
                
                s += float(v[0])
                if v[1] == "AM" and 10.00 > float(v[0]): 
                    print(f"{k} : {v} Early ")

                if office_time == float(v[0]):
                    print(f"{k} : {v} On-Time ")
                
            else:
                print(f"{k} : late")
        avg = s / len(k)
        print(f"Average Check-in Time", avg)
        print("---------------------------------") 


    menu = """
                MENU :::
            1. Process Today’s Attendance Logs
            2. View Attendance Report
            3. Exit

    """
    print(menu)

    choice = int(input("Enter Your choice : "))

    if choice == 1:
        Process_TodaysAttendance_Logs()
    elif choice == 2:
        View_Attendance_Report()
    elif choice == 3:
        status = False



