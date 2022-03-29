from ctypes import pointer
from ReadWriteMemory import ReadWriteMemory
from pymem import process
from pymem.process import base_module


def main():
    base_address = 'socialclub.dll + 85E81F'
    static_address_offset = 0x7FF9240DE81F
    pointer_static_address = base_address + static_address_offset
    offsets = []
    
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_name('Grand Theft Auto')
    process.open()
    my_pointer = process.get_pointer(pointer_static_address, offsets=offsets)
    pointer_value = process.read(my_pointer)
    print(f'Value: {pointer_value}')
    value_to_set = int(input('Enter a value: '))
    process.write(my_pointer, value_to_set)

if __name__ == '__main__':
    main()