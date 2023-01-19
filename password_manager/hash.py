from passlib.hash import cisco_type7


# ATTENTION: cisco_type7 implements the “Type 7”
# password encoding used Cisco IOS.
# This is not actually a true hash,
# but a reversible XOR Cipher encoding the plaintext password.
# "Type 7" strings are (and were designed to be) plaintext equivalent;
# the goal was to protect from "over the shoulder"
# eavesdropping, and little else.


def get_hash(password):
    return cisco_type7.hash(password)


def get_password(hash_password):
    return cisco_type7.decode(hash_password)
