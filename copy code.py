from docx import Document

def extract_menu_from_word(doc_path):
    doc = Document(doc_path)

    menu_items = []

    for paragraph in doc.paragraphs:
        # Implement your logic to extract relevant information
        # For example: Split the paragraph and extract item details
        category, name, description, price = paragraph.text.split(',')

        menu_items.append({
            'category': category,
            'name': name,
            'description': description,
            'price': price
        })

    return menu_items

# Example usage:
word_document_path = 'path/to/your/menu.docx'
menu_data = extract_menu_from_word(word_document_path)
print(menu_data)
