input_file = "2021/16/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()

#data = """620080001611562C8802118E34""".splitlines()

def hex_to_bin(hexadecimal):
    binary_representation = []
    for char in hexadecimal:
        if char in "0123456789":
            bin_value = bin(int(char))[2:]
        else:
            d = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
            bin_value = bin(int(d[char]))[2:]
        bin_value = "0" * (4 - len(bin_value)) + bin_value
        binary_representation += [bin_value]
    return "".join(binary_representation)

def to_dec(bits):
    res = 0
    for i, bit in enumerate(reversed(bits)):
        res += int(bit) * 2**i
    return res

class Packet():
    def __init__(self, binary):
        self.binary = binary
        self.version =  self.binary[0:3]
        self.type_ID = self.binary[3:6]
        self.is_literal = self.type_ID == "100"  # else is_operation
        self.length_ID = None if self.is_literal else self.binary[6]
        self.length_info = None
        self.content_start = 6
        if self.length_ID is not None:
            self.length_info = self.binary[7:18] if self.length_ID == "1" else self.binary[7:22]
            self.content_start = 18 if self.length_ID == "1" else 22
        self.subpackets = []
        self.get_subpackets()
        self.end = self.get_end_of_packet()
        self.binary = self.binary[:self.end]

    def get_end_of_packet(self):
        if self.is_literal:
            start = 6
            while self.binary[start] != "0":
                start += 5
            return start + 5
        else:
            return 7 + sum([s.end for s in self.subpackets]) + len(self.length_info)

    def get_subpackets(self):
        if self.is_literal:
            return
        elif self.length_ID == "1":
            n_subpackets = to_dec(self.length_info)
            pointer = 18
            while n_subpackets and len(self.binary[pointer:]) > 6:
                next_subpacket = Packet(self.binary[pointer:])
                self.subpackets += [next_subpacket]
                pointer += next_subpacket.end
                n_subpackets -= 1

        elif self.length_ID == "0":
            length_subpackets = to_dec(self.length_info) 
            pointer = 22
            end = 22 + length_subpackets
            while len(self.binary[pointer:]) > 6 and pointer < end:
                next_subpacket = Packet(self.binary[pointer:])
                self.subpackets += [next_subpacket]
                pointer += next_subpacket.end


    def get_value(self):
        if self.is_literal:
            number = ""
            for i in range(self.content_start, self.end, 5):
                number += self.binary[i + 1:i + 5]
            return to_dec(number)
        elif self.type_ID == "000":
            return sum([s.get_value() for s in self.subpackets])
        elif self.type_ID == "001":
            values = [s.get_value() for s in self.subpackets]
            res = 1
            for v in values:
                res *= v
            return res
        elif self.type_ID == "010":
            return min([s.get_value() for s in self.subpackets])
        elif self.type_ID == "011":
            return max([s.get_value() for s in self.subpackets])
        elif self.type_ID == "101":
            return 1 if self.subpackets[0].get_value() > self.subpackets[1].get_value() else 0
        elif self.type_ID == "110":
            return 1 if self.subpackets[0].get_value() < self.subpackets[1].get_value() else 0
        elif self.type_ID == "111":
            return 1 if self.subpackets[0].get_value() == self.subpackets[1].get_value() else 0

    def version_sum(self):
        stack = [self]
        visited = []
        running_sum = 0
        while stack:
            current = stack.pop()
            visited += [current]
            #print(current)
            running_sum += to_dec(current.version)
            for sub in current.subpackets:
                if sub not in visited:
                    stack.append(sub)
        return running_sum

    def __repr__(self):
        return self.binary

    def __str__(self):
        full = self.binary + "\n"
        version = f"Version: {self.version} ({to_dec(self.version)})\n"
        tid = f"Type_ID: {self.type_ID} ({to_dec(self.type_ID)})\n"
        lid = f"Length_ID: {self.length_ID} ({to_dec(self.length_ID if self.length_ID is not None else '0')})\n"
        linfo = f"Length_info: {self.length_info} ({to_dec(self.length_info if self.length_info is not None else '0')})\n"
        contents = f"Contents: {self.binary[self.content_start:]}\n"
        total_length = f"Total lenght: {self.end}\n"
        sons = f"Sons: {self.subpackets}\n\n"
        return full + version + tid + lid + linfo + contents + total_length + sons
    

packet = Packet(hex_to_bin(data[0]))

print(packet.version_sum())

# Part Two

packet = Packet(hex_to_bin(data[0]))

print(packet.get_value())