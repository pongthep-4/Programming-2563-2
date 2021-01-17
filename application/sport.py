# pip install prettytable
from prettytable import PrettyTable
import sys
from datetime import datetime

database = {
    'system': {
        'sys_name': '  ระบบยืมคืนอุปกร์กีฬา',
        'sub': 'สถาบันเทคโนโลยีจิตรลดา',
        'type': '',
        'user_id': ''
    },
    'admin': {
        'username': 'cdti',
        'password': '1234',
        'datetime': ''
    },
    'user': {
        '6310301004': {
            'username': '6310301004',
            'password': '1234',
            'name': 'นายพงศ์เทพ นุชเวช',
            'status': '',
            'datetime': ''
        }
    },
    'equipment': {
        'ลูกวอลเลย์บอล': {
            'count': 10
        },
        'ลูกบาสเกตบอล': {
            'count': 7
        },
        'ลูกแบด': {
            'count': 20
        },
        'ไม้แบดมินตัน': {
            'count': 8
        }
    },
    'borrow': {
        '001': {
            'user_id': '6310301004',
            'equipment_id': 'ลูกวอลเลย์บอล',
            'count': 1,
            'datetime': '01/15/2021, 21:09:47',
            'return': '01/16/2021, 21:09:47',
            'status': False
        },
        '002': {
            'user_id': '6310301004',
            'equipment_id': 'ลูกวอลเลย์บอล',
            'count': 1,
            'datetime': '01/15/2021, 21:09:47',
            'return': '01/16/2021, 21:09:47',
            'status': False
        }
    }

}


def get_dt(t):
    now = datetime.now()
    if t == 1:
        return now.strftime("%H:%M:%S")
    elif t == 2:
        return now.strftime("%m/%d/%Y")
    elif t == 3:
        return now.strftime("%H%M%S")
    else:
        return now.strftime("%m/%d/%Y, %H:%M:%S")


def login(in_error):
    error = in_error
    Header()
    print("\n\n\t\t\t\t\t\t\t\t[1] เข้าสู่ระบบ\n")
    if error:
        print("\t\t\t\t\t\t[ ชื่อผู้ใช้และรหัสผ่านไม่ถูกต้อง ]\n")
        print("\t\t\t\t[ กรุณากรอกชื่อผู้ใช้และรหัสผ่านเพื่อเข้าสู่ระบบอีกครั้ง ]\n")
    else:
        print("\t\t\t\t\t\t[ กรุณากรอกชื่อผู้ใช้และรหัสผ่านเพื่อเข้าสู่ระบบ ]\n")
    error = False
    while True:
        username = input("ชื่อผู้ใช้ >>> ").strip()
        if username != '':
            break
    while True:
        password = input("รหัสผ่าน >>> ").strip()
        if password != '':
            break
    x = database['user'].keys()
    if username in x:
        if password == database['user'][username]['password']:
            database['system']['type'] = 'นักศึกษา'
            database['system']['user_id'] = str(username)
            database['user'][username]['datetime'] = get_dt(1)
            user()
        else:
            error = True
    else:
        error = True
    if error:
        login(True)


def user():
    Header()
    print("\n\n\t\t\t\t\t\t[ ยินดีต้อนรับเข้าสู่ระบบ ]\n")
    print("\t\t\t[1] ยืมอุปกรณ์ | [2] คืนอุปกรณ์ | [0] ออกจากระบบ\n\n")
    while True:
        fn = input("กรุณาเลือกฟังก์ชั่นการทำงาน >>> ").strip()
        if fn in ['1', '2', '3', '0']:
            if fn == '1':
                equipment(False)
                break
            elif fn == '2':
                Return(True)
                break
            elif fn == '3':
                profile()
                break
            else:
                database['system']['user_id'] = ''
                database['system']['type'] = ''
                Main()
                break


def profile():
    pass


def Return(status):
    Header()
    print("\n\t\t\t\t\t\t\t\t[1] คืนอุปกรณ์")
    if status:
        print("\t\t\t\t\t\t\t\t[ คืนอุปกรณ์สำเร็จ ]\n")
    data = database['borrow']
    n, m = 1, 1
    data_k = []
    table_t = PrettyTable(['ลำดับ', 'รายการ', 'จำนวน', 'วันเวลา (ยืม)', 'สถานะ'])
    table_f = PrettyTable(['ลำดับ', 'รายการ', 'จำนวน', 'วันเวลา (คืน)', 'สถานะ'])
    for i in data.keys():
        if data[i]['user_id'] == database['system']['user_id']:
            if data[i]['status']:
                table_t.add_row(
                    [f"[{n}]", data[i]['equipment_id'], data[i]['count'], data[i]['datetime'], "ยังไม่ได้คืน"])
                n += 1
                data_k.append(i)
            else:
                table_f.add_row([f"{m}", data[i]['equipment_id'], data[i]['count'], data[i]['return'], "คืนแล้ว"])
                m += 1
    print("<<< รายการที่ยืม >>>")
    print(table_t)
    print("[0] ออกจากระบบ ")
    print("\n<<< ประวัติการยืม >>>")
    print(table_f)
    while True:
        fn = input("กรุณาเลือกรายการที่จะคืน >>>").strip()
        if fn != '':
            print(list(range(1, n + 1)))
            if int(fn) in list(range(1, n + 1)):
                database['borrow'][data_k[int(fn) - 1]]['status'] = False
                database['borrow'][data_k[int(fn) - 1]]['return'] = get_dt(0)
                count1 = int(database['equipment'][database['borrow'][data_k[int(fn) - 1]]['equipment_id']]['count'])
                count2 = int(database['borrow'][data_k[int(fn) - 1]]['count'])
                database['equipment'][database['borrow'][data_k[int(fn) - 1]]['equipment_id']][
                    'count'] = count1 + count2
                Return(True)
                break
            elif fn == '0':
                user()
                break


def equipment(status):
    Header()
    print("\n\n\t\t\t\t\t\t\t\t[1] ยืมอุปกรณ์")
    if status:
        print("\t\t\t\t\t\t\t\t[ ยืมอุปกรณ์สำเร็จ ]\n")
    tmp = dict()
    while True:
        print("\n<<< รายการอุปกรณ์กีฬาทั้งหมด >>>")
        t = PrettyTable(['ลำดับ', 'รายการ', 'จำนวน'])
        data = database['equipment']
        data_key = list(database['equipment'].keys())
        i = 1
        for dt in data:
            t.add_row([f'[{i}]', str(dt), str(database['equipment'][dt]['count'])])
            i += 1
        print(t)
        print("[0] ย้อนกลับ")
        while True:
            fn = input("กรุณาเลือกรายการที่จะยืม >>> ").strip()
            if fn != '':
                if int(fn) in list(range(1, i + 1)) or fn == '0':
                    break
        if fn == '0':
            user()
            break
        while True:

            count = input("กรุณากำหนดจำนวนที่จะยืม >>> ")
            if count != '':
                if int(database['equipment'][data_key[int(fn) - 1]]['count']) - int(count) >= 0:
                    break
                else:
                    print("! จำนวนไม่ถูกต้อง")

        tmp.update({
            str(get_dt(3)): {
                'user_id': database['system']['user_id'],
                'equipment_id': data_key[int(fn) - 1],
                'count': str(count),
                'datetime': get_dt(0),
                'return': '',
                'status': True
            }
        })
        print("\n\n<<< รายการยืมของฉัน >>>")
        my_t = PrettyTable(['ลำดับ', 'รายการ', 'จำนวน(ยืม)', 'วันเวลา'])
        i = 1
        for dt in tmp:
            my_t.add_row([f'[{i}]', tmp[str(dt)]['equipment_id'], tmp[str(dt)]['count'], tmp[str(dt)]['datetime']])
            i += 1
        print(my_t)
        print("[1] ยืนยันรายการ | [2] เพื่มรายการ | [0] ยกเลิก\n")
        while True:
            fn = input("กรุณาเลือกฟังก์ชั่นการทำงาน >>> ").strip()
            if fn in ['0', '1', '2']:
                if fn == '1':
                    for i in tmp:
                        database['borrow'].update({i: tmp[i]})
                        database['equipment'][tmp[i]['equipment_id']]['count'] = int(
                            database['equipment'][tmp[i]['equipment_id']]['count']) - int(
                            database['borrow'][i]['count'])
                    equipment(True)
                    break
                elif fn == '0':
                    equipment(False)
                    break
                else:
                    break
        if fn != '2':
            break


def register():
    Header()
    print("\n\n\t\t\t\t\t\t\t\t[2] สมัครสมาชิค\n")
    print("\t\t\t\t\t\t[ กรุณากำหนดชื่อผู้ใช้และรหัสผ่านเพื่อสมัครสมาชิก ]\n")
    while True:
        name = input("กรุณากรอกชื่อ-นามสกุล: ").strip()
        if name != '':
            break
    while True:
        username = input("กรุณากรอกรหัสนักศึกษา: ").strip()
        if username != '':
            break
    while True:
        while True:
            password = input("กรุณากำหนดรหัสผ่าน: ").strip()
            if password != '':
                break
        while True:
            password2 = input("กรุณายืนยันรหัสผ่าน: ").strip()
            if password2 != '':
                break
        if password == password2:
            break
        else:
            print("!! รหัสผ่านไม่ตรงกัน")
    database['user'].update({
        username: {
            'username': username,
            'password': password2,
            'name': name,
            'status': '',
            'datetime': ''
        }
    })
    Header()
    print("\n\n\t\t\t\t\t\t\t\t[2] สมัครสมาชิค\n")
    print("\t\t\t\t\t\t\t\t[ สมัครสมาชิกสำเร็จ ]\n")
    print("\t\t\t\t\t\t[1] เข้าสู่ระบบ | [0] กลับสู่หน้าแรก \n")
    while True:
        fn = input("กรุณาเลือกฟังก์ชั่นการทำงาน >>> ").strip()
        if fn in ['1', '0']:
            if fn == '1':
                login(False)
                break
            else:
                Main()
                break


def admin():
    Header()
    print("\n\n\t\t\t\t\t\t[ ยินดีต้อนรับเข้าสู่ระบบ ]\n")
    print("\t\t\t[1] จัดการอุปกรณ์กีฬา | [2] รายชื่อผู้ใช้ | [3] ดูประวัติการยืม | [0] ออกจากระบบ\n\n")
    while True:
        fn = input("กรุณาเลือกฟังก์ชั่นการทำงาน >>> ").strip()
        if fn in ['1', '2', '3', '0']:
            if fn == '1':
                equipment_ad(False, '')
                break
            elif fn == '2':
                user_ad()
                break
            elif fn == '3':
                his_ad()
                break
            else:
                database['system']['user_id'] = ''
                database['system']['type'] = ''
                database['admin']['datetime'] = ''
                Main()
                break


def equipment_ad(status, tx):
    def eqm_cr():
        print("<<< 1 เพื่มอุปกรณ์ >>>")
        while True:
            name = input("ชื่ออุปกรณ์ : ").strip()
            if name != '':
                break
        while True:
            count = input("จำนวน : ").strip()
            if count != '':
                break
        database['equipment'].update({str(name): {'count': str(count)}})
        return True

    def eqm_edit(data_key):
        print("<<< 2 แก้ไขข้อมูล | [0] ยกเลิก >>>")
        while True:
            number = input("กรุณาเลือกอุปกร์เพื่อทำการแก้ไข : ").strip()
            if number != '' and number != '0':
                if int(number) in list(range(1, len(list(data_key)) + 1)):
                    break
            elif number == '0':
                return False
            break

        while True:
            name = input("ชื่ออุปกรณ์ : ").strip()
            if name != '':
                break
        while True:
            count = input("จำนวน : ").strip()
            if count != '':
                break
        n = list(data_key)
        database['equipment'].pop(n[int(number) - 1])
        database['equipment'].update({str(name): {'count': str(count)}})

        return True

    def eqm_del(data_key):
        print("<<< 3 ลบข้อมูล | [0] ยกเลิก >>>")
        while True:
            name = input("กรุณาเลือกอุปกร์เพื่อทำการลบ : ").strip()
            if name != '' and name != '0':
                if int(name) in list(range(1, len(list(data_key)) + 1)):
                    break
            elif name == '0':
                return False
            break

    Header()
    print("\n\t\t\t\t\t\t\t\t[1] จัดการอุปกรณ์กีฬา")
    if status:
        print(f"\t\t\t\t\t\t\t\t[ {tx} ]")
    while True:
        print("\n<<< รายการอุปกรณ์กีฬาทั้งหมด >>>")
        t = PrettyTable(['ลำดับ', 'รายการ', 'จำนวน'])
        data = database['equipment']
        data_key = list(database['equipment'].keys())
        i = 1
        for dt in data:
            t.add_row([f'[{i}]', str(dt), str(database['equipment'][dt]['count'])])
            i += 1
        print(t)
        print("[1] เพื่มอุปกรณ์ | [2] แก้ไข | [3] ลบ | [0] ย้อนกลับ")
        while True:
            fn = input("กรุณาเลือกฟังก์ชั่นการทำงาน >>> ").strip()
            if fn == '1':
                if eqm_cr(): equipment_ad(True, 'เพื่มข้อมูลสำเร็จ')
                break
            elif fn == '2':
                if eqm_edit(data_key):
                    equipment_ad(True, 'แก้ไขข้อมูลสำเร็จ')
                else:
                    equipment_ad(False, '')
                break
            elif fn == '3':
                if eqm_del(data_key):
                    equipment_ad(True, 'เพื่มข้อมูลสำเร็จ')
                else:
                    equipment_ad(False, '')
            elif fn == '0':
                admin()
                break


def user_ad():
    Header()
    print("\n\t\t\t\t\t\t\t\t[2] รายชื่อผู้ใช้")
    data = database['user']
    table = PrettyTable(['ลำดับ', 'รหัส', 'ชื่อ-นามสกุล'])
    n = 1
    for i in data.keys():
        table.add_row([f"{n}", data[i]['username'], data[i]['name']])
        n += 1
    print(table)
    print("[0] ออกจากระบบ ")
    while True:
        fn = input("กรุณาเลือกฟังก์ชั่นการทำงาน >>>").strip()
        if fn != '':
            if fn == '0':
                admin()
                break


def his_ad():
    Header()
    print("\n\t\t\t\t\t\t\t\t[3] ประวัติการยืม")
    data = database['borrow']
    n = 1
    table = PrettyTable(['ลำดับ', 'รหัสนักศึกษา', 'รายการ', 'จำนวน', 'วันเวลา (ยืม)', 'วันเวลา (คืน)', 'สถานะ'])
    for i in data.keys():
        if not data[i]['status']:
            table.add_row(
                [f"[{n}]", data[i]['user_id'], data[i]['equipment_id'], data[i]['count'], data[i]['datetime'],
                 data[i]['return'], "คืนแล้ว"])
        else:
            table.add_row(
                [f"[{n}]", data[i]['user_id'], data[i]['equipment_id'], data[i]['count'], data[i]['datetime'],
                 data[i]['return'], "ยังไม่ได้คืน"])
        n += 1
    print(table)
    print("[0] ออกจากระบบ ")
    while True:
        fn = input("กรุณาเลือกฟังก์ชั่นการทำงาน >>>").strip()
        if fn != '':
            if fn == '0':
                admin()
                break


def admin_login(in_error):
    error = in_error
    Header()
    print("\n\n\t\t\t\t\t\t\t\t[1] เข้าสู่ระบบ\n")
    if error:
        print("\t\t\t\t\t\t[ ชื่อผู้ใช้และรหัสผ่านไม่ถูกต้อง ]\n")
        print("\t\t\t\t[ กรุณากรอกชื่อผู้ใช้และรหัสผ่านเพื่อเข้าสู่ระบบอีกครั้ง ]\n")
    else:
        print("\t\t\t\t\t\t[ กรุณากรอกชื่อผู้ใช้และรหัสผ่านเพื่อเข้าสู่ระบบ ]\n")
    error = False
    while True:
        username = input("ชื่อผู้ใช้ >>> ").strip()
        if username != '':
            break
    while True:
        password = input("รหัสผ่าน >>> ").strip()
        if password != '':
            break
    if username == database['admin']['username'] and password == database['admin']['password']:
        database['system']['type'] = 'ผู้ดูแลระบบ'
        database['admin']['datetime'] = get_dt(1)
        admin()
    else:
        admin_login(True)


def Header():
    n = 80
    print("-" * n)
    print(f"\t\t\t\t\t\t\t{database['system']['sys_name']}")
    print(f"\t\t\t\t\t\t\t{database['system']['sub']}")
    print("-" * n)
    if database['system']['type'] != '':
        if database['system']['type'] == 'นักศึกษา':
            type = 'นักศึกษา'
            id = database['user'][str(database['system']['user_id'])]['username']
            name = database['user'][str(database['system']['user_id'])]['name']
            time = database['user'][str(database['system']['user_id'])]['datetime']
        else:
            type = 'ผู้ดูแลระบบ'
            id = ' - '
            name = database['admin']['username']
            time = database['admin']['datetime']
        print(f"ประเภทผู้ใช้: {type} | รหัส: {id} | ชื่อ: {name} | เข้าสู่ระบบเมื่อ: {time} ")
        print("-" * n)


def Main():
    Header()
    print("\n\n\t\t\t\t\t\t[ ยินดีต้อนรับเข้าสู่ระบบ ]\n")
    print("\t[1] เข้าสู่ระบบ | [2] สมัครสมาชิก | [3] ผู้ดูแลระบบ | [0] ออกจากโปรแกรม\n\n")

    while True:
        print("กรุณาเลือกฟังก์ชั่นการทำงาน >>> ")
        fn = input().strip()
        if fn in ['1', '2', '3', '0']:
            break
    if fn == '1':
        login(False)
    elif fn == '2':
        register()
    elif fn == '3':
        admin_login(False)
    else:
        sys.exit()


Main()
