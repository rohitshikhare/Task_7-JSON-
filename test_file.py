from main import Employee, dob
import json

obj = Employee()  # creating obj of Employee class
while True:
    print(end='\n')
    print("1 - Add an employee record.")
    print("2 - Update an employee record.")
    print("3 - Delete an employee record.")
    print("4 - Read an employee record.")
    print("5 - Exit.")

    choice = int(input("Enter your choice :"))
    if choice == 1:

        with open('json_file.json') as file:
            data = json.load(file)
        file.close()

        print('\n**** Adding new employee record* ***')

        user_id = input("Enter Employee ID:")

        if user_id in data.keys():
            print('Employee id already Found...')
            continue

        name = input("Enter Employee Name: ")
        user_type = input("Enter Employee User type: ")
        skill_sets = list(map(str, input("Skill (separated by ,): ").split(',')))
        joining_date = input("Enter Joining Date (yyyy-mm-dd): ")
        DOB = input("Enter Date of birth (yyyy-mm-dd): ")

            # print(data.keys())
        if user_type in data.keys():
            print('Employee id already Found...')
            continue
        try:
            age = dob(DOB)
        except:
            print("Please Enter Correct Date of birth...")
            continue

        project_name = list(map(str, input("Enter Project Name (separated by ,): ").split(',')))
        phone_no = input("Enter Phone Number: ")
        expr = input("Enter years of experience: ")
        try:
            obj.add_data(user_id, name, user_type, joining_date, DOB, age, phone_no
                         , project_name, skill_sets, expr)
        except:
            print("Enter Valid Details...")
            continue

        print("Record Successfully Save...")

    elif choice == 2:

        print('\n**** Updating an employee record ****')
        id = input("Enter Your Employee ID: ")

        temp_dict = {1: 'name', 2: 'user_type', 3: 'exprience', 4: 'joining_date',
                     5: 'DOB', 6: 'phone_no', 7: 'project_name', 8: 'skill_set'}

        while True:
            print()
            # print("1 - user id: ") assumed user id is permanent i.e not changeable
            print("1 - Update Employee Name: ")
            print("2 - Update Employee Type: ")
            print("3 - Update Years of experience")
            print("4 - Update Joining date (yyyy-mm-dd)")
            print("5 - Update Date of birth (yyyy-mm-dd): ")
            print("6 - Update Phone Number: ")
            print("7 - Add Project name: ")
            print("8 - Add Skill sets")
            print("9 - Exit from Update: ")
            cho = int(input("Enter Your Choice: "))

            if cho ==9:
                break

            if 0 >= cho or cho >= 9:
                print('please enter right choice...')
                continue



            data = input(f"Enter updated {temp_dict[cho]}: ")
            try:
                if data != "":
                    obj.update_data(cho, id, data)
                else:
                    print('You Enter Null value...')
                    continue
            except:
                print("Please Enter Right employee id...")

    elif choice == 3:
        print('\n****Deleting an employee record****')
        user_id = input("Enter Employee ID:")
        obj.delete_data(user_id)

    elif choice == 4:
        print('**** List of Employee records ****\n')
        obj.read_data()

    elif choice == 5:
        exit(0)
    else:
        print("Enter Right choice")
