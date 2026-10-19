import time
start = time.perf_counter()
laptop_value = 55000 * 12
mouse_value = 800 * 50
keyboard_value = 1500 * 25

total = laptop_value + mouse_value + keyboard_value
end = time.perf_counter()
print("Laptop stock value:", laptop_value)
print("Mouse stock value:", mouse_value)
print("Keyboard stock value:", keyboard_value)
print("TOTAL:", total)

print("Time taken:", (end - start) * 1000, "ms")