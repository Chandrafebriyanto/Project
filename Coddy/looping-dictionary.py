# looping dictionary adalah struktur data yang memungkinkan kita untuk menyimpan pasangan kunci-nilai
# dan melakukan iterasi melalui pasangan tersebut. Ini sangat berguna untuk menyimpan data yang terkait
# dengan objek tertentu, seperti informasi karyawan dalam sebuah perusahaan.

def print_employee_details(employee_data):
    if len(employee_data) == 0:
            print("No data available")
            return
    else: 
        for key, value in employee_data.items():
            print(f"{key}: {value}")

employee_data = {"Alice": "HR", "Bob": "Engineering", "Diana": "Marketing"}
print_employee_details(employee_data)