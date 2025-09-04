def calculate_discount(price, discount_percent):
    """Calculate final price after applying discount if >= 20%."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price


# --- Main Program ---
try:
    # Prompt user for inputs
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(price, discount_percent)

    # Display result
    if discount_percent >= 20:
        print(f"Discount applied! Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Original price: ${final_price:.2f}")

except ValueError:
    print("⚠️ Please enter valid numeric values for price and discount.")
