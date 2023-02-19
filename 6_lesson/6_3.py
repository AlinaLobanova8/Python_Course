nums = [int(i) for i in input().split()]
# nums = choices(range(3000), k=2000)

# start = time()
m_dict = {}.fromkeys(nums, 0)

for j in nums:
    m_dict[j] += 1

num_count = [1 for i in m_dict.values() if not i % 2]
print(len(num_count))


# print(time() - start)