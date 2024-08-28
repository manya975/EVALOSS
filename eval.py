def add(d,i):
        newd = {}
        t = input("Enter title = ")
        a = input("Enter author = ")
        isbn = (int)(input("Enter isbn = "))
        g = input("Enter genre = ")
        ava = (bool)(input("Enter availability True/False = "))
        newd['title'] = t
        newd['author'] = a
        newd['isbn'] = isbn
        newd['genre'] = g
        newd['avail'] = ava
        key = i
        d[i]=newd
        for key,value in d.items():
                print(f"{key} : {value}")
        return i + 1
def update(d):
        i = (int)(input("Enter isbn you want to upadate = "))
        for key,value in d.items():
               for k,v in value.items():
                       if v == i:
                               
                        choice = input("Enter what detail you want to update? Your choices are title,author,isbn,genre,avail= ")
                        if choice == 'isbn':
                                data = (int)(input("Enter data to be updated = "))
                        elif choice == 'avail':
                                data = (bool)(input("Enter data to be updated = "))
                        else:
                                data = input("Enter data to be updated = ")
                        value[choice] = data
        for key,value in d.items():
                print(f"{key} : {value}")
def search(d):
        data = (int)(input("Enter isbn to search = "))
        for key,value in d.items():
                for k,v in value.items():
                        if v == data:                             
                                for i,j in value.items():
                                        print(f"{i}:{j}")
def generate(d):
        for k,v in d.items():
               for key,value in v.items():
                        if v['avail'] == True:
                                print(f"{k}:{v}")
                                
i = 1
d = {}
f = (int)(input("Enter number of opeartion to perform = "))
#d = {i : {'title' : 'Three Men in A Boat','Author' : 'Robert Brown','isbn' : 123,'genre' : 'Suspense','avail' : True}}
for key,value in d.items():
                print(f"{key} : {value}")
while(f != 0):
        ch = (int)(input("Enter choice = "))
        if ch == 1:
                i = add(d,i)
        elif ch == 2:
                update(d)
        elif ch == 3:
                search(d)
        elif ch == 4:
                generate(d)
        else:
                print("Wrong choice")
                exit()
        f -= 1
