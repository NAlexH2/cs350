#Make a LLL from a list


class node():
    def __init__(self, head, next):
        self.head = head
        self.next = next
    
    def dostuff(self):
        l = [1,2,3]
            
        ll = node(l[0], None)
        current = ll
        for i in range(1, len(l)):
            current = node(l[i], current)
        
        
        while ll:
            print(ll.head)
            ll = ll.next

if __name__ == "__main__":
    mything = node(None, None)
    mything.dostuff()

###THIS IS A WIP

#Next ----
