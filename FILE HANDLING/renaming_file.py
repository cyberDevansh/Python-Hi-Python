import os
old_name="file102.txt"
new_name="file11.txt"
os.rename(old_name,new_name)
print(f"File renamed from {old_name} to {new_name}")