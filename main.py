import json


def dob(DOB):
    # calculate age of employee
    from datetime import date
    year, month, day = map(int, DOB.split('-'))
    age = (date.today() - date(year, month, day)).days // 365
    return age


class Employee:
    def __init__(self):
        self.file_name = "json_file.json"
        file = open(self.file_name)
        data = json.load(file)
        self.Admin_keys = [i for i in data.keys()
                           if str(data[i][0]["user_type"]).lower()
                           == "Admin".lower()]    # adding add admin Keys

    def write_json(self, data):
        # writing add data in add,update,delete
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=2)

    def add_data(self, user_id, name, user_type, joining_date, DOB, age, phone_no,
                 project_name, skill_set, exprience):

        # To add new record of Employee

        with open(self.file_name) as file:
            data = json.load(file)

        data[user_id] = [{"name": name, "user_type": user_type, "joining_date": joining_date
                             , "DOB": DOB, "age": age, "project_name": project_name
                             , "skill_set": skill_set, "phone_no": phone_no
                             , "exprience": exprience}]

        self.write_json(data)

    def update_data(self, case, user_id, info=None): # update employee data
        with open(self.file_name) as file:
            data = json.load(file)

        temp_dict = {1: 'name', 2: 'user_type', 3: 'exprience', 4: 'joining_date',
                     5: 'DOB', 6: 'phone_no', 7: 'project_name', 8: 'skill_set',
                     9: 'age'}

        if 1 <= case <= 6:
            dict_data = data[user_id]
            dict_data[0][temp_dict[case]] = info  # find out dict Keys
            if case == 5:
                dict_data[0][temp_dict[9]] = dob(info)

        elif 7 <= case <= 8:
            dict_data = data[user_id]
            return_list = dict_data[0][temp_dict[case]]
            for insert_data in info.split(','):
                return_list.append(insert_data)
        self.write_json(data)
        print('Record Updated successfully...')

    def delete_data(self, user_id): # delete employee data from json file
        with open(self.file_name) as file:
            data = json.load(file)

        boolean = data.pop(user_id, False)

        if not boolean:
            print("Data Not Found!!!")
        else:
            self.write_json(data)
            print('Record Deleted successfully...')

    def read_data(self): # read all data except Admin user_type from json file
        with open(self.file_name) as file:
            data = json.load(file)

        for user_key in data.keys():
            data_return = data[user_key][0]

            if str(data_return["user_type"]).lower() != "Admin".lower():

                for key, value in zip(data_return.keys(), data_return.values()):
                    print(key, ":", value)
                print()


obj = Employee() # creating obj of Employee class
while True:
    print(end='\n')
    print("1 - Add an employee record.")
    print("2 - Update an employee record.")
    print("3 - Delete an employee record.")
    print("4 - Read an employee record.")
    print("5 - Exit.")

    choice = int(input("Enter your choice :"))
    if choice == 1:
        print('\n**** Adding new employee record* ***')

        user_id = input("Enter Employee ID:")
        name = input("Enter Employee Name: ")
        user_type = input("Enter Employee User type: ")

        skill_sets = list(map(str, input("Skill (separated by ,): ").split(',')))
        joining_date = input("Enter Joining Date (yyyy-mm-dd): ")
        DOB = input("Enter Date of birth (yyyy-mm-dd): ")

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
        cho = int(input("Enter Your Choice: "))

        print('\n**** Updating an employee record ****')
        id = input("Enter Your Employee ID: ")

        temp_dict = {1: 'name', 2: 'user_type', 3: 'exprience', 4: 'joining_date',
                     5: 'DOB', 6: 'phone_no', 7: 'project_name', 8: 'skill_set'}

        data = input(f"Enter updated {temp_dict[cho]}: ")
        try:
            if data == " ":
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
        print('**** List of Employee records ****')
        obj.read_data()

    elif choice == 5:
        exit(0)
    else:
        print("Enter Right choice")
