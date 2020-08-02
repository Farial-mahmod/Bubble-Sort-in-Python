
def bubble_sort(nums):

    # Setting sorting flag to True to run the loop
    sorting = True

    while sorting:
        sorting = False

# Comparing each two adjacent elements as long as initial element > next element
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
			
                # Exchanging elements' positions
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
				
                # Flag set to True indicates further iteration
                sorting = True


# Inputting numbers to test the function bubble_sort()


# User may input any random number
random_nums = [55, 67, 1, 114, 96] 

# Calling the function bubble_sort()
bubble_sort(random_nums)

# Displaying the sorted list
print(random_nums)
