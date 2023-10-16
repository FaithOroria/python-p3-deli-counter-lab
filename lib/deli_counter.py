katz_deli = []

def line(deli_line):
    if not deli_line:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently: "
        for i, customer in enumerate(deli_line, 1):
            line_str += f"{i}. {customer}"
            if i < len(deli_line):
                line_str += " "
        print(line_str)

def take_a_number(deli_line, customer_name):
    deli_line.append(customer_name)
    position = len(deli_line)
    print(f"Welcome, {customer_name}. You are number {position} in line.")

def now_serving(deli_line):
    if not deli_line:
        print("There is nobody waiting to be served!")
    else:
        serving_customer = deli_line.pop(0)
        print(f"Currently serving {serving_customer}.")

# Example usage as described in your question:
take_a_number(katz_deli, "Ada")
take_a_number(katz_deli, "Grace")
take_a_number(katz_deli, "Kent")
line(katz_deli)
now_serving(katz_deli)
line(katz_deli)
take_a_number(katz_deli, "Matz")
line(katz_deli)
now_serving(katz_deli)
line(katz_deli)


