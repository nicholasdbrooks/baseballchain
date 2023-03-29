from pybaseball.lahman import *


def custom_namechain(players, numplayers, name):
    pass


def max_namechain(players, numplayers):
    longest_chain = []
    current_chain = []
    names_used = []

    for i in range(numplayers):
        # clear the used names
        names_used.clear()

        if len(current_chain) == 0:
            current_chain.append(players[i])
            names_used.append(players[i])

        # initialize pointer, bool
        j = 0
        onward = True
        while onward:
            current_name = players[j]
            # the name we are attempting to match
            key_name = current_chain[-1][1]

            # see if the first name of the current player matches the key name
            if current_name[0] == key_name and current_name not in names_used and current_name not in current_chain:
                current_chain.append(current_name)
                names_used.append(current_name)
                j = -1
            elif j == numplayers - 1:
                if len(current_chain) > len(longest_chain):
                    longest_chain.clear()
                    longest_chain = current_chain.copy()
                    print(longest_chain)
                current_chain.pop()
                if len(current_chain) == 0:
                    onward = False
                else:
                    j = -1
            j += 1

    print(longest_chain)






def getuserinput() -> str:
    # prompt the user for a player to begin the chain with
    player = input("Enter the full name of a player to start your chain: ")
    return player


def main():
    # initialize list of players, number of players
    numplayers = 0
    players = []

    # read the total number of players
    f = open("numplayers.txt", "r")
    numplayers = int(f.readline())
    f.close()

    # read the players, split the names, and add to the list
    f = open("players.txt", "r")
    for i in range(numplayers):
        name = f.readline()
        name = name[:-1]
        if len(name.split()) == 2:
            players.append(name.split())
        else:
            numplayers -= 1

    # get the user to select a player
    max_namechain(players, numplayers)


if __name__ == "__main__":
    main()
