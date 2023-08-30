import SingleDES
import TripleDES
import RSA_
import time

while True:
    choice = input("\nChoose an encryption method:\n 1 - Single DES\n 2 - Triple DES\n 3 - RSA\n\n Choice: ")

    if choice == '1':
        print("\nYou have selected \"Single DES\"\n")
        SingleDES.DES_main()
    elif choice == '2':
        print("\nYou have selected \"Triple DES\"\n")
        TripleDES.DES3_main()
    elif choice == '3':
        print("\nYou have selected \"RSA\"\n")
        RSA_.RSA_main()
    else: print("Invalid input\n")
    
    choice = input("Would you like to continue? (Y/N)\n")
    
    if choice in ['Y', 'Yes', 'y', 'yes']:
        continue
    elif choice in ['N', 'No', 'n', 'no']:
        print("\nThank you, exiting program")
        time.sleep(3)
        break
    else: 
        print("Invalid input, exiting the program\n")
        time.sleep(3)
        break