import re
import argparse
import hashlib

parser = argparse.ArgumentParser(prog="Unshadower")
parser.add_argument('-w', '--wordlist', help = "Word list to use", required = True)
parser.add_argument('-s', '--shadowfile', help = "Shadow file to use", required= True) 
namespace = parser.parse_args()
args= vars(namespace)
regex = re.compile(r'\:\$\d\$')
users = []

def main():
    #get the users with a shadowed password
    with open(args['shadowfile']) as file:
        for line in file:
            if regex.search(line):
                users.append(line)
    profiles = []
    for user in users:
        profiles.append(profile(user))

    print(profiles)
        

class profile():
    def __init__(self, ul):
        fields = ul.split('$')
        self.name = fields[0] 
        self.algo = fields[1]
        self.salt = fields[2]
        self.uhash = (fields[3].split(':'))[0]

    def crack(self):
        if(self.algo == '1'):
            m = hashlib.md5
        elif self.algo == '2a' | '2y':
            ##
            pass            
        elif self.algo == '5'
            m=hashlib.sha256
        elif self.algo == '6'
            m=hashlib.sha512
        else:
            print("Hash not recognised")
            return

        ##Hash all of the words in the wordlist and compare
        with read(args['wordlist']) as wl:
            for w in wl:
            x = hashlib.sha256()
            x.update(w)
            x.update(self.salt)    
            h = x.hexdigest()
            if (h == self.uhash)
                result = name + ':' + w +'\n' + "Password Found!"
                break
            result = "Password Not Found" 

if __name__ == "__main__":
    main()
