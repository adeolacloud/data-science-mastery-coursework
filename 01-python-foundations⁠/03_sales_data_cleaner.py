# 03_sales_data_cleaner.py

def clean_raw_sales(raw_records):
    cleaned_records = []
    
    for item in raw_records:
        raw_price = item.get("price")
        raw_qty = item.get("quantity")
        
        # Skip incomplete entries
        if raw_price is None or raw_qty is None:
            continue
            
        try:
            # Clean currency symbols and convert types
            price = float(str(raw_price).replace("$", "").strip())
            quantity = int(raw_qty)
            
            cleaned_records.append({
                "product": item.get("product", "Unknown").title(),
                "unit_price": price,
                "quantity": quantity,
                "total_sales": round(price * quantity, 2)
            })
        except ValueError:
            continue  # Skip corrupt data rows
            
    return cleaned_records

if __name__ == "__main__":
    raw_data = [
        {"product": "cloud storage unit", "price": "$120.50", "quantity": "3"},
        {"product": "python textbook", "price": "$45.00", "quantity": None},
        {"product": "data pipeline tool", "price": "$300.00", "quantity": "2"},
        {"product": "corrupted row", "price": "INVALID", "quantity": "1"}
    ]
    
    cleaned = clean_raw_sales(raw_data)
    for record in cleaned:
        print(record)
