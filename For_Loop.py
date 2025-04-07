# Example 1: calculate salary with bonus

employees = [
    {'name' : 'Sanu', 'base_salary' : 50000, 'bonus_percent' : 10},
    {'name' : 'Atharv', 'base_salary' : 60000, 'bonus_percent' : 15},
    {'name' : 'Anita', 'base_salary' : 55000, 'bonus_percent' : 12},
    {'name' : 'Pinki', 'base_salary' : 70000, 'bonus_percent' : 8},
    {'name' : 'Kartik', 'base_salary' : 100000, 'bonus_percent' : 15}
]

def calculate_salary(base_salary, bonus_perfect):
    return base_salary + (base_salary * bonus_perfect / 100)

for employee in employees:
    final_salary = calculate_salary(employee['base_salary'], employee['bonus_percent'])
    print(f'{employee['name']} - Final Salary: ₹{final_salary:.2f}')


# Example 2: Filter cost whether item is expensive or affordable

items = {'Laptop' : 50000, 'Mouse' : 500, 'Phone' : 20000, 'Tablet' : 30000, 'pendrive' : 800}

for item, price in items.items():
    if price > 25000:
        print(f'Item {item} is Expensive')
        print('. . .')
    else:
        print(f'Item {item} is Affordable')
        print('. . .')



# Example 3: Checking stock levels and reordering items

product_names = ['Apples', 'Bananas', 'Oranges', 'Pears', 'Grapes']

stock_levels = [20, 50, 15, 5, 8]

minimum_stock = 10

reorder_list = []

i = 0

for i in range(len(product_names)):
    if stock_levels[i] < minimum_stock:
        reorder_list.append(product_names[i])

print('Items to Reorder:')
for product in reorder_list:
    print(f'- {product}')


# Example 4: Categorizing heart rate

persons = [
    {'name' : 'Harry', 'heart_rate' : 72},
    {'name' : 'Hermione', 'heart_rate' : 59},
    {'name' : 'Ron', 'heart_rate' : 110},
    {'name' : 'Draco', 'heart_rate' : 90},
    {'name' : 'Dumbledore', 'heart_rate' : 95}
]

def categorize_heart_rate(heart_rate):
    if heart_rate < 60:
        return 'Below Normal'
    elif 60 <= heart_rate <= 100:
        return 'Normal'
    else:
        return 'Above Normal'
    
for person in persons:
    catergory = categorize_heart_rate(person['heart_rate'])
    print(f'{person['name']} - Heart Rate: {person['heart_rate']} bpm, Category: {catergory}')


# Example 5: Check length of strings in a list

words = ['apple', 'banana', 'kiwi', 'watermelon', 'grape']


for word in words:
    if len(word) > 5:
        print(f"'{word}' is a long word with {len(word)} charaters.")
    else:
        print(f"'{word}' is a short word with {len(word)} charaters.")



# Example 6: Square of even numbers in a list

numbers = [1, 4, 12, 9, 7, 8, 18, 21, 26]

for num in numbers:
    if num % 2 == 0:
        print(f'Square of even number {num} is {num ** 2}')
    else:
        print(f'{num} is odd, so no square is calculated')



# Example 7: Check result of students whether pass or fail

students = [
    {'name' : 'Ashwini', 'marks' : 85},
    {'name' : 'Sneha', 'marks' : 40},
    {'name' : 'Nikita', 'marks' : 75},
    {'name' : 'Bob', 'marks' : 30},
    {'name' : 'suthiksh', 'marks' : 92}
]

def evaluate_result(student):
    if student['marks'] >= 50:
        return 'Pass'
    else:
        return 'Fail'
    
for student in students:
    result = evaluate_result(student)
    print(f'{student['name']} - Result: {result}')
    


# Example 8: Check monthly sales is greater or less than threshold value

monthly_sales = [42, 38, 33, 40, 45, 28]

months = ['Jan', 'Feb', 'March', 'April', 'May', 'June']

threshold = 35

for sales_amount, month in zip(monthly_sales, months):
    if sales_amount < threshold:
        print(f'sales amount {sales_amount} is less than threshold in {month}')
        break
    else:
        print(f'sales amount {sales_amount} is greater than threshold in {month}')



# Example 9: Formatting strings

names = ['bob', 'Ash', 'kiran', 'andy', 'satish', 'kajal']

def format_name(name):
    return name.upper()

for name in names:
    formatted_name = format_name(name)
    print(f'Formatted Name: {formatted_name}')


# Example 10: Categorizing scores of students

scores = [85, 60, 45, 92, 77, 35, 67, 73]

for score in scores:
    if score >= 75:
        print(f'Score {score}: Excellent')
    elif 50 <= score < 75:
        print(f'Score {score}: Average')
    else:
        print(f'Score {score}: Poor')

