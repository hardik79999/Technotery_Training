"""
##  Task Overview

The marketing team receives very large, messy text files full of random data.
Your task is to build a small application that extracts **only valid email addresses** and exports them into a clean JSON file.

##  What You Need To Do

1. **Set up a local virtual environment**

   * Create and activate a virtual environment.
   * Install and use a standard code formatter (e.g., `black`).
   * Format your final script before submitting.

2. **Use the provided messy text file**

   * The file will contain random text, names, phone numbers, broken emails, and valid emails.
   * Assume the file could be extremely large (GB-sized).

3. **Extract only valid email addresses**

   * Ignore invalid or broken email patterns.
   * Only return properly formatted emails.

4. **Process the file safely**

   * Do NOT load the whole file into memory.
   * Read and process it step-by-step (sequentially).

5. **Store emails efficiently**

   * Use a strictly typed and memory-efficient structure.
   * Avoid duplicates.

6. **Export results**

   * Save the cleaned email list into a standardized `.json` file.
   * The output must be easy for another system to read.



## 📦 Final Deliverables

* The formatted Python script
* Instructions to run it
* The generated `.json` output file


sample text file:

=== CUSTOMER DATA EXPORT ===
Generated: 2026-01-14 03:44:22
Server: prod-node-77x

John Doe | Sales Lead | 555-123-9999 | johndoe@gmail.com
Random note: call after 5pm lorem ipsum blah blah ###$$$

ID#8821 -- Name: Jane Smith
Phone: (444) 222-1111
Email: jane_smith@company.org
Status: ACTIVE!!!

SystemLog>> 2026-01-01 ERROR user@@domain.com failed login attempt
Temp contact: mike.tyson@boxing.com $$$ revenue: 9000000

----- RANDOM BLOCK -----
notanemail@
something@wrong
@nouser.com
test@com
test@.com
user#domain.com
hello there this is garbage text

Customer Record:
Sarah Connor | 123-444-8888 | sarah.connor1984@future.net
Notes: prefers email contact only.

!!! ALERT !!!
admin@server.local logged in from 10.0.0.22
backup-email: support.team@enterprise.co.uk
Secondary: support.team@enterprise.co.uk

Marketing List 2025:
alex99@yahoo.com, emily.clark@outlook.com, fake@@mail.com
Promo contact: test.user+promo@gmail.com

DATA ENTRY:
Name: Robert Brown
Phone: 777-888-9999
Email: robert_brown123@hotmail.com
Extra: random text random text 123123 !!!

Broken entries:
anotherfake@domain
email.com
plainaddress
missingatsign.com

Log Dump 04:33:21
customer1@business.io SUCCESS
customer2@business.io SUCCESS
customer2@business.io SUCCESS
error user@.invalid

Support Tickets:
Ticket#44321 - Contact: helpdesk@tech-support.net
Ticket#44322 - Contact: billing@finance-dept.org
Ticket#44323 - Contact: invalid@email

Internal Notes:
CEO: ceo.office@corporate.com
HR: hr_department@corporate.com
IT: it-admin@corporate.com

Random Text Block Start
asdfghjkl qwertyuiop zxcvbnm
555-000-1111 666-222-3333
blah blah blah lorem ipsum
customer.service@my-company.com
sales-team@my-company.com
info@my-company
bad@company,com
good.email123@valid-domain.com
Random Text Block End

=== END OF FILE ===
20 walteg
12 mpr
"""
import re
import os
import json


def myfun(input, output_folder):

   email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
   number_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

   Email = []

   with open(input, "r") as i_file:
      for i in i_file:
         match = email_pattern.findall(i)
         for find in match:
            if find.lower() not in Email:
               Email.append(find.lower())

   number = []

   with open(input, "r") as i_file:
      for i in i_file:
         valid = number_pattern.findall(i)
         for p in valid:
            if p not in number:
               number.append(p)

   Original_Email = sorted(Email)
   Original_phone_number = sorted(number)

   DATA = {
      "EMAIL": Original_Email,
      "PHONE": Original_phone_number
   }


   with open(output_folder, "w") as o_file:
      json.dump(DATA, o_file, indent=4)

   print("Total Email : ", len(Original_Email))
   print("Total Number : ", len(Original_phone_number))
   print("Saved To : ", output_folder)



myfun("random.txt", "result.json")








# import re
# import json


# def Email_finder(input,output):
#    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    
#    Email = []

#    with open(input,"r") as i_file:
#       for i in i_file:
#          match = email_pattern.findall(i)
#          for find in match:
#             if find not in Email:
#                Email.append(find.lower())

#    Original_Email = sorted(Email)

#    with open(output,"w") as o_file:
#       json.dump(Original_Email,o_file,indent=4)


#    print("Total Email : ",len(Original_Email))
#    print("Save To ",output)

# Email_finder("random.txt","result.json")


# def Phone_number_finder(input,output):
#    number_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

#    number = []

#    with open(input,"r") as i_file:
#       for i in i_file:
#          valid = number_pattern.findall(i)
#          for p in valid:
#             if p not in number:
#                number.append(p)


#    Original_phone_number = sorted(number)

#    with open(output,"w") as p_file:
#       json.dump(Original_phone_number,p_file,indent=4)

#    print("Total Number : ",len(Original_phone_number))
#    print("Save To : ",output)
 

# Phone_number_finder("random.txt","result.json")