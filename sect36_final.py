#reverse_string
def reverse_string(str):
    s = ''
    for i, char in enumerate(str[::-1]):
        s += char
    return s

#list_check
def list_check(vals):
    return all(type(l) == list for l in vals)

#remove_every_other
def remove_every_other(lst):
    return [val for i,val in enumerate(lst) if i % 2 == 0]

#sum_pairs
def sum_pairs(ints, s):
    visited_diff = set()
    for n in nums:
        diff = num - n
        if n in visited_diff:
            return [diff, n]
        visited_diff.add(diff)
    return []

#vowel_count
def vowel_count(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}

#Titleize
def titleize(string):
    return ' '.join(word[0].upper() + word[1:] for word in string.split(' '))

#find_factors
def find_factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]

#includes
def includes(collection, value, i=None):
    if type(collection) == dict:
        return value in collection.values()
    if not i:
        return value in collection
    return value in collection[i:]

#repeat
def repeat(string, multiplier):
    if (multiplier == 0):
        return ''
    i = 0
    newStr = ''
    while (i < multiplier):
        newStr += string
        i += 1
    return newStr

#truncate
def truncate(string, n):
    if n < 3:
        return "Truncation must be at least 3 characters."
    if n > (len(string) + 2):
        return string
    return string[:n - 3] + "..."

#two_list_dictionary
def two_list_dictionary(dict1, dict2):
    dict1 = {}.fromkeys(dict1, None)
    dict2_len = len(dict2)
    for i, k in enumerate(dict1.keys()):
        if i < dict2_len:
            dict1[k] = dict2[i]
        else:
            break
    return dict1

#range_in_list
def range_in_list(lst, start=0, end=None):
    end = end or lst[-1]
    return sum(lst[start:end+1])

#same_frequency
def same_frequency(n1,n2):
    str1 = str(n1)
    str2 = str(n2)
    d1 = {c:str1.count(c) for c in str1}
    d2 = {c:str2.count(c) for c in str2}
    
    for (k,v) in d1.items():
        if not k in d2.keys():
            return False
        elif d2[k] != d1[k]:
            return False
    return True

def find_the_duplicate(arr):
    visited_nums = []
    for num in nums:
        if num in visited_nums:
            return num
        visited_nums.append(num)
    return None

#sum_up_diagonals
def sum_up_diagonals(l):
    total = 0
    for i,v in enumerate(l):
        total += l[i][i]
        total += l[i][-1-i]
    return total

#min_max_key_in_dictionary
def min_max_key_in_dictionary(d):
    keys = d.keys()
    return [min(keys), max(keys)]

#find_greater_numbers
def find_greater_numbers(arr):
    count = 0
    i = 0
    j = 1
    while i < len(arr):
        while j < len(arr):
            if arr[j] > arr[i]:
                count += 1
            j+=1
        j = i+1
        i+=1
    return count

# two_oldest
def two_oldest_ages(ages):
    return sorted(ages)[-2:]

#is_odd_string
def is_odd_string(string):
    from string import ascii_lowercase
    return sum(ascii_lowercase.index(c) + 1 for c in string.lower()) % 2 == 1

#valid_parentheses
def valid_parentheses(parens):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

#reverse_vowels
def reverse_vowels(s):
    vowels = "aeiou"
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i].lower() not in vowels:
            i += 1
        elif s[j].lower() not in vowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return "".join(s)

#three_odd_numbers
def three_odd_numbers(nums):
    for i, n in enumerate(nums):
        j = i + 1
        k = j + 1
        if k < len(nums) and (nums[i] + nums[j] + nums[k]) % 2 != 0:
            return True
    return False

#mode
def mode(nums):
    return sorted(set(nums), key=lambda n: nums.count(n))[-1]

#running_average
def running_average():
    running_average.accumulator = 0
    running_average.size = 0
  
    def inner(number):
        running_average.accumulator += number
        running_average.size += 1
        return running_average.accumulator / running_average.size
    
    return inner

#letter_counter
def letter_counter(s):
    letter_counter.s = s.lower()
    def inner(letter):
        return letter_counter.s.count(letter.lower())
    return inner

#once
def once(fn):
    fn.executed = False
    def inner(*args, **kwargs):
        if not fn.executed:
            fn.executed = True
            return fn(*args, **kwargs)
    return inner

#Next Prime Generator
def next_prime():
    num = 2
    primes = set()
    while True:
        for prime in primes:
            if num % prime == 0:
                break
        else:
            primes.add(num)
            yield num
        num += num % 2 + 1