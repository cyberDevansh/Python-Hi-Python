class Team:
    def __len__(self):
        return 5

t=Team()
print(len(t)) #Python calls Team.__len__(t) and uses the returned integer (5)