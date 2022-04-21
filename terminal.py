import pickle
import random
import webbrowser

SCP_MAX = 5000
MAX_LENGTH_CREDENTIAL = 50

def get_scp_url(scp_num):
    'Changes url/number at the end to get correct site link. Returns string'
    if scp_num < 1: #unique handling for 0th entry
        return "http://www.scp-wiki.net/scp-000";
    elif scp_num < 10: 
        return "http://www.scp-wiki.net/scp-00"
    elif scp_num < 100:
        return "http://www.scp-wiki.net/scp-0"
    else: return "http://www.scp-wiki.net/scp-"

def search_scp():
    while True:
        print('\'0\' TO RETURN TO MENU')
        u_input = int(input('SCP NUMBER: '))
        if (u_input > SCP_MAX or u_input < 0):
            print("OUT OF BOUND NUMBER. RANGE: 0 - 5000")
            continue;
        return u_input

def create_account(user):
    'Create an account'
    print("-STORING ACCOUNT INFORMATION-")
    try:
        with open('accounts.txt', 'rb') as file_handle:
            accounts = pickle.load(file_handle)
        accounts.append(user)
        file_handle.close()
        with open('accounts.txt', 'wb') as file_handle:
            pickle.dump(accounts, file_handle)
        return True
    except:
        print("CRITICAL ERROR")
        return False

def credentials(user): 
    try:
        with open('accounts.txt', 'rb') as file_handle:
            accounts = pickle.load(file_handle)
        if user in accounts:
            print("-ACCESS GRANTED-")
            return True
        print("-ACCESS DENIED-")
        return False
    except:
        'Only first time, if no accounts were found'
        print("NO ACCOUNTS FOUND, NEW SYSTEM DETECTED")
        print("ADMINISTRATIVE ACCOUNT CREATED")
        accounts = list()
        accounts.append(user)
        with open('accounts.txt', 'wb') as file_handle:
            pickle.dump(accounts, file_handle)
        return True
    
def terminal_selection():
    while True:
        print("MENU:\n0. EXIT\n1. SEARCH SCP\n2. RANDOM SCP\n3. KETER LIST\n4. EUCLID LIST\n5. SAFE LIST\n6. THAUMIEL LIST\n7. REDACTED")
        num_select = int(input("OPTION NUMBER: "))
        if num_select == 0:
            return
        if num_select == 1:
            scp_num = search_scp()
            url = get_scp_url(scp_num)
            url += str(scp_num)
            webbrowser.open(url)
        if num_select == 2:
            print("RETURNING RANDOM ENTRY")
            scp_num = random.randrange(0, SCP_MAX+1)
            url = get_scp_url(scp_num)
            url += str(scp_num)
            webbrowser.open(url)
        if num_select == 3:
            print("-KETER LIST-")
        if num_select == 4:
            print("-EUCLID LIST-")
        if num_select == 5:
            print("-SAFE LIST-")
        if num_select == 6:
            print("-THAUMIEL LIST-")
        if num_select == 7:
            print("REDACTED - O5 ONLY")

if __name__ == '__main__':
    log_in = False
    print("SCP DATABASE V0.1")
    while True:
        print("0. CREATE NEW ACCOUNT")
        print("1. LOG IN")
        try: 
            u_selection = int(input("Selection: "))
            break;
        except: pass

    print("ENTER CREDENTIALS")
    while (log_in == False):
        u_name = input("ACCOUNT NAME: ")
        u_pass = input("ACCOUNT PASSWORD: ")
        user = [u_name, u_pass]
        if u_selection == 0:
            log_in = create_account(user)
        elif u_selection == 1:
            log_in = credentials(user)
    terminal_selection()

