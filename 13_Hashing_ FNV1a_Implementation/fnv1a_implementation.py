# Implementation of FNV-1a Hashing Two types: 32-bit and 64-bit
class Hash:

    # FNV-1a 32-bit hash functions
    def hash32(self, data):
        # FNV-1a 32-bit parameters
        offset_prime = 2166136261
        fnv_prime = 16777619

        # Convert string to bytes
        data_bytes = data.encode('ascii')

        # Initialize hash value to offset basis
        hash_value = offset_prime

        # Perform FNV-1a hashing
        for i in range(len(data_bytes)):
            # XOR the byte into the least significant byte of the hash
            hash_value = hash_value ^ data_bytes[i]
            # force 32-bit
            # & 0xffffffff => use bitwise AND to limit to 32 bits every (f) is 4 bits so 8 f's equals 32 bits 4*8=32 bits
            hash_value = (hash_value * fnv_prime) & 0xffffffff  # force 32-bit

        print(data + " <- hashed 32 to -> " +
              str(hash_value) + " hex value: " + hex(hash_value))

        # Ensure 32-bit output
        return hash_value

    # FNV-1a 64-bit hash functions
    def hash64(self, data):
        # FNV-1a 64-bit parameters
        offset_prime = 14695981039346656037
        fnv_prime = 1099511628211

        # Convert string to bytes
        data_bytes = data.encode('ascii')

        # Initialize hash value to offset basis
        hash_value = offset_prime

        # Perform FNV-1a hashing
        for i in range(len(data_bytes)):
            # XOR the byte into the least significant byte of the hash
            hash_value = hash_value ^ data_bytes[i]
            # force 64-bit
            # & 0xffffffffffffffff => use bitwise AND to limit to 64 bits every (f) is 4 bits so 16 f's equals 64 bits 4*16=64 bits
            hash_value = (hash_value * fnv_prime) & 0xffffffffffffffff

        print(data + " <- hashed 64 to -> " +
              str(hash_value) + " hex value: " + hex(hash_value))

        # Ensure 64-bit output
        return hash_value


if __name__ == "__main__":
    hasher = Hash()
    hasher.hash32("hello world")
    hasher.hash64("hello world")
