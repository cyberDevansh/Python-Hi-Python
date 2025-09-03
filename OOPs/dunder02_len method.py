class Team:
    def __len__(self):
        return 5

print(len(Team())) #Python calls Team.__len__() and uses the returned integer (5)
