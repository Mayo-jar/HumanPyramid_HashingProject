class HashMap:
    """
    This class implements a HashMap data structure using a list (array) as the internal data structure.
    Members:
        n_entries (int): The number of entries in the HashMap.
        k_buckets (int): The number of buckets in the HashMap.
        buck_index (int): The index of the current bucket.
        lyst (list): The internal list (array) used in the HashMap. This is the bucket.
    """

    def __init__(self, buckets: int = 7) -> None:
        """
        Initialize a new HashMap with a specified number of buckets
        Args:
            buckets (int, optional): The initial number of buckets. Defaults to 7.
        """
        self.n_entries = 0
        self.k_buckets = buckets
        self.lyst = [None] * buckets

    def hash(self, key: tuple) -> int:
        """
        Generate a hash value for a given key.

        Args:
            key (tuple): The key to hash.

        Returns:
            int: The hash value of the key.
        """
        return hash(key) % self.k_buckets
    
    def get(self, key: tuple) -> float:
        """
        Retrieve the value associated with a given key in the HashMap.

        Args:
            key (tuple): The key for which to find the value.

        Returns:
            float: The value associated with the key.

        Raises:
            KeyError: If the key is not found in the HashMap.
        """
        
        index = self.hash(key)
        trueIndex = index
        while self.lyst[index] is not None:
            if self.lyst[index][0] == key:
                return self.lyst[index][1]
            index = (index + 1) % self.k_buckets
            if index == trueIndex: raise KeyError
        raise KeyError
        
    def set(self, key: tuple, value: float):
        """
        Add or update a key-value pair in the HashMap.

        Args:
            key (tuple): The key of the element to be added or updated.
            value (float): The value to be associated with the key.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        
        i = self.hash(key)
        i_true = i

        while self.lyst[i] is not None:
            if self.lyst[i][0] == key: break
            i = (i + 1) % self.k_buckets
            if i == i_true: raise IndexError

        self.lyst[i] = (key, value)
        self.n_entries += 1
        if self.n_entries / self.k_buckets > 0.8: self.resize()
        return value     
        
    def resize(self) -> int:
        """
        Resize the HashMap based on the load factor.

        Returns:
            int: The new capacity of the HashMap after resizing.
        """
        self.k_buckets = (self.k_buckets*2)-1
        temp = self.lyst
        self.clear()
        for item in temp:
            if item is not None: self.set(item[0],item[1])

        return self.k_buckets

    def remove(self, key: tuple) -> None:
        """
        Remove a key and its associated value from the HashMap.

        Args:
            key (tuple): The key of the element to be removed.
        """
        index = self.hash(key)
        while index < self.k_buckets:
            if self.lyst[index][0] == key:
                self.lyst[index] = None
                return
            index += 1
    
    def clear(self) -> None:
        """
        Empty the HashMap, removing all entries.
        """
        self.lyst = [None] * self.k_buckets
        self.n_entries = 0


    def capacity(self) -> int:
        """
        Get the current capacity (number of buckets) of the HashMap.

        Returns:
            int: The number of buckets in the HashMap.
        """
        return self.k_buckets
    
    def size(self) -> int:
        """
        Get the number of key-value pairs in the HashMap.

        Returns:
            int: The number of entries in the HashMap.
        """
        return self.n_entries

    def keys(self) -> list:
        """
        Get a list of keys present in the HashMap.

        Returns:
            list: A list of keys in the HashMap.
        """
        temp = []
        for item in self.lyst:
            if item is not None: temp.append(item[0])
        return temp
    
    def the_lyst(self) -> None:
        """
        Print the internal list (array) used in the HashMap.
        """
        print(str(self.lyst))
        
    def __str__(self) -> str:
        """
        Get a string representation of the HashMap.

        Returns:
            str: A string representation of the HashMap.
        """
        return str(self.lyst)