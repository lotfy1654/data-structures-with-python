import ctypes


class OurArray:
    def resize(self, source_array: ctypes.POINTER(ctypes.c_int), new_size: int):
        if new_size <= 0 or (source_array is None) or (new_size == len(source_array.contents)):
            return

        # ctypes.c_int -> mean integer type in c language

        # Make a new array of the new size
        new_array = (ctypes.c_int * new_size)()

        # Copy elements from the old array to the new array
        # memmove(destination, source, size) # Copies size bytes from source to destination
        ctypes.memmove(new_array, source_array, ctypes.sizeof(
            ctypes.c_int) * len(source_array.contents))

        # Update the source_array to point to the new array
        return new_array

    def getat(self, source_array: ctypes.POINTER(ctypes.c_int), index: int):
        if (source_array is None) or (index < 0) or (index >= len(source_array.contents)):
            return None

        # .cast ( source, type) # Casts source to the specified type and returns it
        element_ptr = ctypes.cast(source_array, ctypes.POINTER(ctypes.c_int))
        return element_ptr[index]


# if __name__ == "__main__" this is used to run the code only if the file is executed directly, not when imported as a module
if __name__ == "__main__":
    # Example usage
    # Example array of size 5 containing integers 1 to 5
    arr = (ctypes.c_int * 5)(1, 2, 3, 4, 5)
    # Create a pointer to the array
    arr_ptr = ctypes.pointer(arr)

    our_array = OurArray()

    new_arr = our_array.resize(arr_ptr, 10)

    print("Resize", list(new_arr))

    print("GetAt index 2 =>", our_array.getat(arr_ptr, 2))
