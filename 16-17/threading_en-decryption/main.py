import threading

# Q: Why did the python programmer have crooked teeth?
# A: No braces.


class EasyEncryption(threading.Thread):
    """
    Klasse zum verschluesseln eines Strings

    :ivar string substr: Nachricht welche verschluesselt werden soll
    :ivar int offset: Key (Offset) mit welchem der Substring verschluesselt werden soll
    :param string substr: Nachricht welche verschluesselt werden soll
    :param int offset: Key (Offset) mit welchem der Substring verschluesselt werden soll
    """

    def __init__(self, substr, offset):
        """
        Initialisiert die Superklasse und speichert die Parameter in die Instanzvariablen

        :param substr: Nachricht welche verschluesselt werden soll
        :param offset: Key (Offset) mit welchem der Substring verschluesselt werden soll
        """
        threading.Thread.__init__(self)
        self.substr = substr
        self.offset = offset

    def run(self):
        """
        Verschluesselt den Substring und gibt ihn aus.

        :return: Verschluesselter Substring
        """
        out = ""
        for c in self.substr:
            if c != " ":
                out += (chr(ord(c) + self.offset))
            else:
                out += " "
        return out

class EasyDecryption(threading.Thread):
    """
    Klasse zum entschluesseln eines Strings

    :ivar string substr: Nachricht welche entschluesselt werden soll
    :ivar int offset: Key (Offset) mit welchem der Substring entschluesselt werden soll
    :param string substr: Nachricht welche entschluesselt werden soll
    :param int offset: Key (Offset) mit welchem der Substring entschluesselt werden soll
    """

    def __init__(self, substr, offset):
        """
        Initialisiert die Superklasse und speichert die Parameter in die Instanzvariablen.

        :param substr: Nachricht welche entschluesselt werden soll
        :param offset: Key (Offset) mit welchem der Substring entschluesselt werden soll
        """
        threading.Thread.__init__(self)
        self.substr = substr
        self.offset = offset

    def run(self):
        """
        Entschluesselt den Substring und gibt ihn aus.

        :return: Entschluesselter Substring
        """
        out = ""
        for c in self.substr:
            if c != " ":
                out += (chr(ord(c) - self.offset))
            else:
                out += " "
        return out


# mode selection: encrypt (1), decrypt (2)
mode = input("Do you want to encrypt (1 or 'encrypt') or decrypt (2 or 'decrypt')?")
mode = mode.lower()
intMode = 0
while True:
    if mode == "encrypt" or mode == "1":
        intMode = 1
        break
    elif mode == "decrypt" or mode == "2":
        intMode = 2
        break
    else:
        print("Unknown input, try again!")
    mode = input("")

# message to encrypt
if intMode == 1:
    msg = input("Which message do you want to encrypt?")
elif intMode == 2:
    msg = input("Which message do you want to decrypt?")

while True:
    if len(msg) == 0:
        print("Nothing to encrypt, try again!")
    else:
        msg = msg.upper()
        break
    msg = input("")

# offset/key for en/decryption
offset = input("What's the offset?")
while True:
    try:
        offset = int(offset)
    except ValueError:
        print("The offset is not an integer")
    else:
        break
    num = input("")

# message is later split into n equal length substrings
if intMode == 1:
    num = input("How many threads should encrypt the message?")
elif intMode == 2:
    num = input("How many threads should decrypt the message?")

while True:
    try:
        num = int(num)
    except ValueError:
        print("The thread number is not an integer")
    else:
        # checking length conditions
        if num > len(msg):
            print("The number of threads can't be greater than the length of your message, try again!")
        elif num <= 0:
            print("The number of threads can't be negative or zero, try again!")
        else:
            break
    num = input("")



# maximum length a substring can be
msg_chunk_size = int(len(msg) / num) + 1
# list with split string parts (substrings)
msg_chunk_list = []

# splitting the string by using indices
for i in range(0, len(msg), msg_chunk_size):
    msg_chunk_list.append(msg[i: i + msg_chunk_size])

# aufgrund der tatsache, dass die liste in manchen faellen nicht die gewuenschte laenge hat,
# entspricht die anzahl der threads  der laenge der liste.
threads = []
for i in range(0, len(msg_chunk_list)):
    if intMode == 1:
        thread = EasyEncryption(msg_chunk_list[i], offset)
    elif intMode == 2:
        thread = EasyDecryption(msg_chunk_list[i], offset)
    #liste mit allen threads
    threads += [thread]
    #threads starten
    thread.start()

out_msg = ""
for i in threads:
    out_msg += i.run()

for i in threads:
    i.join()

print(out_msg)
