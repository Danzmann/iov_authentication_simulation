# STEP-1
# AT USER END
# V = Vehicle
# IDV = Identity of Vehicle set by user
# PWi = Password of Vehicle set by user
# ni = random number
# H0 = Hash Function

# STEP-2
# AT TRUST AUTHORITY END
# TA = Trust Authority
# Treg = Request Registration Time

# PVIDvi(Hash function of vechile 1(i = 1) ID) = H0(IDvi)
# Ai = H0(H0(PWi||ni)||PVIDvi)
# Ni = H0(PWi||ni) XOR H0(x||PVIDvi||Treg)

# from random import seed
from random import randint
import getpass
import time

Vechicle_1_user = input('Enter Name of Vehicle 1 User: ')
Vehicle = 1
IDV = input('Enter Vehicle 1 ID: ')
PWi = getpass.getpass(prompt='Enter Password')

# secret server is s

s = 169  # DUMMY VALUES

# generator is g, (I have to search cycle_group on wikipedia to understand better)

g = 189  # DUMMY VALUES

# sat

p = 133  # DUMMY VALUES

# This is in case it is required to use a random number, randomly generated instead of input
# seed(10)
# random_no = randint(0,100)
# print(random_no)
# print('Generating Random Number : ni')
# time.sleep(2)
rand_no = input('Enter a Random No. : ')  # str(random_no)
PWi_ll_ni = PWi + str(rand_no)
# print(PWi_ll_ni)
print('Concatenating Password and Random Number')
time.sleep(1)
print('\n''PWi||ni = ' + PWi_ll_ni)

# Generating Hash Function
hash_find = hash(PWi_ll_ni)

print('Generating Hash Function for Password and Random Number')
time.sleep(1)
print('\n''IDV, H0(PWi||ni)' + str(hash_find))

print('Communicating with Trust Authority for User Registration')
time.sleep(1)

# Process at Trust Authority
Treg = 0.2  # It is registration request time, as this time depends on the real time system speed and it will be in mili seconds so we are considering 0.2 mili seconds
print('\n'f'Registration Request time : {Treg}')
# Now TA will computes following things.
# PVIDvi = H0(IDvi oR say IDV in our case)

hash_IDV = hash(IDV)
# Now calculating Ai = H0(H0(PWi||ni)||PVIDvi)
hash_Ai_sub = str(hash_find) + str(hash_IDV)
# print(hash_find)
# print(hash_IDV)
# print(int(hash_Ai_sub))

hash_Ai = hash(hash_Ai_sub)

# print(hash_Ai)

# x = private key of TA and y = public key of TA
x = 1
y = g ** x
x_hash = hash(x)
y_hash = hash(y)

# x||H0(IDV)||Treg
x_PVIDvi_Treg = str(x_hash) + str(hash_IDV) + str(Treg)
last_hash_Ni = hash(x_PVIDvi_Treg)
# print(hash_find)
# print(last_hash_Ni)
# print(int(hash_find)^int(last_hash_Ni)) # Ni calculatiion by taking XOR

Ni = int(hash_find) ^ int(last_hash_Ni)
print('Trust Authority Computing Attributes')
time.sleep(1)
print('\n''PVIDVi = ' + str(hash_IDV))
print('\n''Ai = ' + str(hash_Ai))
print('\n''Ni = ' + str(Ni))
print('\n''Trust Authority Issuing Data to Smart Card')
print(
    '\n'f'Ai = {hash_Ai}''\n'f'Ni = {Ni}''\n'f'g = {g}''\n'f'p = {p}''\n'f'y = {y}''\n'f'H0 = {hash_find}''n'f'H1 = {hash_IDV}''\n'f'H2 = {hash_Ai}'f'H3 = {last_hash_Ni}')
time.sleep(1)
print('\n''Trust Authority sending Card to Vehicle')
time.sleep(1)
print('\n''User Successfully Regisreted in the System')
# raw_input = raw_input('Press any key to continue')
time.sleep(1)
print('\n''Enter login detail!''\n')
time.sleep(1)

# USER LOGIN PROCESS

# In this phase the user enters the smart card into the vehicle and enter the ID, Password and Random No.
# The Smart card computes the Ai* and match it with the stored Ai.

user_IDV = input('Enter the Vehicle ID : ')
user_PWi = getpass.getpass(prompt='Enter Password :')
user_rand_no = input('Enter Random No. : ')
time.sleep(2)
print('\n''Checking Details')
# if IDV == user_IDV & PWi == user_PWi & rand_no == user_rand_no:
if IDV == user_IDV:
    if PWi == user_PWi:
        if rand_no == user_rand_no:
            print('\n''User is Registered in the System')
            print('\n''Logging In')
            time.sleep(1)
            print('\n''You are now Logged in')

            # DATA AUTHENTICATION PROCESS

            # For each time a vehicular user Vi wants to connect to the TA through a nearby RSU Rx , it executes the following steps
            # to obtain a session key.

            # Vi retrives the K and Y from the smart card a generates the random integer Alpha (a) and computes attributes with time T.

            # Di = ga mod p

            print('\n''Vehicle retriving PUBLIC KEY and K from smart card')
            time.sleep(1)
            hash_IDVs = int(IDV) ^ s
            hash_k = hash(hash_IDVs)
            rand_int = randint(0, 100)  # alpha a
            TR = 1  # current time which we consider 1 for the project
            TT = 1
            Di_modless = g ** rand_int
            Di = Di_modless % p
            print('Vehicle Calculating Attributes')
            time.sleep(1)
            print('\n'f'Di = {Di}')
            # Ei = ya mod p
            Ei_modless = int(y) ** rand_int
            Ei = Ei_modless % p
            print('\n'f'Ei = {Ei}')
            # AIDi = IDVi XOR Hash(Ei)
            hash_Ei = hash(Ei)
            AIDi = int(IDV) ^ int(hash_Ei)
            print('\n'f'AIDi = {AIDi}')
            # DIDV = hash(k||Ei)
            k_ll_Ei = str(hash_k) + str(Ei)
            hash_DIDV = hash(k_ll_Ei)
            print('\n'f'DIDV = {hash_DIDV}')

            # CVi = hash(AIDi || DIDV || Ei || T)
            concat_CVi = str(AIDi) + str(hash_DIDV) + str(Ei) #+ str(T)
            hash_concat_CVi = hash(concat_CVi)
            print('\n'f'CVi = {hash_concat_CVi}')
            time.sleep(1)
            # Subsequently V also send the above detail to the RSU.
            # RSU = Rx
            # When Rx receives the login message from a vehicle,
            # it drops the message if T in the login message
            # expires. Otherwise, it appends its ID IDRx to the
            # message and relays it to the TA.

            if TR <= 1:
                print('\n''Login Details Received at Rx')
                print('\n''Message Forwarded to TA with the RxID')
                time.sleep(1)
                if TT <= 1:
                    # Now TA validate the login Message
                    # TA validate following things Ei-star, K-star, CVi-star
                    # print(Di)
                    # print(x)
                    # Ei-star = DiX mod p

                    # hash(K_star || E_tar)

                    print('\n''Message Reached at Trust Authority')
                    print('\n''Trust Authority Calculating Attributes')
                    time.sleep(1)
                    Ei_stars = (Di) ** x
                    Ei_star = Ei_stars % p
                    print('\n'f'Ei* = {Ei_star}')
                    # K-star = hash(AIDi XOR hash(Ei-star) XOR s)
                    hash_Ei_star = hash(Ei_star)
                    print('\n'f'H0(Ei*) = {hash_Ei_star}')
                    K_star = hash(AIDi ^ hash_Ei_star ^ s)
                    print('\n'f'K* = {K_star}')

                    # CVi-Star = hash(AIDi || DIDV ||Ei_star || T)
                    CVi_star = hash(str(AIDi) + str(hash_DIDV) + str(Ei_star))  # + str(T))
                    print('\n'f'CVi* = {CVi_star}')
                    print('\n'f'CVi = {hash_concat_CVi}')
                    print('\n'f'CVi* = {CVi_star}')
                    if hash_concat_CVi == CVi_star:
                        time.sleep(1)
                        print('\n''AUTHENTICATION SUCCESSFULL AT TRUST AUTHORITY')
                        print('\n''TRUST AUTHORITY COMPUTING Gi, Ks & Ci')
                        time.sleep(1)
                        # TA subsequently generates a random number B = Beta
                        rand_beta = randint(100, 200)
                        # it uses them to computer following
                        # Gi, Ks, Ci

                        # Gi = gB mod p
                        gbeta = g ** rand_beta
                        Gi = gbeta % p
                        print('\n'f'Gi = {Gi}')
                        # Ks = hash1(DiB mod p) it is session key

                        Di_beta = Di ** rand_beta
                        Ks = hash(Di_beta % p)
                        print('\n'f'Ks = {Ks}')

                        # Ci = hash1(DiB mod p || Ei_star || K_star)
                        Di_beta_mod_p = Di_beta % p
                        Ci = hash(str(Di_beta_mod_p) + str(Ei_star) + str(K_star))
                        print('\n'f'Ci = {Ci}')
                        # It sends fAIDi;Ci;Gig to Rx and the RSUs near Rx
                        # through a secure channel. Rx and these RSUs broadcast
                        # the same message on air. The messages are also
                        # sent to the nearby RSU to prevent Vi moving away
                        # from Rx .

                        # STEP 4 of Data Authentication.

                        # Ci_stars =hash1(Gia mod p || Ei || K)
                        print('\n''Vi computing attributes when the broadcasting message begins with AIDi')
                        Gi_alpha = Gi ** rand_int  # Gi and Alpha
                        Gi_mod_p = Gi_alpha % p
                        Ci_star = hash(str(Gi_mod_p) + str(Ei) + str(hash_k))
                        print('\n'f'Ci* = {Ci_star}')
                        # KS_stars = hash1(Gia mod p)
                        KS_star = hash(Gi_mod_p)
                        print('\n'f'K* = {KS_star}')
                        # It accepts the protocol if Ci_star = Ci using KS as the session key.

                        if Ci == Ci_star:
                            time.sleep(1)
                            print('\n''PROTOCOL ACCEPTED')
                            time.sleep(1)
                            print('Successfully Created Secure Connection between Vi and TA')
                        else:
                            print('AUTHENTICATION FAILED AT TRUST AUTHORITY')
                else:
                    print('Message dropped due to time delay at Trust Authority')

            else:
                print('Message dropped due to time delay at Reciver end on RSU')

        else:
            print('\n''User details incorrect or not reigstered in the system.')
            # time.sleep(1)

# print('Done')
