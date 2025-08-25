# 1
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"{self.title} | {self.description} | Due: {self.due_date} | Status: {self.status}"

# 2
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return f"Task '{title}' marked as complete."
        return "Task not found."

    def list_all_tasks(self):
        return "\n".join(str(task) for task in self.tasks) if self.tasks else "No tasks found."

    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if task.status == "Incomplete"]
        return "\n".join(str(task) for task in incomplete) if incomplete else "No incomplete tasks."

def todo_cli():
    todo = ToDoList()
    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date: ")
            task = Task(title, description, due_date)
            todo.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            title = input("Enter task title to mark as complete: ")
            print(todo.mark_task_complete(title))

        elif choice == "3":
            print("\nAll Tasks:")
            print(todo.list_all_tasks())

        elif choice == "4":
            print("\nIncomplete Tasks:")
            print(todo.list_incomplete_tasks())

        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")

# 3
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}"

# 4
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        return "\n\n".join(str(post) for post in self.posts) if self.posts else "No posts found."

    def posts_by_author(self, author):
        posts = [post for post in self.posts if post.author == author]
        return "\n\n".join(str(post) for post in posts) if posts else f"No posts by {author}."

    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                return f"Post '{title}' deleted."
        return "Post not found."

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                return f"Post '{title}' updated."
        return "Post not found."

    def latest_posts(self, n=3):
        return "\n\n".join(str(post) for post in self.posts[-n:]) if self.posts else "No posts found."

def blog_cli():
    blog = Blog()
    while True:
        print("\n--- Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Show Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Show Latest Posts")
        print("7. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter title: ")
            content = input("Enter content: ")
            author = input("Enter author: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post added successfully!")

        elif choice == "2":
            print(blog.list_all_posts())

        elif choice == "3":
            author = input("Enter author name: ")
            print(blog.posts_by_author(author))

        elif choice == "4":
            title = input("Enter post title to delete: ")
            print(blog.delete_post(title))

        elif choice == "5":
            title = input("Enter post title to edit: ")
            new_content = input("Enter new content: ")
            print(blog.edit_post(title, new_content))

        elif choice == "6":
            print(blog.latest_posts())

        elif choice == "7":
            break
        else:
            print("Invalid choice, try again.")

# 5
class Account:
    def __init__(self, acc_number, holder_name, balance=0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} deposited. New Balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"{amount} withdrawn. New Balance: {self.balance}"

    def __str__(self):
        return f"Account No: {self.acc_number} | Holder: {self.holder_name} | Balance: {self.balance}"

# 6
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_number] = account
        return f"Account {account.acc_number} added."

    def check_balance(self, acc_number):
        if acc_number in self.accounts:
            return f"Balance: {self.accounts[acc_number].balance}"
        return "Account not found."

    def deposit(self, acc_number, amount):
        if acc_number in self.accounts:
            return self.accounts[acc_number].deposit(amount)
        return "Account not found."

    def withdraw(self, acc_number, amount):
        if acc_number in self.accounts:
            return self.accounts[acc_number].withdraw(amount)
        return "Account not found."

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >= amount:
                self.accounts[from_acc].withdraw(amount)
                self.accounts[to_acc].deposit(amount)
                return f"Transferred {amount} from {from_acc} to {to_acc}."
            else:
                return "Insufficient funds for transfer."
        return "One or both accounts not found."

    def account_details(self, acc_number):
        return str(self.accounts.get(acc_number, "Account not found."))

def bank_cli():
    bank = Bank()
    while True:
        print("\n--- Banking System Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Account Details")
        print("7. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            acc_number = input("Enter account number: ")
            holder_name = input("Enter holder name: ")
            account = Account(acc_number, holder_name)
            print(bank.add_account(account))

        elif choice == "2":
            acc_number = input("Enter account number: ")
            print(bank.check_balance(acc_number))

        elif choice == "3":
            acc_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            print(bank.deposit(acc_number, amount))

        elif choice == "4":
            acc_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            print(bank.withdraw(acc_number, amount))

        elif choice == "5":
            from_acc = input("From account: ")
            to_acc = input("To account: ")
            amount = float(input("Enter amount to transfer: "))
            print(bank.transfer(from_acc, to_acc, amount))

        elif choice == "6":
            acc_number = input("Enter account number: ")
            print(bank.account_details(acc_number))

        elif choice == "7":
            break
        else:
            print("Invalid choice, try again.")


# 7
def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. ToDo List Application")
        print("2. Blog System")
        print("3. Banking System")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            todo_cli()
        elif choice == "2":
            blog_cli()
        elif choice == "3":
            bank_cli()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


# Run All-in-One Application
main_menu()
