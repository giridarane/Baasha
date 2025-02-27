import string
import secrets
import subprocess

def generate_password(length=16):
    """Generate a secure password with letters, digits, and punctuation."""
    
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a secure password using secrets module
    password = ''.join(secrets.choice(characters) for i in range(length))
    
    return password

def display_banner():
    """Display the Baasha banner using a custom ASCII design."""
    banner = """
		    ==========+=-----+++=---::-==-----:-=++=++***=======++++--=++++**=------..::::::....:---------------
		    ==========+++=-==++=-=----==----------+**********++***++=----=---=-:::::::::---:::......:--:--------
		    =========+++++=++=---:--===-:::::-----=++*+*********++++++===---=-=-:::--::::::-::..::..:::::.:::---
		    ===========+++++*=--:--=------:------=-=+++****+**++++++++=-::-::::::::::::::-::::::.:..::::::::::--
		    =-------=====++*+--::---=--:::::::--=--=+******+=====-:-+##%#*+-....:.:::.:::--:::::.........::::.:- 
		    ---===========--:---::----:::..::--=+-++*****+===+**=*%@@@@@%@%%*-.....:.::::----::::......::...::::
		    ---==----==-:--:::.:.:::-::...:::-==*+*+****--=*####%@@@@@@%#+--#@*.....:....:::-::::::...::.:-:::: 
		    =-:======-::--+===::.::-:::::...:-=+*******+++-*#######%%%@@@%###--+*....::::...:::....:::::::::::::
		    ========:..:-:::::::-:..::::...:==+******==+################%%@%%*:-+..::.:::.........:::::-:::.:-: 
		    =+=======-:::::---:---------:...--=**#*##%%%%%%%%%@%########***%%%%+--....:.::::.........::-::::::::
		    =========----:::--:----:---::...-+**##%#%%%%%%@@@@@@@%@@%%%%%%%%%%@@%#*=..:-:::..........:::::-:-:-:
		    ===========-::.:::::--=--=:----::-**%%%%%%@%%@@@@@@%%#*#@@@@@@%%%@%%%@%*##-...............-*=:::---::
		    ===========---:--::::-+==--:-==-:-*%%%%%@%%%%@@@@@%%#**+%@@@@@@@%#+%%%#%*=#=............-#+::::::----
		    =========---=----::..---=-----::-#%%%@@@@%%%%##*#%@@%%%*#%@@@@%#**%%%####*#:..........*#:...::::::-:
		    ===+===-----==--=:...::::::------*%@@@@@%%######%%%%%%%*##**##*##*%%#%#####:........=#-....::....:-- 
		    ======:-:::====+=:::.:::.::::--=-+#%@%@%%%%%#%%%#########*#**++**#%%@######..==+++=*=...........:.:: 
		    +++==-=--:==+++-:.....--=::-=+--=+@@%%%%%%%%%%######***##***++***#@@%#%%%*..-##*#****+:.........:-. 
		    ++++=+===--====-:--:::--==:-==-==*@@@%%%%%%%%#########**#***+****##%@%%%%*..::=#==*****-........:.. 
		    ==++++++=====+=++-+=:.::===----==+@@@@%%%%%%%%%######*************#*%@%#%%+..*#*##*****+*-.....:::.. 
		    ==++++++++++++++++=---+=++=:--=+++@%@@%%%%%%%%%%%######**###*###***##@%%%%+.=*##**+#*#**++:::...:::- 
		    ==+++===++++++++***++**+=+===-+**+#@%#%%%%%%%%%%%%%%############**#*#%%%@#:.+*##+:...-##**=:...::.:: 
		    =========+++===++***#*#*==-====+****@@@%%%%%%%%%%%%%###%%%#######**###@@@@=..+#*#:.s...*%#***+:......:
		    =========+=+==++*****+**+*+=******+%@@@%%%%%%%%%%%%###%%%%%%%%###*#*%%@@%...#**#-::-=*******=....... 
		    =========++++++****+*##****##**#**#@@@@%@%%%%%%%%######%%%%%%%##*%%%%%%%....%########***++*=:......: 
		    ========++++++++*###############*#*#%@@%%%%%%%%%%%%#####%%%%%%%##%@@%%%%=::..%#######****+++---:::...
		    ======+++++++++**#***####**#******%%@@@%%%%%%%#########%####%###%%@@@%=.....*######*******:...:::::. 
		    ====+*#***###**################****%@%%++#%%%%###############**#%@@%#*..:...:%%###*******::.:::::::- 
		    ===**#**************#################%*+++=*#################*#@@@%%#:.......+%%##*****+-----::----- 
		    ===#*#****************################+=++===*###*+=========**%%%@%#-.........=%%#****+=---:-----:::
		    =+#**###*************##############*#*++===*#+*#:::::-:::--:==+%@%#=.......:...#%#*****+-----:------ 
		    *##**######**###***###############*+*++==#%%%%#+=::::::----++++#%%+:........:..-%##*****=---:::---:: 
		    ###**########%#####*#############*==*+=+%%###-===:::::::=++=+===*###**++=:......%%#****+=-----::---: 
		    %##*#########%##################*==-=+=#******+*#:::::::*++===---=####**+=====:.+%#******=---:.::::- 
		    ###*#########%##########*#**##**=====+#***##+***#::::-*#+========-+#*#**+++====#%%##**#*==-::::-:::- 
		    *##*########%##########*****##*-==-=++*#=+===++=+==-:**======-=====+***++++==+%+=--=+======::::--::-
		    %###########%################+===+*+#%#%*==-+#*=--:-++=++=======+++=***++++++**#++++=+++++=-::--====
		    ###########%#######*******++=+++++**==+++##***=:-=+**+==+++====++++++++++***=*##*++=++++++==:-:-====
		    ##########%#####*******+=++++===+**#+*++-+*##*-::+***====+++++++++*****+##*#**#%+**++++++++=--::--==
		    ##################***+++==++====***###*+******--+*++*=====+****++++++**####*+#*%*=--+++++++++=------
		    ###############*+==+++++======-=**=*###=+=-=-=*+**+++=====+****++++++**####*+#*%*=--+++++++++=------
		    %%#############**===+++++=====-++++++=+*#%##**#+****========++*****+++####**#%#*##***++***+++=------
		    %%%%%%%%%##%%%###*+=============+=**##++%%%%#*%#+***+==========++++***######*%@#*##*#******++++=::---
		    %%%%%%%%%#%%%%###*++===========--+%%%#+##%%#%%##+****+=--==========++#######%#*##**#********++++=:---
		    %%%%%%%%%##%%%###**++============%%#%%%#*%#*%%##*****++====-=====+***#######@%%%%#*#**********+++++::--
		    %%%%%%%%%%%%%%%###**+==========#%*%++*%%######*********++++=======####%%%%#%#*#%%%#*********+++++=::::
		    %%%%%%%%%%%%%%%%###*+=========*%+##*******+++++++********++++====*#%%%%%%%#@%%%%%%%%********++**++:.:
		    %#%%%%%%%%%%%%%###*+=======-*####*************++++*******++++====*#%%%%%#@@@%%%%%%%%#******+***++-.. 
		    ####%%%%%%%%%%%%###*======+####****************+++++******++*#**+=**#%%%%@@@%%%%%%%%#******+***+++:.
		    #####%%%%%%%#%%%###*+===+######******************++++*****#%%%#######%@@@@@@@%##%#%%##***********+-.
		    ######%%%%%%%%%%%###*+#########*******************+*++**#%%%%%%%%%##%%@@@@@@%%##%%*%%#***********++: 
		    """
    print(banner)

def main():
    display_banner()
    
    print("Baasha: Strong Password Generator\n")
    
    try:
        length = int(input("Enter password length (default 16): ") or 16)
        if length < 8:
            print("Password length should be at least 8 characters for security!")
            return
    except ValueError:
        print("Invalid input. Using default length of 16.")
        length = 16

    password = generate_password(length)
    print(f"\nGenerated Strong Password: {password}")

if __name__ == "__main__":
    main()
