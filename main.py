import subprocess
import os

hash_algorithms = {

    "MD5": 0,
    "SHA1": 100,
    "SHA256": 1400,
    "SHA384": 10800,
    "SHA512": 1700,
    "NTLM": 1000

}

algo = hash_algorithms.get(input("Please enter hashing algorithm: "))

while algo == None:

    algo = hash_algorithms.get(input("Please enter a valid hashing algorithm (MD5, SHA1, SHA256, SHA384, SHA512, NTLM): "))

digest = input("Please enter digest in hex: ")

complexity = None

while complexity == None:

    try:

        complexity = int(input("Enter complexity (0 means no rulesets will be applied, 1 means all rulesets will be applied, and higher values will mean repition of rulesets): "))

    except ValueError:

        print("Complexity should be a base-10 integer")

rules = os.listdir("rules")
rules = ["rules/" + rule for rule in rules]

flagged_rules = []

for rule in rules:

    flagged_rules.append("-r")
    flagged_rules.append(rule)

quiet = int(input("Suppress hashcat output? (Y/n): ").lower() != "n")

p = subprocess.Popen(["hashcat", "-a", "0", "-m", str(algo), digest, "--potfile-disable", "-o", "passwords.txt", "wordlist.txt"] + flagged_rules*complexity + ["--quiet"]*quiet)

p.communicate()

print()

try:

    with open("passwords.txt", "r") as f:

        passwords = f.readlines()

        passwords = [password.split(":")[1] for password in passwords]

        if len(passwords) == 0:

            print("Sorry, we couldn't break the password. Try increasing the complexity value.")

        elif len(passwords) == 1:

            print(f"Congrats! You have broken the password. It is: {passwords[0]}")

        else:

            print("Congrats! Not only did you break the password, you also found a hash collision. Here are your passwords: ")
            print(passwords)

except FileNotFoundError:

    print("Sorry, we couldn't break you password. Try increasing the complexity value.")

if os.path.exists("passwords.txt"):

    os.remove("passwords.txt")