# Problem: Given a list of transactions (strings), group them by item and count the occurrences of each item. Return a list of strings formatted as "item count", sorted first by count in descending order, then alphabetically by item name.
from collections import Counter

def groupTransactions(transactions):
    # Step 1 & 2: Count transactions
    counts = Counter(transactions)
    
    # Step 3: Convert to list of "item count"
    result = [f"{item} {count}" for item, count in counts.items()]
    
    # Step 4: Sort by count desc, then alphabetically
    result.sort(key=lambda x: (-int(x.split()[1]), x.split()[0]))
    
    return result

transactions = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(groupTransactions(transactions))
