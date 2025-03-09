class cnichashtable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  

    def hashfunction(self, cnic):
        cnic_digits = cnic[6:] 
        
        total = 0
        for digit in cnic_digits:
            if digit.isdigit():
                total += int(digit)

        return total % self.size

    def insert(self, cnic, data):
        index = self.hashfunction(cnic)

        
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == cnic:
                self.table[index][i] = (cnic, data)
                return

        
        self.table[index].append((cnic, data))

    def search(self, cnic):
        index = self.hashfunction(cnic)

        
        for stored_cnic, stored_data in self.table[index]:
            if stored_cnic == cnic:
                return stored_data

        return None  

    def delete(self, cnic):
        index = self.hashfunction(cnic)

       
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == cnic:
                del self.table[index][i]
                print("Cnic deleted.")
                return

        print("Cnic not found.")

    def printtable(self):
        for i in range(self.size):
            print("Index", i, ":", self.table[i])


if __name__ == "__main__":
    cnic_table = cnichashtable(size=10)

    cnic_table.insert("35202-6789123-1", "rehan")
    cnic_table.insert("35202-6789123-2", "ali")
    cnic_table.insert("35202-1111111-5", "ahmad")
    cnic_table.insert("35202-9999999-9", "arslam")

    print("\nTable after inserts:")
    cnic_table.printtable()

    result = cnic_table.search("35202-6789123-1")
    print("\nSearch for 35202-6789123-1:", result)

    cnic_table.delete("35202-1111111-5")

    print("\nTable after deletion:")
    cnic_table.printtable()

    result = cnic_table.search("35202-1111111-5")
    print("\nSearch for 35202-1111111-5 after deletion:", result)
