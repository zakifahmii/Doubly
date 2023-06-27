import sys as program

def garis():
    print("--------------------------------------------------")

def main():
    print("==================================================")
    print("            Program Double Linked List")
    print("==================================================")
    # Membuat class untuk node dalam Doubly Linked List
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    # Membuat class untuk Doubly Linked List
    class DoublyLinkedList:
        def __init__(self):
            self.head = None
        # Menambah data pada awal linked list

        def push_front(self, data):
            node = Node(data)
            node.next = self.head
            if self.head is not None:
                self.head.prev = node
            self.head = node

        # Menambah data pada akhir linked list
        def push_back(self, data):
            node = Node(data)
            if self.head is None:
                self.head = node
                return
            last = self.head
            while last.next:
                last = last.next
            last.next = node
            node.prev = last

        # Menampilkan isi linked list
        def print_list(self):
            node = self.head
            while node:
                print(node.data, end=" ")
                node = node.next

        # Menghapus node dengan data tertentu
        def delete(self, data):
            node = self.head
            # Jika data yang dihapus adalah head
            if node is not None:
                if node.data == data:
                    self.head = node.next
                    self.head.prev = None
                    node = None
                    return
            # Mencari node dengan data
            while node is not None:
                if node.data == data:
                    break
                node = node.next
            # Jika data tidak ditemukan
            if node is None:
                return
            # Menghapus node
            node.prev.next = node.next
            node.next.prev = node.prev
            node = None

    dll = DoublyLinkedList()
    x = int(input("Input Banyak Elemen: "))
    for i in range(x):
        data = int(input("Masukkan Data ke %d: " % (i+1)))
        dll.push_back(data)

    print("Doubly Linked List: ")
    dll.print_list()

    hapus = int(input("\nMasukkan Angka yang Ingin di Hapus: "))
    dll.delete(hapus)

    garis()
    print("Doubly Linked List setelah menghapus node data %d: " % (hapus))

    dll.print_list()

while True:
    main()
    ulang = input("\nIngin Menginput Lagi?(y/n): ")
    if ulang == "y" or ulang == "Y":
        print("\n")
        continue
    elif ulang == "n" or ulang == "N":
        print("Good Bye!")
        program.exit()
    else:
        print("Ada Kesalahan!")
        program.exit()