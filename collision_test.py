import random

def how_many_before_collision(buckets, loops=1):
    for i in range(loops):
        tries=0

        # SET -> Hash table with only keys and no values
        tried=set()
        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            if hash_index not in tried:
                tried.add(hash_index)
                tries+=1
            else:
                break
        
        print(f"{buckets} buckets, {tries} hashes before collision. ({tries/buckets}%)")


how_many_before_collision(32, 10)
how_many_before_collision(1024, 10)
how_many_before_collision(2048, 10)
how_many_before_collision(4096, 10)
