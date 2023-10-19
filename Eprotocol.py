from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

# /////// Почнемо з генерації ключів.
# Для цього ми використаємо алгоритм RSA,
#  який дозволяє нам створювати пари приватного та публічного ключів.
#  У нашому випадку, публічний ключ буде використано для шифрування голосів,
#   а приватний - для їх розшифровки.

# ///////// Цей код генерує 3072-бітний ключ RSA.
# pubKeyPEM та privKeyPEM - це, відповідно, публічний та приватний ключі.

# Далі ми створимо систему голосування.
# Ми можемо створити простий клас VotingSystem,
# який буде зберігати інформацію про кандидатів та виборців,
# а також реалізовувати методи для голосування та обрахунку голосів.

# Наприклад:


class VotingSystem:
    def __init__(self, candidates, eligible_voters):
        self.candidates = candidates
        self.votes = {candidate: 0 for candidate in candidates}
        self.voters = []
        self.eligible_voters = eligible_voters

    def vote(self, voter, candidate):
        if voter not in self.eligible_voters:
            print('This voter is not eligible to vote.')
            return False
        if voter in self.voters:
            print('This voter has already voted.')
            return False
        if candidate not in self.candidates:
            print('Invalid candidate.')
            return False

        self.voters.append(voter)
        self.votes[candidate] += 1
        return True
    
result = VotingSystem(['Alice', 'Bob'], ['Alice', 'Bob', 'Charlie'])
result.vote('Alice', 'Alice')
result.vote('Alice', 'Bob')
result.vote('Alice', 'Charlie')
result.vote('Bob', 'Alice')
# Цей клас має два методи: vote(), який дозволяє виборцю голосувати за кандидата, та count_votes(), який повертає кількість голосів, які отримав кожен кандидат.

# Нарешті, ми можемо реалізовувати різні сценарії поведінки на випадок порушення протоколу, такі як:

# Виборець не проголосував.
# Виборець проголосував неправильно.
# Виборець не має права голосувати.
# Виборець хоче проголосувати повторно.
# Виборець хоче проголосувати замість іншого виборця.
# Ці сценарії можна реалізувати за допомогою додаткових умов
