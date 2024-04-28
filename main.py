from sha_functions import *


def write_hash_to_file(file: str, hash_file: str, sha_type: int) -> None:
    if sha_type not in (224, 256, 384, 512):
        raise Exception(f'No SHA algorithm with number: {sha_type}')

    with open(file, 'r') as f:
        file_string = f.read()

    if sha_type == 224:
        digest = sha3_224(file_string)
    if sha_type == 256:
        digest = sha3_256(file_string)
    if sha_type == 384:
        digest = sha3_384(file_string)
    if sha_type == 512:
        digest = sha3_512(file_string)

    with open(hash_file, 'w') as f:
        f.write(digest)


def check_hash(file: str, hash_file: str, sha_type: int) -> bool:
    if sha_type not in (224, 256, 384, 512):
        raise Exception(f'No SHA algorithm with number: {sha_type}')

    with open(file, 'r') as f:
        file_string = f.read()

    with open(hash_file, 'r') as f:
        hash_string = f.read()

    if sha_type == 224:
        return hash_string == sha3_224(file_string)
    if sha_type == 256:
        return hash_string == sha3_256(file_string)
    if sha_type == 384:
        return hash_string == sha3_384(file_string)
    if sha_type == 512:
        return hash_string == sha3_512(file_string)


write_hash_to_file('my_text.txt', 'my_text_hash.txt', 224)


# print(check_hash('my_text.txt', 'my_text_hash.txt', 224))
