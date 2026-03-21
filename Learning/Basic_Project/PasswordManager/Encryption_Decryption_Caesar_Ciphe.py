shift = 5

a_z = "abcdefghijklmnopqrstuvwxyz"
A_Z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s_c = "~!@#$%^&*()_-+={[}]:;'?/>.<,"
_n = "1234567890"

a_z_lst = list(a_z)
A_Z_lst = list(A_Z)
s_c_lst = list(s_c)
_n_lst = list(_n)

def ReturnMsg(encrypt: bool , msg: str):
    converted_msg = ""
    for m in msg:
        lst = []
        match m:
            case m if m in a_z_lst: 
                lst = a_z_lst.copy()
            case m if m in A_Z_lst:
                lst = A_Z_lst.copy()
            case m if m in s_c_lst:
                lst = s_c_lst.copy()
            case m if m in _n_lst:
                lst = _n_lst.copy()
            case _ : pass
        
        if encrypt:
            if lst:
                shifted_index = (shift + lst.index(m)) % len(lst)  # % len(lst) keeps the sum under 26 so when sum is example 29 26 is taken out of the sunm and 3 is left
                converted_msg += lst[shifted_index] # like 5 + 25 = 30 now 30 % 26 = 4
            else:
                converted_msg += m
        else:
            if lst:
                shifted_index = (lst.index(m) - shift) % len(lst) # if shifted index is -ve then 26 + that negative number %  does it 
                converted_msg += lst[shifted_index] # like 4-5 = -1 then -1 % 26 we get 25 again 
            else:
                converted_msg += m
    
    return converted_msg

def Encrypt(msg: str):
    return ReturnMsg(True,msg)
                
def Decrypt(encrypted_msg: str): 
    return ReturnMsg(False,encrypted_msg)
