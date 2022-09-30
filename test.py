while True:             
    print("S3 Automation Main Menu".center(80, "—"))
    print("1. List Buckets")
    print("2. Create a Bucket")
    print("3. Delete a Bucket")
    print("4. Exit")
    selection = input("~~>What would you like to do?:")

    if selection == "1":
        print('1')
    elif selection == "2":
        print('2')
    elif selection == '3':
        print('3')
    elif selection == "4":       
        break  