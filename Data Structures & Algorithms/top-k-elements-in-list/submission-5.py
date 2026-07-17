class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Key: The actual number
        # Value: the frequency the number shows up
        freq_dict = {}

        # Populate freq_dict
        for n in nums:
            freq_dict[n] = freq_dict.get(n,0) + 1

        # List of list, where index of outer list is the frequency, and the value is a list of numbers with that frequence
        freq_bucket_list = [[] for _ in range(len(nums)+1)]

        # Populate freq_bucket_list
        for n, freq in freq_dict.items():
            freq_bucket_list[freq].append(n)
        
        print(freq_bucket_list)

        output_list = []
        # Take the k last numbers out from the freq_list
        for i in range(len(nums), -1, -1):

            # Go through each index's list and populate it with these numbers 
            # until the output_list is k items long
            for n in freq_bucket_list[i]:
                if len(output_list) < k:
                    output_list.append(n)
                else:
                    return output_list
        
        return output_list





    
