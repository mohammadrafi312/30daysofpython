# # 🟡 Q6 — Tuple Frequency

# Given:

# ```python
# data = (10, 20, 10, 30, 20, 10, 40)
# ```

# Print the frequency of each unique element.

# ### Expected output

# ```text
# 10 : 3
# 20 : 2
# 30 : 1
# 40 : 1
# ```

# ### Requirements

# * Use a **tuple**
# * Use a `for` loop
# * Don't use `collections.Counter`
# * Try to avoid manually writing `data.count(10)`, `data.count(20)`, etc.

# ### 💡 Hint

# You can create an empty dictionary:

# ```python
# frequency = {}
# ```

# Then for each element, keep track of how many times you've seen it.

# Try it yourself first. 🔥

# data = (10, 20, 10, 30, 20, 10, 40)
# count=0
# for i in range(len(data)):
#     for j in range(len(data)):
#         if data[i]==data[j]:
#             count+=1
#         print(data[i],count)
#     # print(f"{i}:{data[i]}")


data = (10, 20, 10, 30, 20, 10, 40)

frequency = {}

for num in data:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for num, count in frequency.items():
    print(num, ":", count)