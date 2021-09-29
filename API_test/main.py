import sqlite3
from flask import Flask, request, jsonify


def connection():
    conn = sqlite3.connect('json_file.db')
    return conn


def found(id):
    conn = connection()
    check_query = f"select emp_id from emp_details where emp_id ={id}"  # check emp_id in DB
    cur = conn.execute(check_query)
    return cur.fetchone()


app = Flask(__name__)


@app.route('/')  # defining url like /
def main():
    return jsonify({'massage': "main page..."})


@app.route('/insert', methods=['POST'])  # defining url like /insert , receive from postman tool
def insert():
    if request.method == 'POST':
        data = request.get_json()  # loading record from postman
        # print(data)
        emp_id = list(data.keys())[0]
        # print(emp_id)

        ds = list(data.values())[0]
        print(ds[0])
        ds = ds[0]

        query = f"""insert into emp_details values('{emp_id}','{ds["emp_name"]}','{ds["user_type"]}','
                {ds["year_exp"]}','{ds["joining_date"]}',
                '{ds["date_birth"]}','{ds["age"]}','{ds["project_name"]}','{ds["skill_set"]}');"""

        #  f"{value}" formate for query

        conn = connection()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        return jsonify({"Request": "Successfully Save"})


@app.route('/update', methods=['PUT'])  # PUT use in updating and adding new records
def update():
    update_data = request.get_json()  # receive data in json(dictionary) formant...
    id = dict(update_data).pop("emp_id")
    to_update = str(update_data).replace(':', '=')
    print(to_update)
    r = found(id)

    if r is not None:
        # if id found in database then update else return
        query = f"update emp_details set" + to_update[1:len(to_update) - 1] + f"where emp_id ={id}"
        # print(query)
        conn =connection()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        return jsonify({"Record": "Employee data Updated..."})
    else:
        return jsonify({"Record": "Employee data not Found..."})


@app.route('/delete', methods=["DELETE"])
def delete():
    # for delete --> (postman tool) json like {"emp_id":123}

    data = request.get_json()
    emp_id = data["emp_id"]

    check_record = found(emp_id)
    if check_record is None:
        return jsonify({"Request": "No Record to Delete..."})

    query = f"delete from emp_details where emp_id = '{emp_id}'"
    con = connection()
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    return jsonify({"Request": "Record Successfully Delete..."})


@app.route('/select', methods=['GET'])
def select():
    keys = ['emp_id', 'emp_name', 'user_type', 'year_exp', 'joining_date', 'date_birth', 'age', 'project_name',
            'skill_set']
    query = f"select * from emp_details where lower(user_type) != lower('Admin')"
    conn = connection()
    cur = conn.cursor()
    cur.execute(query)
    return_data = cur.fetchall()
    print(return_data)
    json = {}
    count =1
    for i in return_data:
        ds = {}
        for k, v in zip(keys, i):
            ds[k] = v
        json[count] = ds
        count+=1

    conn.commit()

    return jsonify(json)


app.run(debug=True)
