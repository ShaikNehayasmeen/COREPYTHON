def capitalize_lines():
	print("Enter lines of text (type 'exit' to finish):")
    while True:
        line = input()
        if line.lower() == 'exit':
            break  # Exit the loop if 'exit' is typed
        print(line.upper())


capitalize_lines()
