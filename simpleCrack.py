import re
import argparse
import crypt

parser = argparse.ArgumentParser(prog="Unshadower")
parser.add_argument('-w', '--wordlist', help = "Word list to use", required = True)
parser.add_argument('-s', '--shadowfile', help = "Shadow file to use", required= True) 
namespace = parser.parse_args()
args= vars(namespace)
regex = re.compile(r'\:\$\d\$')
users = []

def main():
    #get the users with a shadowed password
    with open(args['shadowfile'],"r",encoding='utf-8') as file:
        for line in file:
            if regex.search(line):
                users.append(line)
    profiles = []
    for user in users:
        profiles.append(profile(user))

    for p in profiles:
        print(p)
        p.crack()
        
class profile():
    def __init__(self, ul):
        fields = ul.split('$')
        self.name = fields[0] 
        self.algo = fields[1]
        self.salt = fields[2]
        self.uhash = (ul.split(':'))[1].encode('utf-8')

    def __str__(self):
        string = self.name + ' ' + self.algo + ' ' + self.salt
        return string

    def crack(self):
        ##Hash all of the words in the wordlist and compare
        with open(args['wordlist'],"r",encoding='utf-8') as wl:
            for w in wl:     
                testHash = crypt.crypt(w.rstrip(),salt='$'+self.algo+'$'+self.salt)
                testHash=testHash.encode('utf-8')

                if testHash == self.uhash:
                    result = self.name + ':' + w +'\n' + "Password Found!"
                    break
                else:
                    result = "Password Not Found" 

        print (result)

if __name__ == "__main__":
    main()
