line1 = "004b"
line2 = "004b0049000000365468697320746561206973206e6f7468696e67206d6f7265207468616e20686f74206c656166206a756963652161004b00490000005053686172696e6720746561207769746820612066617363696e6174696e6720737472616e676572206973206f6e65206f66206c696665277320747275652064656c69676874732e43" #"004b0049000000275468657265206973206e6f2077617220696e2042612053696e672053652e07"

dest_address = ""
source_address = ""
total_frame_length = ""
payload = ""
checksum = ""
rest = ""

def split_frames(line2):
    frame_length = ""
    current_start_point = 0
    current_frame = ""

    for x in range(8, 16):
        frame_length += line2[x]
    frame_length_dec = int(frame_length, 16)
    print(frame_length_dec)

    for x in range(current_start_point, frame_length_dec):
        current_frame += line2[x]
    #ALP(current_frame)
    current_start_point = frame_length_dec
    for x in range(frame_length_dec + 8, frame_length_dec + 16):
        frame_length += line2[x]
    frame_length_dec = int(frame_length, 16)


def ALP(line2):
    x = ""
    total = 0
    checksum = ""
    #extract checksum from the frame
    for z in range(len(line2)-2, len(line2)):
        checksum += line2[z]

    for z in range(0, len(line2)- 2):
        x += line2[z]
        #if there are two bits in x:
        if z % 2 == 1:
            #add the integer version of the hex to total
            total += int(x, 16)
            #reset x
            print(x)
            x = ""
    print(total)
    calculated_checksum = hex(total % 128)
    print(calculated_checksum)

    if dest_address != line1:
        print("ADDRESS MISMATCH")

    if calculated_checksum != checksum:
        print("ERROR")


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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

amount_of_frames = len(rest)-2 / 60

ALP(line2)


