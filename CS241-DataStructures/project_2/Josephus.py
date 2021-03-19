from Linked_List import Linked_List

def Josephus(ll):
    for i in range(len(ll)-1): #Every loop will kill second person.
        ll.rotate_left()
        ll.remove_element_at(0)
        print(ll)
    print("The survivor is: " + str(ll.get_element_at(0)))
    #Returns the last person.

if __name__ == '__main__':
    n = int(input("Input the total number of people: "))
    ll = Linked_List()
    for i in range(n):
        ll.append_element(i+1) #Add one so there is no '0' person.
    print("Initial order:", ll)
    Josephus(ll)
