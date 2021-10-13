import json
from datetime import date

def dob(DOB):
    # calculate age of employee
    year, month, day = map(int, DOB.split('-'))
    age = (date.today() - date(year, month, day)).days // 365
    return age


class Employee:
    def __init__(self, file="json_file.json"):
        self.file_name = file
        with open(self.file_name) as file_json:
            data_file = json.load(file_json)
        file_json.close()

        self.Admin_keys = [i for i in data_file.keys()
                           if str(data_file[i][0]["user_type"]).lower()
                           == "Admin".lower()]  # adding add admin Keys

    def write_json(self, data_file):
        # writing add data in add,update,delete
        with open(self.file_name, "w") as file:
            json.dump(data_file, file, indent=2)
        file.close()

    def add_data(self, user_id, name, user_type, joining_date, DOB, age, phone_no,
                 project_name, skill_set, exprience):

        # To add new record of Employee

        with open(self.file_name) as file:
            data = json.load(file)
        file.close()

        data[user_id] = [{"name": name, "user_type": user_type, "joining_date": joining_date
                             , "DOB": DOB, "age": age, "project_name": project_name
                             , "skill_set": skill_set, "phone_no": phone_no
                             , "exprience": exprience}]

        self.write_json(data)

    def update_data(self, case, user_id, info=None):  # update employee data
        with open(self.file_name) as file:
            data = json.load(file)
        file.close()

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

    def delete_data(self, user_id):  # delete employee data from json file
        with open(self.file_name) as file:
            data = json.load(file)
        file.close()

        boolean = data.pop(user_id, False)

        if not boolean:
            print("Data Not Found!!!")
        else:
            self.write_json(data)
            print('Record Deleted successfully...')

    def read_data(self):  # read all data except Admin user_type from json file
        with open(self.file_name) as file:
            data = json.load(file)
        file.close()

        for count, user_key in enumerate(data.keys()):
            data_return = data[user_key][0]

            if str(data_return["user_type"]).lower() != "Admin".lower():
                print('Record --> ', count+1)  # count of employee

                for key, value in zip(data_return.keys(), data_return.values()):
                    print(key, ":", value)
                print()

