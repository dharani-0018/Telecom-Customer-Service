import random

customer_name = input("Enter Customer Name: ")
mobile_number = input("Enter Mobile Number: ")
address = input("Enter Address: ")

balance = 100
bill = 450
plan = "Unlimited Calls + 2GB/day"
sim_status = "Active"
sim_number = "SIM123456"

complaint = ""
complaint_status = "No Complaint"

call_history = [
    ("9876543210", "Outgoing", "12 mins"),
    ("9123456780", "Incoming", "5 mins"),
    ("9988776655", "Missed", "0 mins")
]

data_usage = [
    ("Monday", "1.2 GB"),
    ("Tuesday", "850 MB"),
    ("Wednesday", "2.0 GB"),
    ("Thursday", "700 MB"),
    ("Friday", "1.5 GB")
]

sms_history = [
    ("9876543210", "Sent"),
    ("9123456780", "Received"),
    ("9988776655", "Sent")
]

while True:
    print("\n========== TELECOM CUSTOMER SERVICE ==========")
    print("1. Customer Details")
    print("2. Check Balance")
    print("3. Recharge")
    print("4. View Current Plan")
    print("5. Change Plan")
    print("6. Pay Bill")
    print("7. Raise Complaint")
    print("8. Complaint Status")
    print("9. Activate/Deactivate SIM")
    print("10. SIM Replacement")
    print("11. Call History")
    print("12. Data Usage History")
    print("13. SMS Usage History")
    print("14. Internet Speed Test")
    print("15. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"\nName: {customer_name}")
        print(f"Mobile: {mobile_number}")
        print(f"Address: {address}")
        print(f"SIM Status: {sim_status}")
        print(f"SIM Number: {sim_number}")

    elif choice == 2:
        print("Available Balance: ₹", balance)

    elif choice == 3:
        amount = int(input("Enter Recharge Amount: ₹"))
        balance += amount
        print("Recharge Successful!")
        print("Updated Balance: ₹", balance)

    elif choice == 4:
        print("Current Plan:", plan)

    elif choice == 5:
        print("1. ₹199 - 28 Days")
        print("2. ₹299 - 56 Days")
        print("3. ₹399 - 84 Days")
        p = int(input("Select Plan: "))
        if p == 1:
            plan = "₹199 Plan - 28 Days"
        elif p == 2:
            plan = "₹299 Plan - 56 Days"
        elif p == 3:
            plan = "₹399 Plan - 84 Days"
        else:
            print("Invalid Plan")
            continue
        print("Plan Updated Successfully.")

    elif choice == 6:
        print("Current Bill: ₹", bill)
        pay = int(input("Enter Amount to Pay: ₹"))
        if pay >= bill:
            bill = 0
            print("Bill Paid Successfully.")
        else:
            bill -= pay
            print("Remaining Bill: ₹", bill)

    elif choice == 7:
        complaint = input("Enter Complaint: ")
        complaint_status = "Under Process"
        print("Complaint Registered Successfully.")

    elif choice == 8:
        print("Complaint:", complaint if complaint else "No Complaint")
        print("Status:", complaint_status)

    elif choice == 9:
        if sim_status == "Active":
            sim_status = "Inactive"
            print("SIM Deactivated Successfully.")
        else:
            sim_status = "Active"
            print("SIM Activated Successfully.")

    elif choice == 10:
        reason = input("Enter Reason (Lost/Damaged): ")
        if sim_status == "Active":
            sim_number = "SIM" + str(random.randint(100000, 999999))
            print("SIM Replacement Successful.")
            print("New SIM Number:", sim_number)
            print("Reason:", reason)
        else:
            print("SIM is inactive. Activate it first.")

    elif choice == 11:
        print("\n----- CALL HISTORY -----")
        for number, ctype, duration in call_history:
            print(f"Number: {number} | Type: {ctype} | Duration: {duration}")

    elif choice == 12:
        print("\n----- DATA USAGE HISTORY -----")
        for day, data in data_usage:
            print(f"{day}: {data}")

    elif choice == 13:
        print("\n----- SMS HISTORY -----")
        for number, status in sms_history:
            print(f"Mobile: {number} | Status: {status}")

    elif choice == 14:
        download = round(random.uniform(20, 120), 2)
        upload = round(random.uniform(10, 60), 2)
        ping = random.randint(5, 40)
        print("\n----- INTERNET SPEED TEST -----")
        print(f"Download Speed: {download} Mbps")
        print(f"Upload Speed: {upload} Mbps")
        print(f"Ping: {ping} ms")

    elif choice == 15:
        print("Thank you for using Telecom Customer Service.")
        break

    else:
        print("Invalid Choice. Please try again.")
