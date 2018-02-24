line1 = "004b"
line2 = "004b0049000000275468657265206973206e6f2077617220696e2042612053696e672053652e07"

dest_address = ""
source_address = ""
total_frame_length = ""
payload = ""
checksum = ""
rest = ""

def ALP(rest):
    x = ""
    total = 0
    checksum = ""
    #extract checksum from the frame
    for z in range(len(rest)-2, len(rest)):
        checksum += rest[z]

    for z in range(0, len(rest)- 2):
        x += rest[z]
        #print(x)
        #if there are two bits in x:
        if z % 2 == 1:
            #add the integer version of the hex to total
            total += int(x, 16)
            #reset x
            x = ""
    calculated_checksum = hex(total % 128)
    print(calculated_checksum)

#select frame is not finished
def select_frame():
    for x in range(1, amount_of_frames + 1):
        current_payload = ""
        start_point = 16
        end_point = start_point + x * 62
        for y in range(start_point, end_point):
            current_payload += line2[y]


for x in range(0, 4):
    dest_address += line2[x]

for x in range(4, 8):
    source_address += line2[x]

for x in range(8, 16):
    total_frame_length += line2[x]

for x in range(16, len(line2)):
    rest += line2[x]

amount_of_frames = len(rest) / 62

ALP(rest)



#print(dest_address)
#print(source_address)
#print(total_frame_length)
#print(len(line2))
#print(rest)

